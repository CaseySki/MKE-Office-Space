/* ── Site Configuration ──
 * Edit these values to brand the site for a new client.
 * This is the ONLY file you need to change for basic setup.
 */
const SITE_CONFIG = {

  // ── Company Info ──
  COMPANY_NAME: "Your Company Name",
  COMPANY_TAGLINE: "Your Tagline Here",
  COMPANY_WEBSITE: "https://yourcompany.com",

  // ── Brand Color ──
  // Main accent color used for buttons, links, badges, hover states
  BRAND_COLOR: "#CF152D",
  BRAND_COLOR_DARK: "#a8112a",

  // ── Google Sheet ──
  // Paste the full URL or just the ID from your Google Sheet.
  // The sheet must have three tabs: Buildings, Suites, Contacts
  // Leave blank to use local JSON files in data/ folder.
  GOOGLE_SHEET_ID: "",

  // ── Google Analytics ──
  // Your GA4 Measurement ID (e.g. "G-XXXXXXXXXX"). Leave blank to disable.
  GA_MEASUREMENT_ID: "",

  // ── Inquiry Form ──
  // Comma-separated email addresses that receive form submissions
  INQUIRY_EMAILS: "broker@yourcompany.com",
  INQUIRY_SUBJECT_PREFIX: "Space Inquiry",

  // ── Listing Type Labels ──
  // Customize the text shown on badges and headers
  LEASE_LABEL: "For Lease",
  SALE_LABEL: "For Sale",

  // ── Meta / SEO ──
  SITE_TITLE: "Available Office Space",
  SITE_DESCRIPTION: "Commercial office space available for lease.",
  SITE_URL: "",  // e.g. "https://yourcompany.github.io/office-space/"

  // ── Display Settings ──
  SHOW_LEASED: true,     // Show leased suites in Browse All Suites
  SUITES_PER_PAGE: 10,   // Pagination size for Browse All Suites
  MAX_RECENT_VIEWS: 4,   // Number of recently viewed buildings to remember
};
