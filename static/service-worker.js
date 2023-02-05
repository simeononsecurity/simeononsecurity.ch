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

const CACHE_NAME = 'offline';
const OFFLINE_URL = 'offline.html';

self.addEventListener('install', function (event) {
    console.log('[ServiceWorker] Install');

    event.waitUntil((async () => {
        const cache = await caches.open(CACHE_NAME);
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

// Listen for the `fetch` event
self.addEventListener('fetch', function (event) {
    if (event.request.url.includes('https://simeononsecurity.ch/rss.xml')) {
        event.respondWith(
            fetch(event.request)
            .then(function (response) {
                return response.text().then(function (xmlString) {
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
                });
            })
            .catch(function (error) {
                console.error('Fetch error:', error);
            })
        );
        event.waitUntil(
            // Perform any other long-running tasks here, such as updating the cache
            // ...
        );
    }
});
