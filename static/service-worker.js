// Cache version — bump this string on every meaningful deploy to evict old caches.
const CACHE_NAME = 'sos-v2';

// Only include assets that are guaranteed to exist in the built site.
// If any URL in cache.addAll() returns non-2xx the ENTIRE install fails,
// so keep this list lean and verified.
const SHELL_ASSETS = [
    '/',
    '/offline.html',
    '/js/ping.js',
    '/js/search.js',
];

const OFFLINE_URL = '/offline.html';

// ── Install: cache the app shell ─────────────────────────────────────────────
self.addEventListener('install', function (event) {
    console.log('[ServiceWorker] Install', CACHE_NAME);
    event.waitUntil(
        caches.open(CACHE_NAME).then(function (cache) {
            // Cache shell assets one at a time so a single 404 doesn't abort
            // the whole install.
            return Promise.all(
                SHELL_ASSETS.map(function (url) {
                    return cache.add(url).catch(function (err) {
                        console.warn('[ServiceWorker] Failed to cache shell asset:', url, err);
                    });
                })
            );
        })
    );
    // Activate the new SW immediately without waiting for old tabs to close.
    self.skipWaiting();
});

// ── Activate: clean up caches from previous versions ─────────────────────────
self.addEventListener('activate', function (event) {
    console.log('[ServiceWorker] Activate', CACHE_NAME);
    event.waitUntil(
        Promise.all([
            // Delete every cache that doesn't match the current version.
            caches.keys().then(function (cacheNames) {
                return Promise.all(
                    cacheNames.map(function (name) {
                        if (name !== CACHE_NAME) {
                            console.log('[ServiceWorker] Deleting old cache:', name);
                            return caches.delete(name);
                        }
                    })
                );
            }),
            // Enable navigation preload if supported (faster page loads).
            (self.registration.navigationPreload
                ? self.registration.navigationPreload.enable()
                : Promise.resolve()),
            // Take control of all open clients right away.
            self.clients.claim(),
        ])
    );
});

// ── Fetch: network-first with cache fallback for navigation requests ──────────
self.addEventListener('fetch', function (event) {
    // Only intercept same-origin navigation requests (full-page loads).
    // Let sub-resources (images, scripts, etc.) go straight to the network.
    if (event.request.mode !== 'navigate') return;

    event.respondWith(
        (async function () {
            try {
                // Use the preload response if navigation preload is active.
                const preload = await event.preloadResponse;
                if (preload) return preload;

                const networkResponse = await fetch(event.request);

                // Cache successful same-origin responses for future offline use.
                if (networkResponse.ok && networkResponse.type === 'basic') {
                    const cache = await caches.open(CACHE_NAME);
                    cache.put(event.request, networkResponse.clone());
                }
                return networkResponse;

            } catch (err) {
                // Network unavailable — try the cache, then fall back to offline page.
                console.log('[ServiceWorker] Network fetch failed, trying cache.', err);
                const cached = await caches.match(event.request);
                if (cached) return cached;

                const offline = await caches.match(OFFLINE_URL);
                return offline || new Response('Offline', { status: 503 });
            }
        })()
    );
});
