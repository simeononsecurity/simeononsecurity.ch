importScripts('https://cdn.jsdelivr.net/npm/workbox-cdn/workbox/workbox-sw.js');

const CACHE_NAME = 'sos';
const staticAssets = [
  '/',
  '/index.html',
  '/offline.html',
  '/assets/main.js',
  '/assets/prism.js',
  '/img/apple-touch-icon-192.png'
];

self.addEventListener('install', function (event) {
  console.log('[ServiceWorker] Install');
  event.waitUntil((async () => {
    const cache = await caches.open(CACHE_NAME);
    await cache.addAll(staticAssets);
  })());
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  console.log('[ServiceWorker] Activate');
  event.waitUntil((async () => {
    // Enable navigation preload if it's supported.
    // See https://developers.google.com/web/updates/2017/02/navigation-preload
    if ('navigationPreload' in self.registration) {
      await self.registration.navigationPreload.enable();
    }
    return self.clients.claim();
  })());

  // Tell the active service worker to take control of the page immediately.
  self.clients.claim();
});

const cacheFirst = new workbox.strategies.CacheFirst();
const staleWhileRevalidate = new workbox.strategies.StaleWhileRevalidate();
const networkFirst = new workbox.strategies.NetworkFirst();
const navigationHandler = async (params) => {
  const { request } = params;

  // Check if the resource is an image
  if ((request.destination === 'image') && (request.url.startsWith(location.origin) || !request.url.startsWith('http'))) {
    const cacheResponse = await cacheFirst.handle(params);
    return cacheResponse;
  }

  // Check if the resource is a CSS file
  if ((request.destination === 'style') && (request.url.startsWith(location.origin) || !request.url.startsWith('http'))) {
    const cacheResponse = await staleWhileRevalidate.handle(params);
    return cacheResponse;
  }

  // Check if the resource is a JS file
  if ((request.destination === 'script') && (request.url.startsWith(location.origin) || !request.url.startsWith('http'))) {
    const cacheResponse = await staleWhileRevalidate.handle(params);
    return cacheResponse;
  }

  // Check if the resource is a font file
  if ((request.destination === 'font') && (request.url.startsWith(location.origin) || !request.url.startsWith('http'))) {
    const cacheResponse = await cacheFirst.handle(params);
    return cacheResponse;
  }

  // For all other resources from the domain
  if (request.url.startsWith(location.origin) || !request.url.startsWith('http')) {
    const networkResponse = await networkFirst.handle(params);
    return networkResponse;
  }

  // For third-party and offsite resources, do not cache
  return fetch(request);
};

workbox.routing.registerRoute(
  ({ request }) => request.mode === 'navigate',
  navigationHandler
);

workbox.routing.registerRoute(
  ({ request }) => {
    const { destination, url } = request;
    return (
      destination === 'image' &&
      (url.origin === location.origin || !url.origin) // Allow relative paths
    );
  },
  navigationHandler
);

workbox.routing.registerRoute(
  ({ request }) => {
    const { destination, url } = request;
    return (
      destination === 'style' &&
      (url.origin === location.origin || !url.origin) // Allow relative paths
    );
  },
  navigationHandler
);

workbox.routing.registerRoute(
  ({ request }) => {
    const { destination, url } = request;
    return (
      destination === 'script' &&
      (url.origin === location.origin || !url.origin) // Allow relative paths
    );
  },
  navigationHandler
);

workbox.routing.registerRoute(
  ({ request }) => {
    const { destination, url } = request;
    return (
      destination === 'font' &&
      (url.origin === location.origin || !url.origin) // Allow relative paths
    );
  },
  navigationHandler
);

workbox.routing.registerRoute(
  ({ request }) => {
    const { url } = request;
    return url.origin === location.origin;
  },
  navigationHandler
);

