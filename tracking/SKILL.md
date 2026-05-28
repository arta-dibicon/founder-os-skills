# Tracking Engine — Komplettes Conversion-Tracking für jede Landing Page

Implementiert Facebook Pixel, Conversions API (CAPI), GA4, Scroll-Tracking, Click-Tracking und Microsoft Clarity auf jeder Landing Page. Ein Skill, alle Daten.

---

## WARUM DIESER SKILL EXISTIERT

Ohne Tracking verbrennen wir Werbebudget blind. Meta braucht Conversion-Daten um den Algorithmus zu füttern. Wir brauchen Daten um zu wissen was funktioniert. Dieser Skill macht jede Landing Page messbar — bevor die erste Ad live geht.

**Reihenfolge:**
```
/ad-creative → /ad-copy → /tracking → /meta-ads
                              ↑
                     MUSS VOR ADS STEHEN
```

---

## WAS GETRACKT WIRD

### Event-Hierarchie (Funnel-Stufen)

| Event | Trigger | FB Pixel | GA4 | Wann |
|---|---|---|---|---|
| **PageView** | Seite geladen | ✅ auto | ✅ auto | Immer |
| **ViewContent** | Seite geladen (mit Content-Typ) | ✅ | ✅ | Listicle/Advertorial/Quiz |
| **ScrollDepth** | 25%, 50%, 75%, 100% | ✅ custom | ✅ | Scroll-Meilensteine |
| **CtaClick** | CTA-Button geklickt | ✅ custom | ✅ | Jeder CTA |
| **Lead** | Quiz abgeschlossen / Email eingetragen | ✅ | ✅ | Quiz/Lead-Form |
| **InitiateCheckout** | Checkout-Link geklickt | ✅ | ✅ | Checkout-Übergang |
| **Purchase** | Kauf abgeschlossen | ✅ + CAPI | ✅ | Success-Page |

### Zusätzliche Metriken

| Metrik | Methode | Zweck |
|---|---|---|
| **Time on Page** | JS Timer | Engagement-Qualität |
| **Bounce Rate** | Scroll < 25% + < 10s | Content-Qualität |
| **CTA-Sichtbarkeit** | IntersectionObserver | Wird der CTA überhaupt gesehen? |
| **Outbound Clicks** | Link-Tracking | Wohin verlassen User die Seite? |
| **UTM-Parameter** | URL-Parsing | Welche Ad/Kampagne bringt Traffic? |
| **Heatmaps** | Microsoft Clarity | Visuelles Verhaltensmuster |
| **Session Recordings** | Microsoft Clarity | Einzelne User-Journeys |

---

## INPUT ERWARTEN

### Pflicht-Inputs
- **PROJEKT**: Projektordner
- **PAGE_PATH**: Pfad zur HTML-Datei die getrackt werden soll
- **PAGE_TYPE**: listicle / advertorial / quiz / checkout / success
- **FB_PIXEL_ID**: Facebook Pixel ID

### Optionale Inputs
- **GA4_MEASUREMENT_ID**: GA4 Measurement ID (G-XXXXXXXXXX). Wenn nicht vorhanden → nur FB Pixel.
- **CLARITY_PROJECT_ID**: Microsoft Clarity ID. Wenn nicht vorhanden → wird angelegt.
- **CURRENCY**: Währung für Purchase-Events (Default: EUR)
- **PRODUCT_VALUE**: Produktpreis für Purchase-Event (Default: aus Checkout ableiten)
- **CUSTOM_EVENTS**: Zusätzliche Events (Array von {name, trigger, selector})

---

## TRACKING-ARCHITEKTUR

### Prinzip: Ein Script, modularer Aufbau

```
tracking.js (Haupt-Script)
├── Module: FB Pixel (fbq)
├── Module: GA4 (gtag)
├── Module: Clarity
├── Module: Scroll-Tracker
├── Module: Click-Tracker
├── Module: UTM-Parser
└── Module: Event-Bus (verbindet alles)
```

### Event-Bus Pattern
Jedes Tracking-Event wird EINMAL gefeuert und an alle aktiven Module weitergeleitet:

```javascript
// Statt:
fbq('track', 'ViewContent', {...});
gtag('event', 'view_content', {...});

// Event-Bus:
trackEvent('ViewContent', {content_type: 'listicle', ...});
// → Bus verteilt automatisch an FB + GA4 + Custom
```

---

## IMPLEMENTIERUNG

### tracking.js — Das Haupt-Script

```javascript
(function() {
  'use strict';

  // ============================================
  // CONFIG — wird pro Page angepasst
  // ============================================
  const CONFIG = {
    fbPixelId: '%%FB_PIXEL_ID%%',
    ga4Id: '%%GA4_ID%%',
    clarityId: '%%CLARITY_ID%%',
    pageType: '%%PAGE_TYPE%%',        // listicle|advertorial|quiz|checkout|success
    productValue: %%PRODUCT_VALUE%%,  // z.B. 29
    currency: '%%CURRENCY%%',        // EUR|USD
    debug: false                      // true = console.log alle Events
  };

  // ============================================
  // UTM PARSER
  // ============================================
  const UTM = (function() {
    const params = new URLSearchParams(window.location.search);
    const data = {
      source: params.get('utm_source') || '(direct)',
      medium: params.get('utm_medium') || '(none)',
      campaign: params.get('utm_campaign') || '(not set)',
      content: params.get('utm_content') || '(not set)',
      term: params.get('utm_term') || '(not set)',
      fbclid: params.get('fbclid') || null,
      gclid: params.get('gclid') || null
    };
    // Persist in sessionStorage for cross-page tracking
    if (params.has('utm_source')) {
      sessionStorage.setItem('utm_data', JSON.stringify(data));
    }
    return JSON.parse(sessionStorage.getItem('utm_data') || JSON.stringify(data));
  })();

  // ============================================
  // FACEBOOK PIXEL
  // ============================================
  const FB = (function() {
    if (!CONFIG.fbPixelId) return { track: function(){} };

    // Pixel Base Code
    !function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){
    n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};
    if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
    n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;
    s=b.getElementsByTagName(e)[0];s.parentNode.insertBefore(t,s)}(
    window,document,'script','https://connect.facebook.net/en_US/fbevents.js');

    fbq('init', CONFIG.fbPixelId);
    fbq('track', 'PageView');

    return {
      track: function(event, params) {
        if (typeof fbq !== 'undefined') {
          fbq('track', event, params || {});
        }
      },
      trackCustom: function(event, params) {
        if (typeof fbq !== 'undefined') {
          fbq('trackCustom', event, params || {});
        }
      }
    };
  })();

  // ============================================
  // GA4
  // ============================================
  const GA = (function() {
    if (!CONFIG.ga4Id) return { track: function(){} };

    // gtag Base Code
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + CONFIG.ga4Id;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', CONFIG.ga4Id, { send_page_view: true });

    return {
      track: function(event, params) {
        gtag('event', event, params || {});
      }
    };
  })();

  // ============================================
  // MICROSOFT CLARITY
  // ============================================
  (function() {
    if (!CONFIG.clarityId) return;
    (function(c,l,a,r,i,t,y){c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
    t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
    y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window,document,"clarity","script",CONFIG.clarityId);
  })();

  // ============================================
  // EVENT BUS — Zentraler Event-Verteiler
  // ============================================
  function trackEvent(eventName, data) {
    data = data || {};
    data.page_type = CONFIG.pageType;
    data.utm_source = UTM.source;
    data.utm_medium = UTM.medium;
    data.utm_campaign = UTM.campaign;
    data.utm_content = UTM.content;

    // FB Pixel Mapping
    var fbEventMap = {
      'ViewContent': 'ViewContent',
      'CtaClick': 'Lead',
      'ScrollDepth': null,  // Custom Event
      'InitiateCheckout': 'InitiateCheckout',
      'Purchase': 'Purchase',
      'Lead': 'Lead',
      'TimeOnPage': null
    };

    var fbEvent = fbEventMap[eventName];
    if (fbEvent) {
      FB.track(fbEvent, data);
    } else if (eventName === 'ScrollDepth') {
      FB.trackCustom('ScrollDepth', data);
    }

    // GA4 Mapping (snake_case)
    var ga4EventMap = {
      'ViewContent': 'view_content',
      'CtaClick': 'cta_click',
      'ScrollDepth': 'scroll_depth',
      'InitiateCheckout': 'begin_checkout',
      'Purchase': 'purchase',
      'Lead': 'generate_lead',
      'TimeOnPage': 'time_on_page'
    };

    var ga4Event = ga4EventMap[eventName] || eventName.toLowerCase();
    GA.track(ga4Event, data);

    // Debug
    if (CONFIG.debug) {
      console.log('[TRACK]', eventName, data);
    }
  }

  // ============================================
  // SCROLL TRACKING
  // ============================================
  (function() {
    var milestones = [25, 50, 75, 100];
    var reached = {};

    function getScrollPercent() {
      var h = document.documentElement;
      var b = document.body;
      var st = window.pageYOffset || h.scrollTop || b.scrollTop || 0;
      var sh = Math.max(h.scrollHeight, b.scrollHeight) - Math.max(h.clientHeight, b.clientHeight);
      return sh > 0 ? Math.round((st / sh) * 100) : 0;
    }

    var scrollTimer;
    window.addEventListener('scroll', function() {
      clearTimeout(scrollTimer);
      scrollTimer = setTimeout(function() {
        var pct = getScrollPercent();
        milestones.forEach(function(m) {
          if (pct >= m && !reached[m]) {
            reached[m] = true;
            trackEvent('ScrollDepth', {
              depth: m,
              depth_label: m + '%'
            });
          }
        });
      }, 150);
    }, { passive: true });
  })();

  // ============================================
  // TIME ON PAGE
  // ============================================
  (function() {
    var startTime = Date.now();
    var intervals = [10, 30, 60, 120, 300]; // Sekunden
    var fired = {};

    setInterval(function() {
      var elapsed = Math.floor((Date.now() - startTime) / 1000);
      intervals.forEach(function(s) {
        if (elapsed >= s && !fired[s]) {
          fired[s] = true;
          trackEvent('TimeOnPage', {
            seconds: s,
            time_label: s + 's'
          });
        }
      });
    }, 5000);
  })();

  // ============================================
  // CTA CLICK TRACKING
  // ============================================
  (function() {
    // Track all CTA clicks (buttons + links with specific classes/attributes)
    document.addEventListener('click', function(e) {
      var el = e.target.closest('a[href], button, [data-track-cta]');
      if (!el) return;

      var isCta = el.classList.contains('cta') ||
                  el.classList.contains('cta-button') ||
                  el.classList.contains('btn-primary') ||
                  el.classList.contains('checkout-btn') ||
                  el.hasAttribute('data-track-cta') ||
                  (el.tagName === 'A' && el.href && el.href.includes('stripe.com')) ||
                  (el.tagName === 'A' && el.href && el.href.includes('checkout')) ||
                  (el.tagName === 'A' && el.href && el.href.includes('buy.stripe.com'));

      if (!isCta) return;

      var href = el.href || el.getAttribute('data-href') || '';
      var text = (el.textContent || '').trim().substring(0, 50);
      var ctaId = el.getAttribute('data-track-cta') || el.id || '';

      // Determine event type
      var isCheckout = href.includes('stripe.com') || href.includes('checkout') || href.includes('buy.stripe.com');

      trackEvent(isCheckout ? 'InitiateCheckout' : 'CtaClick', {
        cta_text: text,
        cta_id: ctaId,
        cta_url: href,
        content_name: document.title,
        value: isCheckout ? CONFIG.productValue : undefined,
        currency: isCheckout ? CONFIG.currency : undefined
      });
    });
  })();

  // ============================================
  // CTA VISIBILITY TRACKING
  // ============================================
  (function() {
    if (!('IntersectionObserver' in window)) return;

    var observer = new IntersectionObserver(function(entries) {
      entries.forEach(function(entry) {
        if (entry.isIntersecting) {
          var el = entry.target;
          var ctaId = el.getAttribute('data-track-cta') || el.id || el.textContent.trim().substring(0, 30);
          trackEvent('CtaVisible', {
            cta_id: ctaId,
            cta_text: (el.textContent || '').trim().substring(0, 50)
          });
          observer.unobserve(el); // Nur einmal pro Element
        }
      });
    }, { threshold: 0.5 });

    // Observe all CTAs
    setTimeout(function() {
      var ctas = document.querySelectorAll('a.cta, a.cta-button, .btn-primary, .checkout-btn, [data-track-cta], a[href*="stripe.com"], a[href*="buy.stripe.com"]');
      ctas.forEach(function(cta) { observer.observe(cta); });
    }, 1000);
  })();

  // ============================================
  // PAGE-TYPE SPECIFIC EVENTS
  // ============================================
  (function() {
    // ViewContent — auf allen Funnel-Pages
    if (['listicle', 'advertorial', 'quiz'].includes(CONFIG.pageType)) {
      trackEvent('ViewContent', {
        content_type: CONFIG.pageType,
        content_name: document.title,
        value: CONFIG.productValue,
        currency: CONFIG.currency
      });
    }

    // Purchase — auf Success-Page
    if (CONFIG.pageType === 'success') {
      trackEvent('Purchase', {
        value: CONFIG.productValue,
        currency: CONFIG.currency,
        content_type: 'product',
        content_name: document.title
      });
    }
  })();

  // ============================================
  // OUTBOUND LINK TRACKING
  // ============================================
  (function() {
    document.addEventListener('click', function(e) {
      var link = e.target.closest('a[href]');
      if (!link) return;
      var href = link.href;
      if (!href || href.startsWith('#') || href.startsWith('javascript:')) return;

      try {
        var url = new URL(href);
        if (url.hostname !== window.location.hostname) {
          GA.track('outbound_click', {
            link_url: href,
            link_text: (link.textContent || '').trim().substring(0, 50)
          });
        }
      } catch(e) {}
    });
  })();

})();
```

---

## ABLAUF (Step by Step)

### Step 0: Inputs klären
1. Welche Seite? (Pfad zur HTML)
2. Welcher Page-Type? (listicle/advertorial/quiz/checkout/success)
3. FB Pixel ID vorhanden? → Wenn nicht: neuen Pixel erstellen lassen oder bestehenden nutzen
4. GA4 ID vorhanden? → Optional, aber empfohlen
5. Clarity ID vorhanden? → Wenn nicht: wird übersprungen (kostenlos anlegbar auf clarity.microsoft.com)

### Step 1: tracking.js generieren
1. Template oben nehmen
2. Platzhalter ersetzen:
   - `%%FB_PIXEL_ID%%` → echte Pixel ID
   - `%%GA4_ID%%` → GA4 Measurement ID (oder '' wenn nicht vorhanden)
   - `%%CLARITY_ID%%` → Clarity ID (oder '' wenn nicht vorhanden)
   - `%%PAGE_TYPE%%` → listicle/advertorial/quiz/checkout/success
   - `%%PRODUCT_VALUE%%` → Produktpreis (z.B. 29)
   - `%%CURRENCY%%` → EUR/USD
3. Speichern als `[projekt]/tracking/tracking.js`

### Step 2: Script in HTML einbinden
1. HTML-Datei lesen
2. Vor `</head>` einfügen:
   ```html
   <!-- Facebook Pixel NoScript Fallback -->
   <noscript><img height="1" width="1" style="display:none"
   src="https://www.facebook.com/tr?id=%%FB_PIXEL_ID%%&ev=PageView&noscript=1"/></noscript>
   ```
3. Vor `</body>` einfügen:
   ```html
   <!-- Tracking Engine -->
   <script src="tracking.js"></script>
   ```
   ODER: Script inline einbetten (besser für Netlify single-file deploys):
   ```html
   <script>
   [kompletter tracking.js Inhalt]
   </script>
   ```
4. **Inline bevorzugen** — kein extra HTTP-Request, sofort geladen

### Step 3: CTA-Elemente taggen
1. Alle CTA-Buttons/Links in der HTML identifizieren
2. `data-track-cta="cta-name"` Attribut hinzufügen wo noch nicht vorhanden
3. Sicherstellen dass CTAs eine der erkannten Klassen haben:
   - `.cta`, `.cta-button`, `.btn-primary`, `.checkout-btn`
   - ODER `data-track-cta` Attribut
   - ODER `href` enthält `stripe.com` / `buy.stripe.com`

### Step 4: Success-Page konfigurieren
1. Success-Page HTML laden
2. `pageType: 'success'` setzen → feuert automatisch Purchase-Event
3. **Produktwert** im Purchase-Event = echter Preis
4. Falls Stripe Webhook vorhanden → serverseitiges Purchase-Event via CAPI (optional, Advanced)

### Step 5: Verifizierung
1. **Facebook Pixel Helper** — Chrome Extension prüfen (oder via API):
   ```bash
   curl -s "https://graph.facebook.com/v22.0/[PIXEL_ID]?fields=name,is_active,last_fired_time&access_token=$TOKEN"
   ```
2. **Playwright-Test:**
   - Seite laden
   - Scrollen (25%, 50%, 75%, 100%)
   - CTA klicken
   - Console-Logs prüfen (debug: true)
   - Network-Requests prüfen (facebook.com/tr, google-analytics.com)
3. **Events verifizieren:**
   - FB: Events Manager → Test Events
   - GA4: Realtime Report
   - Clarity: Dashboard

### Step 6: Deploy
1. Geänderte HTML auf Netlify deployen
2. Tracking-Datei im Projekt speichern
3. **QA nach Deploy:** Playwright-Test auf Live-URL wiederholen

---

## CONVERSIONS API (CAPI) — Server-Side Events

### Warum CAPI?
- iOS 14.5+ blockiert Browser-Pixel bei ~40% der User
- CAPI sendet Events server-side → umgeht Ad Blocker + iOS Tracking Prevention
- Meta empfiehlt "Dual Tracking": Browser-Pixel + CAPI parallel
- Bessere Event-Match-Rate = bessere Ad-Optimierung

### CAPI via Netlify Functions

Für Purchase-Events (wichtigstes Event für ROAS-Tracking):

```javascript
// netlify/functions/track-purchase.js
const https = require('https');

exports.handler = async (event) => {
  const body = JSON.parse(event.body);
  const pixelId = process.env.FB_PIXEL_ID;
  const accessToken = process.env.META_ACCESS_TOKEN;

  const eventData = {
    data: [{
      event_name: 'Purchase',
      event_time: Math.floor(Date.now() / 1000),
      event_source_url: body.source_url,
      action_source: 'website',
      user_data: {
        client_ip_address: event.headers['x-forwarded-for'] || event.headers['client-ip'],
        client_user_agent: event.headers['user-agent'],
        fbc: body.fbc || null,  // Facebook Click ID (aus Cookie)
        fbp: body.fbp || null   // Facebook Browser ID (aus Cookie)
      },
      custom_data: {
        value: body.value,
        currency: body.currency || 'EUR',
        content_type: 'product',
        content_name: body.product_name
      }
    }]
  };

  const response = await fetch(
    `https://graph.facebook.com/v22.0/${pixelId}/events?access_token=${accessToken}`,
    {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(eventData)
    }
  );

  const result = await response.json();

  return {
    statusCode: 200,
    body: JSON.stringify(result)
  };
};
```

### CAPI in tracking.js integrieren (Client-Side Trigger)

```javascript
// Im Purchase-Block:
if (CONFIG.pageType === 'success' && CONFIG.capiEndpoint) {
  fetch(CONFIG.capiEndpoint, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      value: CONFIG.productValue,
      currency: CONFIG.currency,
      product_name: document.title,
      source_url: window.location.href,
      fbc: getCookie('_fbc'),
      fbp: getCookie('_fbp')
    })
  }).catch(function() {});
}
```

**CAPI ist optional für V1.** Browser-Pixel reicht zum Starten. CAPI als Upgrade wenn die ersten Kampagnen laufen.

---

## OUTPUT-STRUKTUR

```
[projekt]/tracking/
├── tracking.js              ← Haupt-Script (Template, Platzhalter ersetzt)
├── tracking-config.json     ← Konfiguration für alle Pages
└── capi/                    ← Server-Side Functions (optional)
    └── track-purchase.js
```

### tracking-config.json

```json
{
  "fb_pixel_id": "[ID]",
  "ga4_id": "[ID oder null]",
  "clarity_id": "[ID oder null]",
  "currency": "EUR",
  "pages": [
    {
      "path": "listicle/krisenvorsorge-masterplan.html",
      "type": "listicle",
      "product_value": 29,
      "tracking_implemented": true,
      "deployed_url": "https://krisenvorsorge-listicle.netlify.app/krisenvorsorge-masterplan.html"
    },
    {
      "path": "advertorial/krisenvorsorge-masterplan.html",
      "type": "advertorial",
      "product_value": 29,
      "tracking_implemented": false
    },
    {
      "path": "checkout/success.html",
      "type": "success",
      "product_value": 29,
      "tracking_implemented": false
    }
  ]
}
```

---

## REGELN

1. **Tracking VOR Ads** — Nie eine Kampagne starten ohne funktionierendes Tracking
2. **FB Pixel ist Pflicht** — ohne Pixel keine Conversion-Optimierung bei Meta
3. **Inline-Script bevorzugen** — kein extra HTTP-Request, sofort geladen
4. **CAPI optional für V1** — Browser-Pixel reicht zum Start
5. **Keine PII (Personally Identifiable Information)** in Custom Events — DSGVO
6. **Cookie-Banner** — wenn nötig, Tracking erst NACH Consent laden. Für DE-Traffic IMMER prüfen ob nötig.
7. **Debug-Modus** — `debug: true` beim Testen, `debug: false` für Production
8. **UTM-Parameter** — werden in sessionStorage persistiert für Cross-Page-Tracking
9. **Purchase-Event NUR auf Success-Page** — nie auf Checkout-Page (Double-Counting!)
10. **Scroll-Tracking mit Throttle** — nicht bei jedem Pixel feuern, 150ms Debounce
11. **QA nach jedem Deploy** — Playwright-Test auf Live-URL
12. **tracking-config.json pflegen** — zentrale Übersicht welche Pages getrackt werden
