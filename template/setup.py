#!/usr/bin/env python3
"""
Office Space Website — Quick Setup
Configures the template for a new client in under a minute.

Usage:
    python3 setup.py

It will prompt for company details and update all files automatically.
"""

import os
import re
import json

TEMPLATE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DIR = os.path.join(TEMPLATE_DIR, "site")
CONFIG_PATH = os.path.join(SITE_DIR, "js", "config.js")

HTML_FILES = [
    os.path.join(SITE_DIR, "index.html"),
    os.path.join(SITE_DIR, "building.html"),
    os.path.join(SITE_DIR, "find-space.html"),
]

def prompt(label, default=""):
    suffix = f" [{default}]" if default else ""
    val = input(f"  {label}{suffix}: ").strip()
    return val or default

def main():
    print()
    print("=" * 50)
    print("  Office Space Website — Setup")
    print("=" * 50)
    print()
    print("Answer the prompts below. Press Enter to keep defaults.")
    print()

    print("── Company Info ──")
    company = prompt("Company name", "Acme Realty")
    tagline = prompt("Tagline / slogan", "Your Space, Our Priority")
    website = prompt("Company website URL", "https://example.com")

    print()
    print("── Brand Color ──")
    print("  Enter a hex color code for the accent color.")
    print("  Examples: #CF152D (red), #1e40af (blue), #059669 (green)")
    color = prompt("Brand color", "#CF152D")
    color_dark = color  # We'll darken it automatically
    # Simple darkening: reduce each hex component by ~20%
    try:
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        color_dark = f"#{max(0,int(r*0.8)):02x}{max(0,int(g*0.8)):02x}{max(0,int(b*0.8)):02x}"
    except (ValueError, IndexError):
        color_dark = color

    print()
    print("── Data Source ──")
    print("  Your Google Sheet must have 3 tabs: Buildings, Suites, Contacts")
    print("  Leave blank to use local JSON files in data/ folder.")
    sheet_id = prompt("Google Sheet ID or URL", "")

    print()
    print("── Contact Emails ──")
    emails = prompt("Inquiry email(s), comma-separated", "broker@example.com")

    print()
    print("── Google Analytics ──")
    ga_id = prompt("GA4 Measurement ID (e.g. G-XXXXXXXXXX)", "")

    print()
    print("── Site URL ──")
    site_url = prompt("Live site URL (for social sharing)", "")
    if site_url and not site_url.endswith("/"):
        site_url += "/"

    # ── Update config.js ──
    config_content = f'''/* ── Site Configuration ──
 * Edit these values to brand the site for a new client.
 * This is the ONLY file you need to change for basic setup.
 */
const SITE_CONFIG = {{

  // ── Company Info ──
  COMPANY_NAME: "{company}",
  COMPANY_TAGLINE: "{tagline}",
  COMPANY_WEBSITE: "{website}",

  // ── Brand Color ──
  BRAND_COLOR: "{color}",
  BRAND_COLOR_DARK: "{color_dark}",

  // ── Google Sheet ──
  GOOGLE_SHEET_ID: "{sheet_id}",

  // ── Google Analytics ──
  GA_MEASUREMENT_ID: "{ga_id}",

  // ── Inquiry Form ──
  INQUIRY_EMAILS: "{emails}",
  INQUIRY_SUBJECT_PREFIX: "Space Inquiry",

  // ── Listing Type Labels ──
  LEASE_LABEL: "For Lease",
  SALE_LABEL: "For Sale",

  // ── Meta / SEO ──
  SITE_TITLE: "Available Office Space",
  SITE_DESCRIPTION: "Commercial office space available for lease.",
  SITE_URL: "{site_url}",

  // ── Display Settings ──
  SHOW_LEASED: true,
  SUITES_PER_PAGE: 10,
  MAX_RECENT_VIEWS: 4,
}};
'''
    with open(CONFIG_PATH, "w") as f:
        f.write(config_content)
    print(f"  ✓ Updated config.js")

    # ── Update HTML files ──
    for html_path in HTML_FILES:
        with open(html_path, "r") as f:
            content = f.read()
        content = content.replace("__COMPANY_NAME__", company)
        content = content.replace("__COMPANY_TAGLINE__", tagline)
        content = content.replace("__SITE_URL__", site_url)
        with open(html_path, "w") as f:
            f.write(content)
        print(f"  ✓ Updated {os.path.basename(html_path)}")

    # ── Update CSS brand color ──
    css_path = os.path.join(SITE_DIR, "css", "style.css")
    with open(css_path, "r") as f:
        css = f.read()
    css = css.replace("#CF152D", color, 1)  # --red
    css = css.replace("#a8112a", color_dark, 1)  # --red-dark
    with open(css_path, "w") as f:
        f.write(css)
    print(f"  ✓ Updated brand color in style.css")

    print()
    print("=" * 50)
    print("  Setup complete!")
    print("=" * 50)
    print()
    print("Next steps:")
    print(f"  1. Add your logo files to site/images/logos/")
    print(f"     - logo-white.svg  (white version for dark header)")
    print(f"     - favicon.svg     (browser tab icon)")
    print(f"     - favicon.png     (fallback favicon, 64x64)")
    print(f"  2. Add building photos to site/images/")
    print(f"  3. Add your OG image to site/images/og-image.jpg (1200x630)")
    if sheet_id:
        print(f"  4. Populate your Google Sheet with building data")
    else:
        print(f"  4. Edit the JSON files in site/data/ with your listings")
    print(f"  5. Test locally: cd site && python3 -m http.server 8000")
    print(f"  6. Push to GitHub and enable Pages in repo Settings")
    print()

if __name__ == "__main__":
    main()
