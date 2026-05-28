---
name: checkout
description: "Erstelle einen kompletten Checkout-Flow (Stripe Payment Link + Success-Page + Tracking) für ein digitales Produkt. TRIGGER wenn the Owner sagt 'Checkout bauen', 'Stripe aufsetzen', 'Payment einrichten', oder '/checkout [Produkt]'."
allow_tools: Read, Write, Edit, Bash, Glob, Grep, Agent, TodoWrite, WebSearch, WebFetch, mcp__playwright__browser_navigate, mcp__playwright__browser_snapshot, mcp__playwright__browser_take_screenshot, mcp__playwright__browser_click, mcp__playwright__browser_resize
---

# Checkout Flow Builder — Stripe Payment Links + Success Page

Erstelle einen kompletten Checkout-Flow für ein digitales Produkt. Nutzt Stripe Payment Links (gehosteter Checkout von Stripe) + eigene Success-Page mit Tracking.

## Abgrenzung: Digital vs. Physical

| | Digital (Guide, Kurs, Template) | Physical (Box, Kit, Produkt) |
|---|---|---|
| **Checkout** | Stripe Payment Link (gehostet) | Shopify Checkout |
| **Delivery** | Success-Page Download + Email | Shopify Fulfillment |
| **Skill** | Dieser Skill | Shopify-Link in CTA, kein eigener Checkout |

**Dieser Skill ist für DIGITALE Produkte.** Für physische Produkte: CTA-Button → Shopify Checkout URL.

## Warum Payment Links statt Embedded Checkout

1. **Stripe's Checkout ist bereits conversion-optimiert** — besser als jede eigene Lösung
2. **Zero Maintenance** — Stripe updated Design, Zahlungsmethoden, Compliance automatisch
3. **Apple Pay, Google Pay, Link, Klarna** automatisch verfügbar (je nach Account-Region)
4. **Kein eigener Server nötig** für die Checkout-Session-Erstellung
5. **PCI-Compliance: Null Risiko** — wir berühren keine Kartendaten
6. **Mobile-optimiert** von Stripe out-of-the-box

## Input erwarten

### Pflicht-Inputs
- **PRODUKT**: Was wird verkauft? (z.B. "Krisenvorsorge Masterplan Guide")
- **PREIS**: Verkaufspreis in Euro (z.B. "29")
- **PROJEKT**: Projektordner (z.B. "3_archiv/eCommerce/survival-shop")
- **PRODUKTBILD**: Pfad zum Mockup/Produktbild (wird auf Stripe hochgeladen)
- **DOWNLOAD_URL**: URL zur digitalen Datei (kann Platzhalter sein)
- **BESCHREIBUNG**: Kurze Produktbeschreibung für Stripe (1-2 Sätze)

### Optionale Inputs
- **STRIPE_PRODUCT_ID**: Wenn bereits in Stripe angelegt
- **STRIPE_PRICE_ID**: Wenn bereits in Stripe angelegt
- **GARANTIE**: Garantie-Text (Default: "30 Tage Geld-zurück-Garantie")
- **BENEFITS**: Liste der Produkt-Benefits (für Success-Page)
- **FB_PIXEL_ID**: Facebook Pixel ID
- **GA4_ID**: Google Analytics 4 Measurement ID
- **SUPPORT_EMAIL**: Support-Kontakt (Default: support@domain.com)
- **SPRACHE**: Default: Deutsch

---

## STRIPE SETUP (via API — automatisch)

### Schritt 1: Produkt erstellen
```bash
curl -s -X POST "https://api.stripe.com/v1/products" \
  -u "$STRIPE_SECRET_KEY:" \
  -d "name=Krisenvorsorge Masterplan Guide" \
  -d "description=Dein kompletter Familien-Vorsorge-Guide — Schritt-für-Schritt Plan für 14 Tage Autarkie."
```

### Schritt 2: Preis erstellen
```bash
curl -s -X POST "https://api.stripe.com/v1/prices" \
  -u "$STRIPE_SECRET_KEY:" \
  -d "product=prod_xxx" \
  -d "unit_amount=2900" \
  -d "currency=eur"
```

### Schritt 3: Payment Link erstellen
```bash
curl -s -X POST "https://api.stripe.com/v1/payment_links" \
  -u "$STRIPE_SECRET_KEY:" \
  -d "line_items[0][price]=price_xxx" \
  -d "line_items[0][quantity]=1" \
  -d "after_completion[type]=redirect" \
  -d "after_completion[redirect][url]=https://NETLIFY_URL/success.html?session_id={CHECKOUT_SESSION_ID}"
```

### Schritt 4: Produktbild hochladen
Das Mockup-Bild muss als öffentlich erreichbare URL vorliegen. Workflow:
1. Success-Page + Images auf Netlify deployen (brauchen wir eh)
2. Öffentliche Bild-URL nutzen für Stripe Product Update:
```bash
curl -s -X POST "https://api.stripe.com/v1/products/prod_xxx" \
  -u "$STRIPE_SECRET_KEY:" \
  -d "images[0]=https://NETLIFY_URL/images/product-mockup.png"
```

### Ergebnis
- Payment Link URL (z.B. `https://buy.stripe.com/xxx`) → wird in alle CTA-Buttons eingesetzt
- Stripe hostet den kompletten Checkout (Formular, Zahlungsmethoden, Validierung)
- Nach Zahlung → Redirect auf unsere Success-Page

---

## SUCCESS-PAGE STRUKTUR

Die Success-Page ist das EINZIGE was wir selbst bauen. Alles andere macht Stripe.

```
┌─────────────────────────────────────────────┐
│              ✅ Zahlung erfolgreich!          │
│                                             │
│  Danke, [Name]! Dein [Produkt] ist bereit.  │
│                                             │
│  ┌─────────────────────────────────────┐    │
│  │  [Mockup]                          │    │
│  │  📥 JETZT HERUNTERLADEN            │    │
│  └─────────────────────────────────────┘    │
│                                             │
│  📧 Download-Link auch an [email] geschickt │
│                                             │
│  ─────────────────────────────────────────  │
│  Nächste Schritte:                          │
│  1. [Schritt 1]                             │
│  2. [Schritt 2]                             │
│  3. [Schritt 3]                             │
│  ─────────────────────────────────────────  │
│  Bei Fragen: support@domain.com             │
└─────────────────────────────────────────────┘
```

### Success-Page Features
- **Session-Verifizierung** via Netlify Function (session-status.js)
- **Personalisierung**: Kundenname + Email aus Stripe Session
- **Download-Button** mit Link zur digitalen Datei
- **Tracking Events**: FB Pixel Purchase + GA4 purchase
- **Nächste Schritte**: Produktspezifische Handlungsanweisungen
- **Support-Kontakt**

### Tracking auf Success-Page
```javascript
// FB Pixel Purchase Event
fbq('track', 'Purchase', {
    value: PREIS,
    currency: 'EUR',
    content_type: 'product',
    content_ids: ['PRODUKT_SLUG'],
    content_name: 'PRODUKT_NAME'
});

// GA4 Purchase Event
gtag('event', 'purchase', {
    transaction_id: sessionId,
    value: PREIS,
    currency: 'EUR',
    items: [{ item_name: 'PRODUKT_NAME', price: PREIS }]
});
```

---

## TECHNISCHE UMSETZUNG

### Dateistruktur
```
[projekt]/checkout/
├── success.html               ← Success-Page mit Download + Tracking
├── images/
│   └── product-mockup.png     ← Produktbild (auch auf Stripe hochgeladen)
├── netlify/
│   └── functions/
│       └── session-status.js  ← Prüft Stripe Session-Status
├── package.json               ← Stripe dependency
├── netlify.toml               ← Deploy + Functions Config
└── .env                       ← STRIPE_SECRET_KEY (Netlify Env Vars)
```

**WICHTIG:** Es gibt KEINE checkout.html. Stripe hostet den Checkout.

### Netlify Function: session-status.js
```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

exports.handler = async (event) => {
    const sessionId = event.queryStringParameters?.session_id;
    if (!sessionId) {
        return { statusCode: 400, body: 'Missing session_id' };
    }

    try {
        const session = await stripe.checkout.sessions.retrieve(sessionId);
        return {
            statusCode: 200,
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                status: session.status,
                customer_email: session.customer_details?.email,
                customer_name: session.customer_details?.name,
                amount_total: session.amount_total,
            }),
        };
    } catch (error) {
        return {
            statusCode: 500,
            body: JSON.stringify({ error: error.message }),
        };
    }
};
```

### netlify.toml
```toml
[build]
  functions = "netlify/functions"
  publish = "."

[dev]
  functions = "netlify/functions"
  publish = "."

[functions]
  node_bundler = "esbuild"
```

### Environment Variables
```
STRIPE_SECRET_KEY=sk_live_xxx   # Stripe Secret Key ([entity] LLC)
```

---

## ABLAUF (Step by Step)

### Step 1: Inputs sammeln
1. Produkt, Preis, Mockup-Pfad, Download-URL, Beschreibung
2. Tracking-IDs (FB Pixel, GA4) — optional, Platzhalter wenn nicht vorhanden
3. Support-Email, Garantie-Text, Benefits

### Step 2: Stripe API — Produkt + Preis + Payment Link
1. Produkt via API erstellen (oder bestehende ID nutzen)
2. Preis via API erstellen (oder bestehende ID nutzen)
3. Payment Link via API erstellen mit Redirect auf Success-Page
4. Payment Link URL speichern → wird in CTA-Buttons eingesetzt

### Step 3: Success-Page bauen
1. Clean Card-Layout mit Bestätigungs-Icon
2. Session-Verifizierung via Netlify Function
3. Personalisierung (Name, Email aus Stripe)
4. Download-Button
5. Tracking-Events (FB Pixel, GA4)
6. Nächste Schritte + Support-Kontakt
7. Responsive Design (Mobile + Desktop)

### Step 4: Netlify Functions
1. session-status.js (Stripe Session verifizieren)
2. package.json mit stripe dependency
3. netlify.toml

### Step 5: Deploy + Produktbild
1. `npm install` im checkout-Ordner
2. Netlify Site erstellen + deployen
3. Produktbild-URL auf Stripe Product aktualisieren (öffentliche Netlify-URL)
4. Payment Link Redirect-URL auf finale Netlify-URL setzen
5. .env / Netlify Env Vars setzen (STRIPE_SECRET_KEY)

### Step 6: CTA-Buttons verknüpfen
1. Alle Funnel-Pages (Listicle, Advertorial, Quiz) → CTA href = Payment Link URL
2. UTM-Parameter können an Payment Link URL angehängt werden

### Step 7: QA
1. Payment Link im Browser öffnen — Produktbild + Name + Preis korrekt?
2. Test-Zahlung durchführen (Stripe Test-Mode oder echte €1-Zahlung)
3. Success-Page prüfen: Name angezeigt? Download-Button? Tracking?
4. Mobile + Desktop testen
5. Playwright Screenshots

---

## STRIPE ACCOUNT & KEYS

### eCommerce-Projekte ([entity] LLC)
- **Account:** acct_1Qr0AUArvkmouSRc
- **Secret Key:** In Memory (reference_stripe_ecom.md)
- **Publishable Key:** In Memory (reference_stripe_ecom.md)
- **Für:** Survival-Shop, zukünftige Shops

### NICHT verwenden
- [brand]-Account (acct_51SR30lR0KOHbLsqW) → NUR für [brand]

### Zahlungsmethoden (US-Account)
- Kreditkarten (Visa, MC, Amex)
- Apple Pay + Google Pay (Wallets)
- Link (Stripe 1-Click)
- Klarna, Afterpay (BNPL)
- **KEIN PayPal** (nur für EU-Accounts verfügbar)

---

## QUALITÄTS-CHECK

### Stripe Setup
- [ ] Produkt in Stripe mit Name + Beschreibung + Bild?
- [ ] Preis korrekt (Betrag + Währung)?
- [ ] Payment Link erstellt mit korrekter Redirect-URL?
- [ ] Apple Pay / Google Pay aktiviert in Stripe Dashboard?

### Success-Page
- [ ] Session-Verifizierung funktioniert?
- [ ] Kundenname + Email angezeigt?
- [ ] Download-Button mit korrektem Link?
- [ ] FB Pixel Purchase Event feuert?
- [ ] GA4 purchase Event feuert?
- [ ] Email-Hinweis vorhanden?
- [ ] Nächste Schritte sinnvoll?
- [ ] Support-Kontakt vorhanden?
- [ ] Mobile-responsive?

### Integration
- [ ] CTA-Buttons in allen Funnel-Pages → Payment Link URL?
- [ ] Netlify Function deployed + erreichbar?
- [ ] STRIPE_SECRET_KEY als Netlify Env Var gesetzt?
- [ ] Produktbild auf Stripe sichtbar (im Payment Link Checkout)?

---

## WICHTIGE REGELN

1. **Payment Links, kein Embedded Checkout.** Stripe hostet den Checkout — wir bauen NUR die Success-Page.
2. **Keine Kartendaten berühren.** Alles auf Stripe's Domain. Null PCI-Risiko.
3. **Produktbild PFLICHT.** Ohne Bild sieht der Stripe Checkout "lieblos" aus. Immer Mockup hochladen.
4. **Tracking nur auf Success-Page.** Purchase-Event erst wenn bezahlt und redirected.
5. **Session verifizieren.** Nie blind "Danke" zeigen — immer via API prüfen dass bezahlt wurde.
6. **Stripe Branding optimieren.** Im Dashboard: Public Name + Logo setzen (gilt account-weit).
7. **Dateien via Bash schreiben** (nicht Write/Edit — VSCode Bug).
8. **Digital only.** Für physische Produkte: Shopify Checkout URL als CTA.
9. **Keys aus Memory laden.** reference_stripe_ecom.md für Primus/eCommerce Account.
10. **Deploy-Reihenfolge:** Netlify zuerst (für öffentliche Bild-URL) → dann Stripe Product Image updaten.

## LEARNINGS

1. **Stripe's eigener Checkout konvertiert besser** als jede selbstgebaute Lösung — optimiert für Mobile, Wallets, BNPL.
2. **Payment Links = Zero-Code Checkout.** Kein Server, kein iframe, keine Session-Erstellung nötig.
3. **Produktbild im Stripe Checkout** macht massiven Unterschied — ohne Bild wirkt es unprofessionell.
4. **PayPal nicht verfügbar** für US-Stripe-Accounts — nur EU/UK/CH.
5. **Branding (Name + Logo) gilt account-weit** — nicht pro Produkt änderbar. Neutralen Namen wählen.
6. **Success-Page auf separater Netlify-Site** deployen — unabhängig von Funnel-Pages.
7. **session_id wird als URL-Parameter** von Stripe an die Redirect-URL angehängt — {CHECKOUT_SESSION_ID} Platzhalter nutzen.
