const cacheName = 'sos';
const staticAssets = [
    '/',
    '/index.html',
    '/offline.html',
    '/style.css',
    '/assets/style.css',
    '/assets/main.js',
    '/assets/prism.js',
    '/img/apple-touch-icon-192.png'
];

const OFFLINE_URL = 'offline.html';

self.addEventListener('install', function (event) {
    console.log('[ServiceWorker] Install');

    event.waitUntil((async () => {
        const cache = await caches.open(cacheName);
        await cache.addAll(staticAssets);
        // Setting {cache: 'reload'} in the new request will ensure that the response
        // isn't fulfilled from the HTTP cache; i.e., it will be from the network.
        await cache.add(new Request(OFFLINE_URL, {
            cache: 'reload'
        }));
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
    })());

    // Tell the active service worker to take control of the page immediately.
    self.clients.claim();
});

self.addEventListener('fetch', function (event) {
    console.log('Fetch Event Activated:');
    if (event.request.url.includes('https://simeononsecurity.ch/rss.xml')) {
        console.log("url included https://simeononsecurity.ch/rss.xml");
        console.log(event.request);
        event.respondWith(
            fetch(event.request)
            .then(async function (response) {
                const xmlString = await response.text();
                const parser = new DOMParser();
                const xml = parser.parseFromString(xmlString, 'text/xml');
                const latestArticle = xml.querySelector('item');
                const latestArticleTitle = latestArticle.querySelector('title').textContent;
                const latestArticleLink = latestArticle.querySelector('link').textContent;
                console.log(parser);
                // Check if there is a new article
                if (localStorage.getItem('latestArticleLink') !== latestArticleLink) {
                    localStorage.setItem('latestArticleLink', latestArticleLink);
                    // Show notification with the latest article title
                    self.registration.showNotification(latestArticleTitle, {
                        body: 'A new article is available!',
                        tag: 'new-article-notification',
                    });
                }
                return response;
            })
            .catch(function (error) {
                console.error('Fetch error:', error);
            })
        );
        event.waitUntil(async function() {
            try {
                const response = await fetch(event.request);
                const cache = await caches.open(cacheName);
                await cache.put(event.request, response.clone());
            } catch (error) {
                console.error(error);
            }
        }());
    } else {
        event.respondWith(async function() {
            try {
                const cache = await caches.open(cacheName);
                const cachedResponse = await cache.match(event.request);
                if (cachedResponse) {
                    return cachedResponse;
                }
                const response = await fetch(event.request);
                await cache.put(event.request, response.clone());
                return response;
            } catch (error) {
                console.error(error);
                const cache = await caches.open(cacheName);
                const cachedResponse = await cache.match(OFFLINE_URL);
                if (cachedResponse) {
                    return cachedResponse;
                }
            }
        }());
    }
});
