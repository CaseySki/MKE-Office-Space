# Commercial Office Space Website — Template

A ready-to-deploy website for commercial real estate brokerages. Mobile-first, data-driven, no build tools required.

## Features

- Interactive map with numbered pins (Leaflet.js)
- Building detail pages with suite cards, floor plans, brochures
- "Find Your Space" matching tool
- Suite comparison side-by-side
- Favorites and recently viewed
- Dark mode
- Contact form (mailto-based, no server needed)
- Google Analytics integration
- Google Sheets as live data source (or local JSON fallback)
- Mobile-optimized (QR code friendly)
- GitHub Pages deployment with one-click CI/CD

## Quick Start

### 1. Clone this template

```bash
git clone <this-repo> my-client-site
cd my-client-site
```

### 2. Run the setup script

```bash
python3 setup.py
```

It will ask for:
- Company name and tagline
- Brand color (hex code)
- Google Sheet ID (optional)
- Broker email addresses
- Google Analytics ID (optional)

### 3. Add your assets

| File | Purpose |
|------|---------|
| `site/images/logos/logo-white.svg` | Header & loading screen logo (white version) |
| `site/images/logos/favicon.svg` | Browser tab icon |
| `site/images/logos/favicon.png` | Fallback favicon (64x64) |
| `site/images/og-image.jpg` | Social sharing preview (1200x630) |
| `site/images/*.jpg` | Building photos |

### 4. Add your data

**Option A: Google Sheets (recommended)**

Create a Google Sheet with three tabs:

**Buildings tab columns:**
`building_id`, `building_name`, `address`, `city`, `state`, `zip`, `latitude`, `longitude`, `description`, `photo_filename`, `listing_type`, `asking_price`, `sort_order`, `map_group`, `broker`

**Suites tab columns:**
`suite_id`, `building_id`, `suite_number`, `floor`, `square_feet`, `lease_rate`, `rate_unit`, `lease_type`, `status`, `available_date`, `notes`, `floor_plan_filename`, `brochure_filename`, `photos`

**Contacts tab columns:**
`name`, `title`, `phone`, `email`, `photo_filename`

**Option B: Local JSON files**

Edit the files in `site/data/` directly.

### 5. Test locally

```bash
cd site && python3 -m http.server 8000
```

Open http://localhost:8000

### 6. Deploy

Push to GitHub, go to Settings > Pages, and enable GitHub Pages from the `main` branch. The included GitHub Actions workflow deploys automatically on every push.

## Configuration

All settings are in one file: `site/js/config.js`

| Setting | Description |
|---------|-------------|
| `COMPANY_NAME` | Shown in titles, share text, footer |
| `BRAND_COLOR` | Accent color for buttons, badges, hover states |
| `GOOGLE_SHEET_ID` | Live data source (leave blank for local JSON) |
| `GA_MEASUREMENT_ID` | Google Analytics tracking |
| `INQUIRY_EMAILS` | Where contact form submissions go |
| `SHOW_LEASED` | Show/hide leased suites |
| `SUITES_PER_PAGE` | Pagination size |

## File Structure

```
site/
├── index.html          # Home page with map
├── building.html       # Building detail page
├── find-space.html     # Space finder tool
├── css/style.css       # All styles
├── js/
│   ├── config.js       # ← Edit this file
│   └── app.js          # Site logic (don't edit)
├── data/               # Fallback JSON data
│   ├── buildings.json
│   ├── suites.json
│   └── contacts.json
└── images/
    └── logos/           # Your logo files
```

## Custom Domain

To use a custom domain (e.g. `listings.yourcompany.com`):

1. In your DNS provider, add a CNAME record pointing to `yourusername.github.io`
2. In GitHub repo Settings > Pages, enter your custom domain
3. GitHub will automatically provision an SSL certificate
