/**
 * sw-prefetch.js
 *
 * Two-mode link prefetcher that works in tandem with the service worker:
 *
 *  1. IDLE mode — after the page is fully loaded and the browser is idle,
 *     collect the first few same-origin page links from the document and
 *     ask the SW to cache them quietly in the background.
 *
 *  2. INTENT mode — when the user hovers over (or focuses on) any same-origin
 *     link, immediately ask the SW to pre-cache that page. This complements
 *     instantpage.js (which does the network-level prefetch) by ensuring the
 *     response also lands in the SW cache for instant repeat visits / offline.
 *
 * Both modes:
 *   - Respect navigator.connection.saveData — disabled on metered connections.
 *   - Only target same-origin HTML page links (not .css / .js / images /
 *     anchors / mailto / tel, etc.).
 *   - Deduplicate against a per-session seen-set to avoid repeat postMessages.
 *   - Silently bail if the service worker is not available or not yet active.
 */
(function () {
    'use strict';

    if (!('serviceWorker' in navigator)) return;

    // Respect data-saver mode
    if (navigator.connection && navigator.connection.saveData) return;

    // Extension patterns that should NOT be prefetched as pages
    var SKIP_EXTS = /\.(css|js|mjs|woff2?|ttf|otf|eot|webp|jpg|jpeg|png|gif|svg|ico|avif|pdf|xml|json|zip|gz|mp4|mp3|wav)(\?.*)?$/i;

    // Already-sent URLs this session
    var sent = new Set();

    function isSameOriginPage(href) {
        try {
            var url = new URL(href, location.href);
            if (url.origin !== location.origin) return false;
            if (url.hash && url.pathname === location.pathname) return false; // anchor on same page
            if (SKIP_EXTS.test(url.pathname)) return false;
            if (url.protocol !== 'https:' && url.protocol !== 'http:') return false;
            return true;
        } catch (e) { return false; }
    }

    function sendToPrefetch(urls) {
        if (!navigator.serviceWorker.controller) return;
        // De-duplicate against already-sent set
        var fresh = urls.filter(function (u) {
            if (sent.has(u)) return false;
            sent.add(u);
            return true;
        });
        if (fresh.length === 0) return;
        navigator.serviceWorker.controller.postMessage({
            type: 'PREFETCH_LINKS',
            urls: fresh,
        });
    }

    // ── IDLE MODE ─────────────────────────────────────────────────────────────
    // Collect the first N same-origin links visible in the document and send
    // them during the browser's first idle window after the load event.
    function idlePrefetch() {
        var LIMIT = 6;
        var anchors = document.querySelectorAll('main a[href], article a[href], nav a[href]');
        var urls = [];

        for (var i = 0; i < anchors.length && urls.length < LIMIT; i++) {
            var href = anchors[i].href;
            if (href && isSameOriginPage(href)) {
                urls.push(href);
            }
        }

        // Also grab a few from the rest of the document if we still have budget
        if (urls.length < LIMIT) {
            var all = document.querySelectorAll('a[href]');
            for (var j = 0; j < all.length && urls.length < LIMIT; j++) {
                var h = all[j].href;
                if (h && isSameOriginPage(h) && !urls.includes(h)) {
                    urls.push(h);
                }
            }
        }

        sendToPrefetch(urls);
    }

    // Schedule idle prefetch after the page settles
    function scheduleIdle() {
        if ('requestIdleCallback' in window) {
            requestIdleCallback(idlePrefetch, { timeout: 4000 });
        } else {
            setTimeout(idlePrefetch, 2500);
        }
    }

    if (document.readyState === 'complete') {
        scheduleIdle();
    } else {
        window.addEventListener('load', scheduleIdle, { once: true, passive: true });
    }

    // ── INTENT MODE ──────────────────────────────────────────────────────────
    // Prefetch a page the moment the user signals intent (hover / focus).
    // We debounce to avoid firing on quick mouse sweeps.
    var intentTimer = null;
    var lastIntentUrl = null;

    document.addEventListener('mouseover', function (e) {
        var a = e.target.closest('a[href]');
        if (!a) return;
        var url = a.href;
        if (!url || !isSameOriginPage(url)) return;
        if (url === lastIntentUrl) return;

        clearTimeout(intentTimer);
        lastIntentUrl = url;
        // 80 ms dwell before we consider it intentional
        intentTimer = setTimeout(function () {
            sendToPrefetch([url]);
        }, 80);
    }, { passive: true });

    // Also fire immediately on keyboard focus (zero debounce — user is tabbing)
    document.addEventListener('focusin', function (e) {
        if (e.target.tagName !== 'A') return;
        var url = e.target.href;
        if (!url || !isSameOriginPage(url)) return;
        sendToPrefetch([url]);
    }, { passive: true });

    // Cancel pending intent if the user moves away quickly
    document.addEventListener('mouseout', function (e) {
        var a = e.target.closest('a[href]');
        if (a && a.href === lastIntentUrl) {
            clearTimeout(intentTimer);
        }
    }, { passive: true });

})();
