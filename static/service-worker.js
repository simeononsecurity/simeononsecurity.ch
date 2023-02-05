const CACHE_NAME = 'sos';
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
    })());

    // Tell the active service worker to take control of the page immediately.
    self.clients.claim();
});

self.addEventListener('fetch', function (event) {
    if (event.request.mode === 'navigate' || staticAssets.includes(event.request.url)) {
        event.respondWith((async () => {
            try {
                const preloadResponse = await event.preloadResponse;
                if (preloadResponse) {
                    return preloadResponse;
                }

                const networkResponse = await fetch(event.request);
                if (networkResponse.status === 200 && networkResponse.type === 'basic') {
                    const cache = await caches.open(CACHE_NAME);
                    cache.put(event.request, networkResponse.clone());
                }
                return networkResponse;
            } catch (error) {
                console.log('[Service Worker] Fetch failed; returning offline page instead.', error);

                const cache = await caches.open(CACHE_NAME);
                const cachedResponse = await cache.match(OFFLINE_URL);
                return cachedResponse;
            }
        })());
    }
});

const fetchRss = async () => {
    const rssUrl = 'https://simeononsecurity.ch/rss.xml';
    let parser;
    if (typeof window !== "undefined" && typeof window.DOMParser !== "undefined") {
        parser = new window.DOMParser();
        console.log(parser);
    } else if (typeof self !== "undefined" && typeof self.DOMParser !== "undefined") {
        parser = new self.DOMParser();
        console.log(parser);
    } else {
        // handle the error here, such as logging a message or throwing an exception
        console.error("The DOMParser is not available in this context");
        return;
    }
        try {
            const response = await fetch(rssUrl);
            console.log(response);
            const text = await response.text();
            console.log(text);
            const xml = parser.parseFromString(text, "text/xml");
            console.log(xml);
            const items = xml.querySelectorAll("item");
            console.log(items);
            const rssData = Array.from(items).map(item => {
                const title = item.querySelector("title").textContent;
                const link = item.querySelector("link").textContent;
                return {
                    title,
                    link
                };
            });
            console.log(rssData);
            return rssData;
        } catch (error) {
            console.error(`Failed to fetch RSS data: ${error}`);
            console.error(error.stack);
            return null;
        }

};

setInterval(async () => {
    const rssData = await fetchRss();
    if (rssData) {
        const lastPost = rssData[0];
        if (lastPost) {
            // Check if this is a new post compared to what we have stored locally
            const localLastPost = localStorage.getItem('lastPost');
            if (!localLastPost || lastPost.title !== localLastPost) {
                localStorage.setItem('lastPost', lastPost.title);
                // Trigger the push event to show the notification
                self.dispatchEvent(new PushEvent('push', {
                    data: lastPost
                }));
            }
        }
    }
}, 60000);

self.addEventListener('push', event => {
    const data = event.data.json();
    const options = {
        body: `${data.title}`,
        badge: '/img/apple-touch-icon-192.png'
    };
    event.waitUntil(self.registration.showNotification('New Post', options));
});