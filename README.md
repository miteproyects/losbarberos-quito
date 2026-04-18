# 💈 Los Barberos Quito — Bilingual Streamlit Website

A modern, dark-luxury, **Spanish / English** website for the Quito-based barbershop
[Los Barberos Quito](https://www.facebook.com/LosBarberosQuito/).

Built with **Streamlit** · animated hero · booking calendar · WhatsApp integration ·
interactive market analysis · mobile-responsive.

---

## ✨ Features

- **Fully bilingual (ES / EN)** toggle with session persistence
- **Modern dark + gold UI** — custom CSS, glassmorphism, smooth animations
- **Horizontal top-nav** (streamlit-option-menu) with 7 sections
- **Hero section** with background image, metrics row, CTAs
- **Service catalog** — 6 services with icons, prices (USD), duration
- **Interactive gallery** — auto-filled with Unsplash imagery
- **Team / barbers** section
- **Client testimonials**
- **📅 Booking calendar** — date picker, time-slot generator (respects business hours),
  SQLite persistence, auto-generates pre-filled WhatsApp confirmation message
- **💬 WhatsApp integration** — floating pulse button (always visible) + CTA buttons
  throughout the site, all with localized messages
- **📊 Market analysis page** — Plotly charts for market size, Quito competitor
  landscape, customer personas, SWOT, 90-day growth playbook, recommended channel mix
- **Contact section** with hours table, Google Maps embed, social links
- **SEO-ready page title + icon**

---

## 🚀 Quick start

```bash
# 1. Clone / download this repo
git clone https://github.com/<you>/losbarberos-quito.git
cd losbarberos-quito

# 2. Create virtual env (optional but recommended)
python -m venv .venv && source .venv/bin/activate       # Linux / macOS
# .venv\Scripts\activate                                 # Windows

# 3. Install deps
pip install -r requirements.txt

# 4. Run
streamlit run app.py
```

Then open <http://localhost:8501>.

---

## 🛠 Customization

All business-specific content lives in **`components/config.py`** — edit one file
and every section of the site updates. Fields marked `# TODO` are the placeholders
you must replace before going live:

| What | Where |
| ---- | ----- |
| WhatsApp number (E.164, digits only) | `WHATSAPP_NUMBER` |
| Display phone | `PHONE_DISPLAY` |
| Email | `EMAIL` |
| Street address | `ADDRESS_ES` / `ADDRESS_EN` |
| Google Maps embed `src` | `GOOGLE_MAPS_EMBED` |
| Hours (24h) | `HOURS` dict |
| Services + prices | `SERVICES` list |
| Barber roster | `BARBERS` list |
| Gallery images | `GALLERY` list (any public image URLs) |
| Social URLs | `FACEBOOK`, `INSTAGRAM`, `TIKTOK` |

To add more text strings in both languages, edit `components/i18n.py`.

---

## 🧭 Project structure

```
losbarberos-quito/
├── app.py                       # Main entry — routing + navbar + footer
├── requirements.txt
├── README.md                    # You are here
├── LICENSE
├── .gitignore
├── .streamlit/
│   └── config.toml              # Theme + server settings
├── components/
│   ├── config.py                # ✏️  ALL business data (edit me!)
│   ├── i18n.py                  # ES / EN translation dictionary
│   ├── styles.py                # Custom CSS + floating WhatsApp button
│   ├── sections.py              # Hero, services, gallery, about, contact, footer
│   ├── booking.py               # Booking calendar + WhatsApp handoff
│   └── market.py                # Market analysis (Plotly charts)
└── data/                        # SQLite DB lives here at runtime
```

---

## 📦 Push to GitHub

From inside the project folder:

```bash
git init -b main
git add .
git commit -m "Initial commit: Los Barberos Quito bilingual Streamlit site"

# Option A — with GitHub CLI (recommended)
gh repo create losbarberos-quito --public --source=. --remote=origin --push

# Option B — manually
# 1. Create an empty repo at github.com/<you>/losbarberos-quito (no README)
# 2. Then:
git remote add origin https://github.com/<you>/losbarberos-quito.git
git push -u origin main
```

---

## ☁️ Deploy to Streamlit Community Cloud (free)

1. Push the repo to GitHub (see above).
2. Go to <https://share.streamlit.io> and sign in with GitHub.
3. Click **"New app"** → pick your repo → `app.py` → Deploy.
4. Share the public URL with clients.

Zero-config — the included `.streamlit/config.toml` sets the theme, and
`requirements.txt` is auto-detected.

---

## 💬 How the WhatsApp integration works

- Every CTA button builds a `https://wa.me/<number>?text=<urlencoded message>` link.
- The **floating button** (bottom-right, pulsing) opens a generic "I want to book" message.
- After a successful booking-form submit, the app generates a **pre-filled
  confirmation message** including service, barber, date, time, and notes — the
  owner gets a clean, copy-paste-ready message on their phone.
- No WhatsApp Business API / Twilio needed: all handoffs are deep-links.

For proactive reminders (e.g. "your appointment is tomorrow") upgrade to
**WhatsApp Business Cloud API** — see the 90-day growth playbook on the Market page.

---

## 📈 Market analysis (built-in)

The **Market** tab is a fully interactive mini-dashboard meant to help the owner
grow the shop:

- Global market-size projection (2021–2026)
- Scatter of top Quito competitors (rating × review volume) — sourced from Barberhead
- Four customer personas with recommended acquisition channels
- SWOT analysis tailored to an Ecuadorian premium barbershop
- 90-day growth playbook (Day 0–15, 15–30, 30–60, 60–90, ongoing)
- Recommended channel-mix bar chart + expected CAC overlay

Data sources (as of 2025-2026): Kentley Insights, Accio, Upmetrics, Barberhead,
Google Maps review aggregates.

---

## 📄 License

MIT — see [LICENSE](LICENSE).
