// This is the service worker with the combined offline experience (Offline page + Offline copy of pages)

const CACHE = "pwabuilder-offline-page";

importScripts('https://storage.googleapis.com/workbox-cdn/releases/5.1.2/workbox-sw.js');

const offlineFallbackPage = "/offline.html";

self.addEventListener("message", (event) => {
  if (event.data && event.data.type === "SKIP_WAITING") {
    self.skipWaiting();
  }
});

self.addEventListener('install', async (event) => {
  event.waitUntil(
    caches.open(CACHE)
    .then((cache) => cache.add(offlineFallbackPage))
    .then(() => {
      const staticAssets = [
        '/',
        '/index.html',
        '/offline.html',
        '/assets/main.js',
        '/assets/prism.js',
        '/img/apple-touch-icon-192.png'
      ];

      return caches.open(CACHE).then((cache) => cache.addAll(staticAssets));
    })
  );
});

if (workbox.navigationPreload.isSupported()) {
  workbox.navigationPreload.enable();
}

workbox.routing.registerRoute(
  new RegExp('/*'),
  new workbox.strategies.StaleWhileRevalidate({
    cacheName: CACHE,
    plugins: [
      new workbox.expiration.ExpirationPlugin({
        maxEntries: 50, // Adjust the number of cached entries as needed
        purgeOnQuotaError: true
      }),
      new workbox.cacheableResponse.CacheableResponsePlugin({
        statuses: [200]
      }),
      new workbox.broadcastUpdate.BroadcastUpdatePlugin(),
    ]
  })
);

self.addEventListener('fetch', (event) => {
  const { request } = event;

  // Skip handling of external resources
  if (!request.url.startsWith(self.location.origin)) {
    return;
  }

  event.respondWith(
    caches.match(request)
      .then((cachedResponse) => {
        if (cachedResponse) {
          return cachedResponse;
        }

        return fetch(request)
          .then((response) => {
            // Clone the response since it can only be consumed once
            const responseClone = response.clone();

            caches.open(CACHE)
              .then((cache) => {
                cache.put(request, responseClone);
              });

            return response;
          });
      })
      .catch(() => {
        // Return the offline fallback page if any error occurs
        return caches.match(offlineFallbackPage);
      })
  );
});
