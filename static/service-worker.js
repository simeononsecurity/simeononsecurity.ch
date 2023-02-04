const cacheName = 'sos';
const staticAssets = [
  '/',
  '/index.html',
  '/style.css',
  '/assets/style.css',
  '/assets/main.js',
  '/assets/prism.js',
  '/img/apple-touch-icon-192.png'
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(cacheName)
      .then(cache => {
        cache.addAll(staticAssets);
      })
  );
});

self.addEventListener('fetch', event => {
  event.respondWith(
    caches.match(event.request)
      .then(response => {
        return response || fetch(event.request);
      })
  );
});
