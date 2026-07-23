/**
 * Service Worker — simeononsecurity.com
 *
 * Cache strategy by resource type:
 *   Pages (navigate)   → network-first, cache on success; offline → pages cache → prefetch cache → /offline.html
 *   Assets (CSS/JS/font) → cache-first, background refresh (stale-while-revalidate style)
 *   Images              → stale-while-revalidate; trim to MAX_IMAGES
 *   Link prefetch       → background fetch on postMessage from page; trim to MAX_PREFETCH
 *
 * Bump CACHE_VERSION to evict all old caches on next activate.
 */

const CACHE_VERSION  = 3;
const CACHE_PAGES    = 'sos-pages-v'    + CACHE_VERSION;  // navigations
const CACHE_ASSETS   = 'sos-assets-v'   + CACHE_VERSION;  // CSS / JS / fonts
const CACHE_IMAGES   = 'sos-images-v'   + CACHE_VERSION;  // images (s-w-r)
const CACHE_PREFETCH = 'sos-prefetch-v' + CACHE_VERSION;  // proactive link prefetch

const ALL_CACHES  = [CACHE_PAGES, CACHE_ASSETS, CACHE_IMAGES, CACHE_PREFETCH];
const MAX_IMAGES  = 80;   // oldest entries trimmed beyond this
const MAX_PREFETCH = 50;  // oldest prefetched pages trimmed beyond this

// Minimal app shell — only paths guaranteed to exist in the built site.
// Each asset is cached individually so a single 404 never aborts the install.
const SHELL_ASSETS = [
    '/',
    '/offline.html',
    '/js/ping.js',
    '/js/search.js',
];

const OFFLINE_URL = '/offline.html';

// Static-asset extensions for the cache-first strategy
const ASSET_EXTS  = new Set(['css', 'js', 'mjs', 'woff', 'woff2', 'ttf', 'otf', 'eot']);
// Image extensions for the stale-while-revalidate strategy
const IMAGE_EXTS  = new Set(['webp', 'jpg', 'jpeg', 'png', 'gif', 'svg', 'ico', 'avif']);

// ── Helpers ─────────────────────────────────────────────────────────────────

function isSameOrigin(url) {
    try { return new URL(url).origin === self.location.origin; }
    catch (e) { return false; }
}

function getExt(url) {
    try {
        const path = new URL(url).pathname;
        const dot  = path.lastIndexOf('.');
        return dot >= 0 ? path.slice(dot + 1).toLowerCase() : '';
    } catch (e) { return ''; }
}

function categorize(request) {
    if (request.mode === 'navigate') return 'page';
    const ext = getExt(request.url);
    if (ASSET_EXTS.has(ext)) return 'asset';
    if (IMAGE_EXTS.has(ext)) return 'image';
    return 'other';
}

async function trimCache(cacheName, maxItems) {
    const cache = await caches.open(cacheName);
    const keys  = await cache.keys();
    if (keys.length > maxItems) {
        await Promise.all(
            keys.slice(0, keys.length - maxItems).map(k => cache.delete(k))
        );
    }
}

async function safeFetch(url, options) {
    try {
        const r = await fetch(url, options);
        return r;
    } catch (e) {
        return null;
    }
}

// ── Install ──────────────────────────────────────────────────────────────────
self.addEventListener('install', function (event) {
    console.log('[SW] Install v' + CACHE_VERSION);
    event.waitUntil(
        caches.open(CACHE_ASSETS).then(function (cache) {
            return Promise.all(
                SHELL_ASSETS.map(function (url) {
                    return cache.add(url).catch(function (err) {
                        console.warn('[SW] Shell asset skipped:', url, err.message);
                    });
                })
            );
        })
    );
    self.skipWaiting();
});

// ── Activate ─────────────────────────────────────────────────────────────────
self.addEventListener('activate', function (event) {
    console.log('[SW] Activate v' + CACHE_VERSION);
    event.waitUntil(
        Promise.all([
            // Evict every cache that isn't from the current version
            caches.keys().then(function (keys) {
                return Promise.all(
                    keys.map(function (key) {
                        if (!ALL_CACHES.includes(key)) {
                            console.log('[SW] Deleting stale cache:', key);
                            return caches.delete(key);
                        }
                    })
                );
            }),
            // Enable navigation preload for faster first-byte on navigations
            self.registration.navigationPreload
                ? self.registration.navigationPreload.enable()
                : Promise.resolve(),
            // Claim all open clients immediately
            self.clients.claim(),
        ])
    );
});

// ── Message handler ──────────────────────────────────────────────────────────
//
// Page sends:
//   { type: 'PREFETCH_LINKS', urls: ['https://...', ...] }
//   { type: 'SKIP_WAITING' }
//
self.addEventListener('message', function (event) {
    if (!event.data || typeof event.data.type !== 'string') return;

    if (event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
        return;
    }

    if (event.data.type === 'PREFETCH_LINKS') {
        var urls = event.data.urls;
        if (!Array.isArray(urls) || urls.length === 0) return;

        // Cap per-message batch to avoid overwhelming the network
        urls = urls.slice(0, 8);

        event.waitUntil(
            (async function () {
                const cache = await caches.open(CACHE_PREFETCH);

                for (const url of urls) {
                    // Sanity-check: only prefetch same-origin page URLs
                    if (!isSameOrigin(url)) continue;
                    const ext = getExt(url);
                    if (ASSET_EXTS.has(ext) || IMAGE_EXTS.has(ext)) continue;

                    // Skip if already cached in any cache
                    const hit = await caches.match(url);
                    if (hit) continue;

                    const response = await safeFetch(url, {
                        credentials: 'same-origin',
                        headers: { 'Purpose': 'prefetch', 'Sec-Purpose': 'prefetch' },
                    });

                    if (response && response.ok && response.type === 'basic') {
                        await cache.put(url, response);
                        console.log('[SW] Prefetched:', url);
                    }
                }

                await trimCache(CACHE_PREFETCH, MAX_PREFETCH);
            })()
        );
    }
});

// ── Fetch handler ─────────────────────────────────────────────────────────────
self.addEventListener('fetch', function (event) {
    const req = event.request;

    // Only handle GET requests to the same origin
    if (req.method !== 'GET' || !isSameOrigin(req.url)) return;

    const category = categorize(req);

    // ── 1. Navigation pages: network-first ──────────────────────────────────
    if (category === 'page') {
        event.respondWith(
            (async function () {
                try {
                    // Use navigation preload when available
                    const preload = await event.preloadResponse;
                    if (preload) {
                        const cache = await caches.open(CACHE_PAGES);
                        cache.put(req, preload.clone());
                        return preload;
                    }

                    const response = await fetch(req);
                    if (response.ok) {
                        const cache = await caches.open(CACHE_PAGES);
                        cache.put(req, response.clone());
                    }
                    return response;

                } catch (err) {
                    // Offline fallback chain: pages → prefetch → /offline.html
                    const fromPages = await caches.match(req, { cacheName: CACHE_PAGES });
                    if (fromPages) return fromPages;

                    const fromPrefetch = await caches.match(req, { cacheName: CACHE_PREFETCH });
                    if (fromPrefetch) return fromPrefetch;

                    // Last resort: check all caches, then serve /offline.html
                    const anywhere = await caches.match(req);
                    if (anywhere) return anywhere;

                    const offline = await caches.match(OFFLINE_URL);
                    return offline || new Response('Offline', {
                        status: 503,
                        headers: { 'Content-Type': 'text/plain' },
                    });
                }
            })()
        );
        return;
    }

    // ── 2. Static assets (CSS/JS/fonts): cache-first + background refresh ───
    if (category === 'asset') {
        event.respondWith(
            (async function () {
                const cached = await caches.match(req);

                // Refresh the cache asynchronously while serving the stale copy
                const fetchAndCache = fetch(req).then(function (response) {
                    if (response && response.ok && response.type === 'basic') {
                        caches.open(CACHE_ASSETS).then(function (cache) {
                            cache.put(req, response.clone());
                        });
                    }
                    return response;
                }).catch(function () { return null; });

                // Return cached immediately if we have it
                if (cached) return cached;

                // First-time fetch: wait for network
                const fresh = await fetchAndCache;
                if (fresh) return fresh;

                return new Response('', { status: 503 });
            })()
        );
        return;
    }

    // ── 3. Images: stale-while-revalidate ───────────────────────────────────
    if (category === 'image') {
        event.respondWith(
            (async function () {
                const cached = await caches.match(req);

                // Always refresh in the background
                const fetchPromise = fetch(req).then(async function (response) {
                    if (response && response.ok && response.type === 'basic') {
                        const cache = await caches.open(CACHE_IMAGES);
                        cache.put(req, response.clone());
                        trimCache(CACHE_IMAGES, MAX_IMAGES);
                    }
                    return response;
                }).catch(function () { return null; });

                // Serve cached copy immediately; wait for network only on cache miss
                return cached || fetchPromise;
            })()
        );
        return;
    }

    // ── 4. Everything else: pass through to network (don't intercept) ────────
    // (API calls, external resources, etc.)
});
