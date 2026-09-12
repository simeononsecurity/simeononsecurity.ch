/**
 * sw-prefetch.js
 *
 * Two responsibilities:
 *
 *  A. LINK PREFETCHING — tells the service worker to proactively cache pages
 *     the user is likely to visit next.
 *
 *     1. IDLE mode   — requestIdleCallback collects first 6 same-origin links
 *                      after page load and sends them to the SW.
 *     2. INTENT mode — 80 ms debounced mouseover / immediate keyboard focus
 *                      sends that single URL to the SW.
 *
 *  B. UPDATE TOAST — listens for SW_UPDATED messages broadcast by the service
 *     worker on every upgrade activation and shows a non-intrusive "refresh"
 *     banner at the bottom of the screen.
 *
 * Safeguards:
 *   - Skips when navigator.connection.saveData is true (metered connections).
 *   - Deduplicates via a per-session Set (never sends the same URL twice).
 *   - Filters out all non-page URLs (assets, images, anchors, external, mailto…).
 *   - Gracefully bails when the SW is unavailable or not yet controlling.
 */
(function () {
    'use strict';

    if (!('serviceWorker' in navigator)) return;

    // ── A. LINK PREFETCHING ───────────────────────────────────────────────────

    // Respect data-saver / metered connections
    if (navigator.connection && navigator.connection.saveData) return;

    var SKIP_EXTS = /\.(css|js|mjs|woff2?|ttf|otf|eot|webp|jpg|jpeg|png|gif|svg|ico|avif|pdf|xml|json|zip|gz|mp4|mp3|wav)(\?.*)?$/i;
    var sent = new Set();

    function isSameOriginPage(href) {
        try {
            var url = new URL(href, location.href);
            if (url.origin !== location.origin) return false;
            if (url.hash && url.pathname === location.pathname) return false;
            if (SKIP_EXTS.test(url.pathname)) return false;
            if (url.protocol !== 'https:' && url.protocol !== 'http:') return false;
            return true;
        } catch (e) { return false; }
    }

    function sendToPrefetch(urls) {
        if (!navigator.serviceWorker.controller) return;
        var fresh = urls.filter(function (u) {
            if (sent.has(u)) return false;
            sent.add(u);
            return true;
        });
        if (!fresh.length) return;
        navigator.serviceWorker.controller.postMessage({
            type: 'PREFETCH_LINKS',
            urls: fresh,
        });
    }

    // Idle mode: prefetch first 6 navigation links after page load
    function idlePrefetch() {
        var LIMIT   = 6;
        var anchors = document.querySelectorAll('main a[href], article a[href], nav a[href]');
        var urls    = [];

        for (var i = 0; i < anchors.length && urls.length < LIMIT; i++) {
            if (anchors[i].href && isSameOriginPage(anchors[i].href)) {
                urls.push(anchors[i].href);
            }
        }
        if (urls.length < LIMIT) {
            var all = document.querySelectorAll('a[href]');
            for (var j = 0; j < all.length && urls.length < LIMIT; j++) {
                if (all[j].href && isSameOriginPage(all[j].href) && !urls.includes(all[j].href)) {
                    urls.push(all[j].href);
                }
            }
        }
        sendToPrefetch(urls);
    }

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

    // Intent mode: hover (80 ms debounce) + keyboard focus (immediate)
    var intentTimer   = null;
    var lastIntentUrl = null;

    document.addEventListener('mouseover', function (e) {
        var a = e.target.closest && e.target.closest('a[href]');
        if (!a || !isSameOriginPage(a.href)) return;
        if (a.href === lastIntentUrl) return;
        clearTimeout(intentTimer);
        lastIntentUrl = a.href;
        intentTimer   = setTimeout(function () { sendToPrefetch([a.href]); }, 80);
    }, { passive: true });

    document.addEventListener('focusin', function (e) {
        if (e.target.tagName !== 'A') return;
        if (e.target.href && isSameOriginPage(e.target.href)) {
            sendToPrefetch([e.target.href]);
        }
    }, { passive: true });

    document.addEventListener('mouseout', function (e) {
        var a = e.target.closest && e.target.closest('a[href]');
        if (a && a.href === lastIntentUrl) clearTimeout(intentTimer);
    }, { passive: true });

    // ── B. SW UPDATE TOAST ────────────────────────────────────────────────────

    navigator.serviceWorker.addEventListener('message', function (event) {
        if (!event.data || event.data.type !== 'SW_UPDATED') return;
        showUpdateToast();
    });

    function showUpdateToast() {
        // Don't create a second toast if already visible
        if (document.getElementById('sw-update-toast')) return;

        var toast = document.createElement('div');
        toast.id            = 'sw-update-toast';
        toast.role          = 'status';
        toast.setAttribute('aria-live', 'polite');

        // Inline styles — no dependency on external CSS
        Object.assign(toast.style, {
            position:     'fixed',
            bottom:       '1.25rem',
            right:        '1.25rem',
            display:      'flex',
            alignItems:   'center',
            gap:          '0.6rem',
            padding:      '0.65rem 1rem',
            background:   'var(--background-secondary, #1a1a2e)',
            color:        'var(--color, #e8e8e8)',
            border:       '1px solid var(--border-color, #444)',
            borderRadius: '8px',
            boxShadow:    '0 4px 16px rgba(0,0,0,0.4)',
            fontSize:     '0.875rem',
            zIndex:       '99999',
            maxWidth:     '320px',
            lineHeight:   '1.4',
        });

        // Shared button base style
        function makeBtn(text, title, primary) {
            var btn             = document.createElement('button');
            btn.textContent     = text;
            btn.title           = title;
            btn.setAttribute('type', 'button');
            Object.assign(btn.style, {
                cursor:       'pointer',
                border:       primary ? 'none' : '1px solid currentColor',
                borderRadius: '4px',
                padding:      primary ? '0.3rem 0.65rem' : '0.25rem 0.5rem',
                fontSize:     'inherit',
                fontWeight:   primary ? '600' : '400',
                background:   primary ? 'var(--color-secondary, #5b8af5)' : 'transparent',
                color:        primary ? '#fff' : 'inherit',
                flexShrink:   '0',
            });
            return btn;
        }

        var msg     = document.createElement('span');
        msg.textContent = '\u2728 Site updated!';

        var refreshBtn  = makeBtn('Refresh', 'Load the latest version', true);
        refreshBtn.addEventListener('click', function () { location.reload(); });

        var dismissBtn  = makeBtn('\u00D7', 'Dismiss', false);
        dismissBtn.setAttribute('aria-label', 'Dismiss update notification');
        dismissBtn.addEventListener('click', function () {
            if (toast.parentElement) toast.remove();
        });

        toast.appendChild(msg);
        toast.appendChild(refreshBtn);
        toast.appendChild(dismissBtn);

        // Wait for body to be ready (page may still be loading when SW activates)
        function appendToast() {
            document.body.appendChild(toast);
        }
        if (document.body) {
            appendToast();
        } else {
            document.addEventListener('DOMContentLoaded', appendToast, { once: true });
        }

        // Auto-dismiss after 20 seconds
        setTimeout(function () {
            if (toast.parentElement) toast.remove();
        }, 20000);
    }

})();
