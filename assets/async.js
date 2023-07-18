// Start Load Service Worker

const divInstall = document.getElementById('installContainer');
const butInstall = document.getElementById('butInstall');

// Register the service worker
if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('/service-worker.js').then(function(registration) {
      console.log('Service Worker registration successful with scope: ', registration.scope);
    }, function(err) {
      console.log('Service Worker registration failed: ', err);
    });
  });
}

/**
 * Warn the page must be served over HTTPS
 * The `beforeinstallprompt` event won't fire if the page is served over HTTP.
 * Installability requires a service worker with a fetch event handler, and
 * if the page isn't served over HTTPS, the service worker won't load.
if (window.location.protocol === 'http:') {
  const requireHTTPS = document.getElementById('requireHTTPS');
  const link = requireHTTPS.querySelector('a');
  link.href = window.location.href.replace('http://', 'https://');
  requireHTTPS.classList.remove('hidden');
}
 */

// END Load Service Worker

// Start Share Buttons

var shareButtons = document.querySelectorAll(".sharebuttons a");

function trackShareButtonClick(event) {
    var shareButton = event.target.closest("a");
    var sharePlatform = shareButton.getAttribute("title");

    try {
    gtag("event", "share", {
        event_category: "social",
        event_label: sharePlatform,
        transport_type: "beacon",
    });
    } catch (error) {
    console.error("Error tracking share event:", error);
    }
}

for (var i = 0; i < shareButtons.length; i++) {
    shareButtons[i].addEventListener("click", trackShareButtonClick, {
    passive: true,
    });
}

// End Share Buttons

// Start Related Content

document.addEventListener('DOMContentLoaded', function() {
    var relatedLinks = document.querySelectorAll('.related-title a');
    for (var i = 0; i < relatedLinks.length; i++) {
      relatedLinks[i].addEventListener('click', function(event) {
        event.preventDefault();
        var linkUrl = this.href;
        try {
          gtag('event', 'click', {
            'event_category': 'Related Article',
            'event_label': linkUrl,
            'event_callback': function() {
              setTimeout(function() {
                window.location.href = linkUrl;
              }, 100);
            }
          });
        } catch (error) {
          console.error('Error sending gtag event:', error);
          setTimeout(function() {
            window.location.href = linkUrl;
          }, 100);
        }
      });
    }
  });

// END Related Content

// Start Google Adsense Lazy Load

const adPlaceholders = document.querySelectorAll(".ad-placeholder");
let enablePageLevelAds = false;
let adsLoadCounter = 0;

function loadAd(adPlaceholder) {
  const adClientId = adPlaceholder.getAttribute("data-ad-client");
  const randomInt = adPlaceholder.getAttribute("random-int");

  if (!adClientId || !randomInt) {
    console.error("Ad client ID or random-int attribute not found.");
    return;
  }

  const adsInPlaceholder = adPlaceholder.querySelectorAll("ins.adsbygoogle");
  if (adsInPlaceholder.length > 0) {
    console.warn("Ad already loaded in the ad placeholder.");
    return;
  }

  enablePageLevelAds = adsLoadCounter === 0;
  adsLoadCounter++;

  (adsbygoogle = window.adsbygoogle || []).push({
    google_ad_client: adClientId,
    ...(enablePageLevelAds ? { enable_page_level_ads: true } : {}),
    done_loading: function() {
      adPlaceholder.style.visibility = "visible";
    },
  });

  console.log("Ad loaded with random-int:", randomInt);
  console.log("Total ads loaded:", adsLoadCounter);
}

function checkIfAdShouldLoad(adPlaceholder) {
  const randomInt = adPlaceholder.getAttribute("random-int");
  const adLoaded = adPlaceholder.classList.contains("ad-loaded");

  if (
    randomInt &&
    !adLoaded &&
    window.innerHeight + window.scrollY >= document.body.offsetHeight
  ) {
    loadAd(adPlaceholder);
    adPlaceholder.classList.add("ad-loaded");
  }
}

function debounce(func, delay) {
  let timeoutId;

  return function() {
    clearTimeout(timeoutId);
    timeoutId = setTimeout(func, delay);
  };
}

function onPageLoad() {
  adPlaceholders.forEach(function(adPlaceholder) {
    lazyLoadAd(adPlaceholder);
  });
}

function lazyLoadAd(adPlaceholder) {
  const observerCallback = debounce(function(entries, observer) {
    entries.forEach(function(entry) {
      if (entry.isIntersecting && !adPlaceholder.classList.contains("ad-loaded")) {
        loadAd(adPlaceholder);
        adPlaceholder.classList.add("ad-loaded");
        observer.unobserve(entry.target);
      }
    });
  }, 200);

  const observer = new IntersectionObserver(observerCallback, {
    rootMargin: "200px",
    threshold: 0,
  });
  observer.observe(adPlaceholder);
}

window.addEventListener("load", onPageLoad, { passive: true });

// END Google Adsense Lazy Load