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
        return self.clients.claim();
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

let stoprss = false;

const fetchRss = async () => {
    const rssUrl = 'https://simeononsecurity.ch/rss.xml';
    let parser;
    if (typeof window !== "undefined" && typeof window.DOMParser !== "undefined") {
        parser = new window.DOMParser();
        console.log('DOMParser is Window');
    } else if (typeof self !== "undefined" && typeof self.DOMParser !== "undefined") {
        parser = new self.DOMParser();
        console.log('DOMParser is Self');
    } else {
        // handle the error here, such as logging a message or throwing an exception
        console.error("The DOMParser is not available in this context");
        stoprss = true;
        return;
    }
    try {
        let response = await fetch(rssUrl);
        console.log(response);
        let text = await response.text();
        console.log(text);
        let xml = parser.parseFromString(text, "text/xml");
        let itemsArray = Array.from(xml.getElementsByTagName("item"));
        let rssData = itemsArray.map(item => 
            ({title: item.getElementsByTagName("title")[0].innerText, 
              link: item.getElementsByTagName("link")[0].innerText }));
        return rssData;
        console.log(rssData);
        return rssData;
    } catch (error) {
        console.error(`Failed to fetch RSS data: ${error}`);
        console.error(error.stack);
        return null;
    }

};


setInterval(async () => {
    if (stoprss != true) {
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
    }
}, 60000);


// https://geekflare.com/convert-webapp-to-pwa/

self.addEventListener('push', event => {
    const data = event.data.json();
    const options = {
        body: `${data.title}`,
        badge: '/img/apple-touch-icon-192.png'
    };
    event.waitUntil(self.registration.showNotification('New Post', options));
});

if ('Notification' in window && Notification.permission != 'granted') {
    console.log('Ask user permission')
    Notification.requestPermission(status => {  
        console.log('Status:'+status)
        displayNotification('Notification Enabled');
    });
}

const displayNotification = notificationTitle => {
    console.log('display notification')
    if (Notification.permission == 'granted') {
        navigator.serviceWorker.getRegistration().then(reg => {
            console.log(reg)
            const options = {
                    body: 'Thanks for allowing push notification !',
                    icon:  '/img/apple-touch-icon-144-precomposed.png',
                    vibrate: [100, 50, 100],
                    data: {
                      dateOfArrival: Date.now(),
                      primaryKey: 0
                    }
                  };
    
            reg.showNotification(notificationTitle, options);
        });
    }
};

const updateSubscriptionOnYourServer = subscription => {
    console.log('Write your ajax code here to save the user subscription in your DB', subscription);
    // write your own ajax request method using fetch, jquery, axios to save the subscription in your server for later use.
};

const subscribeUser = async () => {
    const swRegistration = await navigator.serviceWorker.getRegistration();
    const applicationServerPublicKey = ''; // paste your webpush certificate public key
    const applicationServerKey = urlB64ToUint8Array(applicationServerPublicKey);
    swRegistration.pushManager.subscribe({
      userVisibleOnly: true,
      applicationServerKey
    })
    .then((subscription) => {
        console.log('User is subscribed newly:', subscription);
        updateSubscriptionOnServer(subscription);
    })
    .catch((err) => {
        if (Notification.permission === 'denied') {
          console.warn('Permission for notifications was denied')
        } else {
          console.error('Failed to subscribe the user: ', err)
        }
    });
};
const urlB64ToUint8Array = (base64String) => {
    const padding = '='.repeat((4 - base64String.length % 4) % 4)
    const base64 = (base64String + padding)
        .replace(/\-/g, '+')
        .replace(/_/g, '/')

    const rawData = window.atob(base64);
    const outputArray = new Uint8Array(rawData.length);

    for (let i = 0; i < rawData.length; ++i) {
        outputArray[i] = rawData.charCodeAt(i);
    }
    return outputArray;
};

const checkSubscription = async () => {
    const swRegistration = await navigator.serviceWorker.getRegistration();
    swRegistration.pushManager.getSubscription()
    .then(subscription => {
        if (!!subscription) {
            console.log('User IS Already subscribed.');
            updateSubscriptionOnYourServer(subscription);
        } else {
            console.log('User is NOT subscribed. Subscribe user newly');
            subscribeUser();
        }
    });
};

checkSubscription();

self.addEventListener('push', (event) => {
    const json = JSON.parse(event.data.text())
    console.log('Push Data', event.data.text())
    self.registration.showNotification(json.header, json.options)
  });