/**
 * Service Worker — simeononsecurity.com  v4
 *
 * New in v4:
 *   • SW update notification  — broadcasts SW_UPDATED to all open tabs on activate
 *   • Page cache TTL           — pages older than PAGE_TTL_MS are treated as stale
 *   • MAX_PAGES limit          — CACHE_PAGES auto-trims like CACHE_IMAGES
 *   • Adaptive strategy        — slow/2g connections get cache-first navigation
 *
 * Cache strategy summary:
 *   Pages (navigate)     → network-first (cache-first on slow 2g); TTL 24 h; max 100
 *   Assets (CSS/JS/font) → cache-first + background refresh
 *   Images               → stale-while-revalidate; max 80
 *   Prefetch (links)     → background fetch via postMessage; max 50
 *
 * To evict old caches, increment CACHE_VERSION.
 */

// ── Version & cache names ────────────────────────────────────────────────────
const CACHE_VERSION  = 4;
const CACHE_PAGES    = 'sos-pages-v'    + CACHE_VERSION;
const CACHE_ASSETS   = 'sos-assets-v'   + CACHE_VERSION;
const CACHE_IMAGES   = 'sos-images-v'   + CACHE_VERSION;
const CACHE_PREFETCH = 'sos-prefetch-v' + CACHE_VERSION;
const ALL_CACHES     = [CACHE_PAGES, CACHE_ASSETS, CACHE_IMAGES, CACHE_PREFETCH];

// ── Limits & TTL ─────────────────────────────────────────────────────────────
const MAX_PAGES    = 100;
const MAX_IMAGES   = 80;
const MAX_PREFETCH = 50;
const PAGE_TTL_MS  = 24 * 60 * 60 * 1000; // 24 hours

// ── Shell assets (must exist; cached individually so one 404 ≠ install abort) ─
const SHELL_ASSETS = ['/', '/offline.html', '/js/ping.js', '/js/search.js'];
const OFFLINE_URL  = '/offline.html';

// ── Extension sets ───────────────────────────────────────────────────────────
const ASSET_EXTS = new Set(['css', 'js', 'mjs', 'woff', 'woff2', 'ttf', 'otf', 'eot']);
const IMAGE_EXTS = new Set(['webp', 'jpg', 'jpeg', 'png', 'gif', 'svg', 'ico', 'avif']);

// Track whether this is an upgrade (existing SW replaced) vs. fresh install
let isFreshInstall = true;

// ── Shared helpers ────────────────────────────────────────────────────────────

function isSameOrigin(url) {
    try { return new URL(url).origin === self.location.origin; }
    catch (e) { return false; }
}

function getExt(url) {
    try {
        const p   = new URL(url).pathname;
        const dot = p.lastIndexOf('.');
        return dot >= 0 ? p.slice(dot + 1).toLowerCase() : '';
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

/** Returns true if navigator.connection signals 2G or slower. */
function isSlowConnection() {
    try {
        const conn = self.navigator && self.navigator.connection;
        if (!conn) return false;
        return conn.effectiveType === 'slow-2g' || conn.effectiveType === '2g';
    } catch (e) { return false; }
}

/**
 * Cache a page response with an X-Cached-At timestamp header.
 * The caller must own a separate clone to return to the browser.
 */
async function cachePageResponse(cache, request, responseClone) {
    try {
        const body    = await responseClone.arrayBuffer();
        const headers = new Headers(responseClone.headers);
        headers.set('X-Cached-At', String(Date.now()));
        await cache.put(
            request,
            new Response(body, {
                status:     responseClone.status,
                statusText: responseClone.statusText,
                headers,
            })
        );
    } catch (e) {
        // If cloning failed just skip — not catastrophic
    }
}

/** True when a cached page response is past its TTL. */
function isPageStale(cachedResponse) {
    const ts = cachedResponse.headers.get('X-Cached-At');
    if (!ts) return false; // no timestamp = assume not stale (legacy entry)
    return (Date.now() - parseInt(ts, 10)) > PAGE_TTL_MS;
}

async function safeFetch(url, options) {
    try { return await fetch(url, options); }
    catch (e) { return null; }
}

// ── Install ───────────────────────────────────────────────────────────────────
self.addEventListener('install', function (event) {
    // If there is already an active SW this is an upgrade, not a fresh install
    isFreshInstall = !self.registration.active;
    console.log('[SW] Install v' + CACHE_VERSION, isFreshInstall ? '(fresh)' : '(update)');

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

// ── Activate ──────────────────────────────────────────────────────────────────
self.addEventListener('activate', function (event) {
    console.log('[SW] Activate v' + CACHE_VERSION);
    event.waitUntil(
        Promise.all([
            // Evict stale caches from previous versions
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
            // Enable navigation preload
            self.registration.navigationPreload
                ? self.registration.navigationPreload.enable()
                : Promise.resolve(),
            // Take control of all open tabs
            self.clients.claim(),
        ]).then(function () {
            // Only broadcast update toast when replacing an existing SW
            if (!isFreshInstall) {
                self.clients
                    .matchAll({ type: 'window', includeUncontrolled: true })
                    .then(function (clients) {
                        clients.forEach(function (client) {
                            client.postMessage({
                                type:    'SW_UPDATED',
                                version: CACHE_VERSION,
                            });
                        });
                    });
            }
        })
    );
});

// ── Message handler ───────────────────────────────────────────────────────────
self.addEventListener('message', function (event) {
    if (!event.data || typeof event.data.type !== 'string') return;

    if (event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
        return;
    }

    if (event.data.type === 'PREFETCH_LINKS') {
        const urls = (event.data.urls || []).slice(0, 8);
        if (!urls.length) return;

        event.waitUntil(
            (async function () {
                const cache = await caches.open(CACHE_PREFETCH);
                for (const url of urls) {
                    if (!isSameOrigin(url)) continue;
                    const ext = getExt(url);
                    if (ASSET_EXTS.has(ext) || IMAGE_EXTS.has(ext)) continue;
                    const hit = await caches.match(url);
                    if (hit) continue;

                    const response = await safeFetch(url, {
                        credentials: 'same-origin',
                        headers: { 'Purpose': 'prefetch', 'Sec-Purpose': 'prefetch' },
                    });
                    if (response && response.ok && response.type === 'basic') {
                        await cachePageResponse(cache, url, response);
                        console.log('[SW] Prefetched:', url);
                    }
                }
                await trimCache(CACHE_PREFETCH, MAX_PREFETCH);
            })()
        );
    }
});

// ── Fetch ─────────────────────────────────────────────────────────────────────
self.addEventListener('fetch', function (event) {
    const req = event.request;
    if (req.method !== 'GET' || !isSameOrigin(req.url)) return;

    const category = categorize(req);

    // ── 1. Navigation: adaptive network-first (cache-first on slow connections) ──
    if (category === 'page') {
        event.respondWith(
            (async function () {
                const pageCache = await caches.open(CACHE_PAGES);

                // ▸ SLOW CONNECTION: try cache first (skip network latency)
                if (isSlowConnection()) {
                    const cached = await pageCache.match(req);
                    if (cached && !isPageStale(cached)) {
                        // Refresh in background so next visit is fresh
                        fetch(req).then(async function (r) {
                            if (r && r.ok) {
                                await cachePageResponse(pageCache, req, r.clone());
                                await trimCache(CACHE_PAGES, MAX_PAGES);
                            }
                        }).catch(function () {});
                        return cached;
                    }
                    // Cache miss or stale — fall through to normal network-first
                }

                // ▸ NORMAL: network-first
                try {
                    const preload = await event.preloadResponse;
                    const networkResponse = preload || await fetch(req);

                    if (networkResponse.ok) {
                        await cachePageResponse(pageCache, req, networkResponse.clone());
                        trimCache(CACHE_PAGES, MAX_PAGES);
                    }
                    return networkResponse;

                } catch (err) {
                    // Offline fallback chain
                    const fromPages = await pageCache.match(req);
                    if (fromPages) return fromPages;

                    const fromPrefetch = await caches.match(req, { cacheName: CACHE_PREFETCH });
                    if (fromPrefetch) return fromPrefetch;

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

    // ── 2. Assets (CSS/JS/fonts): cache-first + background refresh ───────────
    if (category === 'asset') {
        event.respondWith(
            (async function () {
                const cached = await caches.match(req);

                const fetchAndCache = fetch(req).then(function (r) {
                    if (r && r.ok && r.type === 'basic') {
                        caches.open(CACHE_ASSETS).then(function (c) { c.put(req, r.clone()); });
                    }
                    return r;
                }).catch(function () { return null; });

                if (cached) return cached;
                return (await fetchAndCache) || new Response('', { status: 503 });
            })()
        );
        return;
    }

    // ── 3. Images: stale-while-revalidate ────────────────────────────────────
    if (category === 'image') {
        event.respondWith(
            (async function () {
                const cached = await caches.match(req);

                const fetchPromise = fetch(req).then(async function (r) {
                    if (r && r.ok && r.type === 'basic') {
                        const c = await caches.open(CACHE_IMAGES);
                        c.put(req, r.clone());
                        trimCache(CACHE_IMAGES, MAX_IMAGES);
                    }
                    return r;
                }).catch(function () { return null; });

                return cached || fetchPromise;
            })()
        );
        return;
    }

    // ── 4. Everything else: pass through ────────────────────────────────────
});
