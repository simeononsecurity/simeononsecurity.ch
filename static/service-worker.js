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
      })
    ]
  })
);

self.addEventListener('fetch', function(event) {
  event.respondWith(
    caches.open(CACHE).then(function(cache) {
      return cache.match(event.request).then(function(response) {
        // Return cached resource if found
        if (response) {
          return response;
        }
        // Fetch resource from the network
        return fetch(event.request).then(function(networkResponse) {
          // Cache the fetched resource for future use
          cache.put(event.request, networkResponse.clone());
          return networkResponse;
        }).catch(function(error) {
          // Handle fetch errors gracefully
          console.log('Fetch failed:', error);
          // Return a fallback response or simply allow the browser to fetch the resource
          return fetch(event.request);
        });
      });
    })
  );
});
