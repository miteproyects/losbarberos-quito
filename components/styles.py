"""Custom CSS + a floating WhatsApp button.

Agency-style editorial redesign — cream + ink with a single brass-gold accent.
Inspired by thisisstudiox.com: oversized serif display, mono kickers, sharp edges,
flipped dark hero over a light page, subtle marquee, minimal chrome.
"""
from pathlib import Path
import streamlit as st
from components.config import WHATSAPP_NUMBER


# ---- Load the Los Barberos logo once at import time ----
_LOGO_PATH = Path(__file__).resolve().parent.parent / "assets" / "logo.svg"
try:
    _RAW_SVG = _LOGO_PATH.read_text(encoding="utf-8")
    # CRITICAL: Streamlit's markdown parser treats lines indented by 4+ spaces
    # as code blocks even inside `unsafe_allow_html=True`. The logo.svg has
    # nested groups with 4–8-space indentation, which leaks into the page as
    # `<pre><code>` containing raw SVG XML. Collapse the SVG into a single
    # de-indented line so the parser sees it as inline HTML.
    LOGO_SVG = " ".join(line.strip() for line in _RAW_SVG.splitlines() if line.strip())
except FileNotFoundError:
    LOGO_SVG = ""


def logo_svg(css_class: str = "") -> str:
    """Return the Los Barberos SVG logo with an optional CSS class.

    The SVG uses `currentColor` for every stroke/fill, so the color is fully
    driven by the wrapping element — perfect for theme switching.
    """
    if not LOGO_SVG:
        return ""
    if css_class:
        return LOGO_SVG.replace("<svg ", f'<svg class="{css_class}" ', 1)
    return LOGO_SVG


def init_theme():
    # New default: editorial cream (studiox-inspired). Dark remains available.
    if "theme" not in st.session_state:
        st.session_state.theme = "light"


def toggle_theme():
    init_theme()
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"


# ======================================================================
# Design tokens
# ======================================================================
LIGHT_VARS = """
:root {
    --bg: #F2EEE6;            /* warm cream */
    --bg-2: #E9E2D2;          /* deeper cream (cards) */
    --ink: #141414;           /* near-black */
    --ink-soft: #2E2E2E;
    --muted: #6B6660;         /* warm gray */
    --accent: #A8762E;        /* brass */
    --accent-2: #C8944A;
    --line: rgba(20,20,20,.12);
    --line-strong: rgba(20,20,20,.28);
    --card: #EDE6D8;
    --dark-section: #141414;  /* flipped sections */
    --on-dark: #F2EEE6;
    --shadow: 0 14px 40px rgba(40,30,10,.08);
    --img-filter: saturate(1) contrast(.98);
    --map-filter: grayscale(.2) contrast(1.05);
}
"""

DARK_VARS = """
:root {
    --bg: #0E0E0E;
    --bg-2: #161616;
    --ink: #F2EEE6;
    --ink-soft: #C9C6C0;
    --muted: #888580;
    --accent: #D4A24C;
    --accent-2: #E8C070;
    --line: rgba(245,238,230,.14);
    --line-strong: rgba(245,238,230,.3);
    --card: #1A1A1A;
    --dark-section: #070707;
    --on-dark: #F2EEE6;
    --shadow: 0 20px 50px rgba(0,0,0,.55);
    --img-filter: saturate(.92) brightness(.93);
    --map-filter: grayscale(.3) brightness(.85) contrast(1.1);
}
"""


BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..800;1,9..144,300..800&family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');

/* ================================================================
   1. GLOBAL
   ================================================================ */
html, body, [class*="st-"], [class*="css-"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--ink);
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
}

.stApp { background: var(--bg); }

/* Make every Streamlit container transparent */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stVerticalBlock"],
[data-testid="stHorizontalBlock"],
[data-testid="column"],
[data-testid="stForm"],
section.main,
section[data-testid="stSidebar"],
div[data-testid="stDateInput"],
div[data-testid="stTextInput"],
div[data-testid="stSelectbox"],
div[data-testid="stTextArea"],
div[data-testid="stNumberInput"],
div[data-testid="stTimeInput"],
.block-container {
    background: transparent !important;
    background-color: transparent !important;
}

#MainMenu, footer, header[data-testid="stHeader"] {visibility: hidden; height: 0;}
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 0 !important;
    max-width: 1320px;
}

/* ================================================================
   2. TYPOGRAPHY
   ================================================================ */
h1, h2, h3, h4, .display {
    font-family: 'Fraunces', 'Playfair Display', Georgia, serif !important;
    font-weight: 400;
    letter-spacing: -0.015em;
    line-height: 0.98;
    color: var(--ink);
    margin: 0;
}
em, .italic {
    font-family: 'Fraunces', Georgia, serif;
    font-style: italic;
    font-weight: 300;
    color: var(--accent);
}

/* Display scale */
.display-xl {
    font-size: clamp(3.25rem, 11vw, 10.5rem);
    line-height: 0.92;
    font-weight: 400;
    letter-spacing: -0.02em;
}
.display-xl em { font-style: italic; font-weight: 300; color: var(--accent-2); }

.section-title {
    font-size: clamp(2.25rem, 6vw, 4.5rem);
    line-height: 1;
    margin: 0.3rem 0 1.5rem;
    font-weight: 400;
}
.section-title em { font-style: italic; font-weight: 300; color: var(--accent); }

.muted {
    color: var(--muted);
    font-size: 1.05rem;
    line-height: 1.55;
    max-width: 62ch;
    font-family: 'Inter', sans-serif;
}

/* Mono label ("kicker") with leading rule */
.kicker {
    font-family: 'JetBrains Mono', ui-monospace, monospace !important;
    font-size: 0.72rem;
    font-weight: 500;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--muted);
    display: inline-flex;
    align-items: center;
    gap: 0.9rem;
}
.kicker::before {
    content: "";
    width: 42px; height: 1px;
    background: var(--accent);
}
.kicker.center { justify-content: center; }
.kicker.center::before { background: var(--accent); }

/* ================================================================
   3. NAV  (brand + actions)
   ================================================================ */
.brand-logo-wrap {
    display: inline-flex; align-items: center; gap: .75rem;
    text-decoration: none; color: var(--ink);
}
.brand-logo {
    width: 44px; height: 44px; flex: 0 0 auto;
    color: var(--accent);
    transition: transform .5s cubic-bezier(.2,.8,.2,1);
}
.brand-logo-wrap:hover .brand-logo { transform: rotate(-8deg) scale(1.05); }

.brand-text { display: flex; flex-direction: column; line-height: 1; }
.brand-text .brand-top {
    font-family: 'Fraunces', serif;
    font-style: italic;
    font-size: .82rem;
    color: var(--accent);
    letter-spacing: .06em;
    font-weight: 300;
}
.brand-text .brand-bot {
    font-family: 'Fraunces', serif;
    font-weight: 500;
    font-size: 1.35rem;
    letter-spacing: .02em;
    color: var(--ink);
    margin-top: .1rem;
}
.brand-text .brand-bot span { color: var(--accent); font-style: italic; font-weight: 300; }

/* Divider after the nav row */
.nav-rule {
    height: 1px; background: var(--line);
    margin: 1rem 0 1.25rem;
}

/* ================================================================
   4. HERO   (flipped-dark panel inside cream page)
   ================================================================ */
.hero {
    position: relative;
    padding: clamp(3.5rem, 8vw, 6.5rem) clamp(1.5rem, 5vw, 4rem) clamp(3rem, 6vw, 5rem);
    background: var(--dark-section);
    color: var(--on-dark);
    border-radius: 4px;
    overflow: hidden;
    box-shadow: var(--shadow);
    margin-top: 1rem;
}
.hero .display-xl { color: var(--on-dark); }
.hero .display-xl em { color: var(--accent-2); font-style: italic; }

.hero-kicker {
    font-family: 'JetBrains Mono', monospace;
    font-size: .7rem;
    letter-spacing: .2em;
    text-transform: uppercase;
    color: var(--accent-2);
    display: inline-flex; align-items: center; gap: .7rem;
    margin-bottom: 2rem;
}
.hero-kicker::before {
    content: ""; width: 42px; height: 1px; background: var(--accent-2);
}
.hero-kicker.center { justify-content: center; }

.hero-sub {
    font-family: 'Fraunces', Georgia, serif;
    font-weight: 300;
    font-size: clamp(1.1rem, 1.8vw, 1.4rem);
    line-height: 1.45;
    color: rgba(242,238,230,.78);
    max-width: 620px;
    margin: 1.75rem auto 0;
    text-align: center;
}

/* Hero logo medallion (kept but simplified) */
.hero-logo-stage {
    position: relative;
    width: clamp(140px, 18vw, 200px);
    aspect-ratio: 1/1;
    margin: 0 auto 1.75rem;
    display: flex; align-items: center; justify-content: center;
}
.hero-logo-stage::before {
    content: "";
    position: absolute; inset: -10px;
    border-radius: 50%;
    background: conic-gradient(
        from 0deg,
        rgba(212,162,76,0) 0deg,
        rgba(212,162,76,.55) 90deg,
        rgba(232,192,112,.9) 180deg,
        rgba(212,162,76,.35) 270deg,
        rgba(212,162,76,0) 360deg
    );
    -webkit-mask: radial-gradient(circle, transparent 62%, #000 63%, #000 69%, transparent 70%);
            mask: radial-gradient(circle, transparent 62%, #000 63%, #000 69%, transparent 70%);
    animation: haloSpin 12s linear infinite;
    filter: blur(.5px);
    pointer-events: none;
}
.hero-logo {
    position: relative; z-index: 1;
    width: 100%; height: 100%;
    color: var(--on-dark);
    transition: transform .6s cubic-bezier(.2,.8,.2,1);
}
.hero-logo-stage:hover .hero-logo { transform: scale(1.04) rotate(1.5deg); }
@keyframes haloSpin { to { transform: rotate(360deg); } }
@media (prefers-reduced-motion: reduce) { .hero-logo-stage::before { animation: none; } }

/* Hero metrics (inline row) */
.hero-metrics {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 0;
    margin-top: 3rem;
    border-top: 1px solid rgba(245,238,230,.14);
}
@media (max-width: 780px) { .hero-metrics { grid-template-columns: repeat(2, 1fr); } }
.hero-metric {
    padding: 1.5rem 1rem 0;
    border-right: 1px solid rgba(245,238,230,.14);
    text-align: left;
}
.hero-metric:last-child { border-right: none; }
.hero-metric .num {
    font-family: 'Fraunces', serif;
    font-weight: 300;
    font-size: clamp(1.9rem, 3.6vw, 3rem);
    color: var(--accent-2);
    line-height: 1;
}
.hero-metric .lbl {
    font-family: 'JetBrains Mono', monospace;
    font-size: .65rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    color: rgba(242,238,230,.55);
    margin-top: .6rem;
}

/* Hero button row */
.btn-row { display: flex; gap: .75rem; margin-top: 2rem; flex-wrap: wrap; }
.btn-row.center { justify-content: center; }

/* ================================================================
   5. BUTTONS   (minimal, editorial)
   ================================================================ */
.btn, a.btn {
    display: inline-flex;
    align-items: center;
    gap: .6rem;
    padding: .95rem 1.6rem;
    border: 1px solid currentColor;
    border-radius: 2px;
    background: transparent;
    color: var(--ink);
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    font-weight: 500;
    cursor: pointer;
    text-decoration: none;
    transition: background .25s, color .25s, transform .25s;
}
.btn:hover { background: var(--ink); color: var(--bg); transform: translateY(-1px); }

.btn.primary { background: var(--ink); color: var(--bg); border-color: var(--ink); }
.btn.primary:hover { background: var(--accent); border-color: var(--accent); color: var(--bg); }

.btn.ghost { color: var(--ink); border-color: var(--line-strong); }
.btn.ghost:hover { background: var(--ink); color: var(--bg); }

/* Hero buttons (inside dark panel) */
.hero .btn { color: var(--on-dark); border-color: var(--on-dark); }
.hero .btn:hover { background: var(--on-dark); color: var(--ink); }
.hero .btn.primary { background: var(--accent); border-color: var(--accent); color: var(--ink); }
.hero .btn.primary:hover { background: var(--accent-2); border-color: var(--accent-2); color: var(--ink); }
.hero .btn.wa { background: #25D366; border-color: #25D366; color: #fff; }
.hero .btn.wa:hover { background: #1FB656; border-color: #1FB656; }

/* ================================================================
   6. STREAMLIT BUTTONS (nav language + theme toggle)
   ================================================================ */
.stButton > button {
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 500 !important;
    font-size: .72rem !important;
    letter-spacing: .18em !important;
    text-transform: uppercase !important;
    border-radius: 2px !important;
    padding: .7rem 1.1rem !important;
    transition: transform .2s, background .2s, color .2s, border-color .2s !important;
}
.stButton > button[kind="primary"] {
    background: var(--ink) !important;
    color: var(--bg) !important;
    border: 1px solid var(--ink) !important;
    box-shadow: none !important;
}
.stButton > button[kind="primary"]:hover {
    background: var(--accent) !important;
    border-color: var(--accent) !important;
    color: var(--bg) !important;
    transform: translateY(-1px);
}
.stButton > button[kind="secondary"] {
    background: transparent !important;
    color: var(--ink) !important;
    border: 1px solid var(--line-strong) !important;
}
.stButton > button[kind="secondary"]:hover {
    background: var(--ink) !important;
    color: var(--bg) !important;
    border-color: var(--ink) !important;
}
.stButton > button:focus { box-shadow: 0 0 0 3px rgba(168,118,46,.25) !important; }
.stButton > button:disabled { opacity: .4 !important; cursor: not-allowed !important; }

/* Form submit — filled ink */
.stForm .stButton > button[kind="primary"] {
    padding: 1rem 1.8rem !important;
    font-size: .75rem !important;
}

/* ================================================================
   7. MARQUEE  (horizontal infinite scroll)
   ================================================================ */
.marquee {
    overflow: hidden;
    padding: 1.5rem 0;
    margin: 3rem -2rem;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    background: var(--bg);
}
.marquee__track {
    display: inline-flex;
    gap: 2.5rem;
    animation: marqueeScroll 38s linear infinite;
    white-space: nowrap;
    padding-left: 0;
}
.marquee__item {
    font-family: 'Fraunces', Georgia, serif;
    font-size: clamp(1.75rem, 4.2vw, 3.5rem);
    font-weight: 300;
    color: var(--ink);
    display: inline-flex; align-items: center; gap: 2.5rem;
}
.marquee__item em { color: var(--accent); font-weight: 300; }
.marquee__sep {
    color: var(--accent);
    font-size: .7em;
    opacity: .7;
}
@keyframes marqueeScroll {
    from { transform: translateX(0); }
    to   { transform: translateX(-50%); }
}

/* ================================================================
   8. SERVICE CARDS  (flat editorial, hover-flip to dark)
   ================================================================ */
.svc-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1px;
    margin-top: 2rem;
    background: var(--line);
    border: 1px solid var(--line);
}
@media (max-width: 980px) { .svc-grid { grid-template-columns: repeat(2, 1fr); } }
@media (max-width: 620px) { .svc-grid { grid-template-columns: 1fr; } }
.svc-card {
    position: relative;
    padding: 2.5rem 2rem;
    background: var(--bg);
    border-radius: 0;
    transition: background .3s, color .3s;
    display: flex; flex-direction: column; gap: .6rem;
}
.svc-card:hover {
    background: var(--ink);
}
.svc-card:hover .svc-name,
.svc-card:hover .svc-desc,
.svc-card:hover .svc-dur { color: var(--on-dark); }
.svc-card:hover .svc-price { color: var(--accent-2); }
.svc-card:hover .svc-icon { color: var(--accent-2); }
.svc-card:hover .svc-meta { border-top-color: rgba(245,238,230,.18); }

.svc-icon { font-size: 1.5rem; color: var(--accent); transition: color .3s; }
.svc-name {
    font-family: 'Fraunces', serif;
    font-size: clamp(1.5rem, 2vw, 2rem);
    font-weight: 400;
    color: var(--ink);
    margin-top: .4rem;
    transition: color .3s;
}
.svc-desc {
    color: var(--muted);
    font-size: .95rem;
    line-height: 1.55;
    transition: color .3s;
}
.svc-meta {
    display: flex; justify-content: space-between; align-items: baseline;
    margin-top: auto;
    padding-top: 1.25rem;
    border-top: 1px solid var(--line);
    transition: border-color .3s;
}
.svc-price {
    font-family: 'Fraunces', serif;
    font-size: 2.2rem;
    font-weight: 300;
    font-style: italic;
    color: var(--accent);
    line-height: 1;
    transition: color .3s;
}
.svc-dur {
    font-family: 'JetBrains Mono', monospace;
    color: var(--muted);
    font-size: .7rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    transition: color .3s;
}

/* ================================================================
   9. GALLERY  (asymmetric grid)
   ================================================================ */
.gallery {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: .35rem;
    margin-top: 1.75rem;
}
@media (max-width: 980px) { .gallery { grid-template-columns: repeat(2, 1fr); } }
.gallery img {
    width: 100%;
    aspect-ratio: 1/1;
    object-fit: cover;
    border-radius: 2px;
    filter: var(--img-filter);
    transition: transform .5s cubic-bezier(.2,.8,.2,1), filter .3s;
}
.gallery img:nth-child(1), .gallery img:nth-child(8) { aspect-ratio: 4/5; }
.gallery img:hover { transform: scale(1.015); filter: saturate(1.1); }

/* ================================================================
   10. TESTIMONIALS  (editorial pull-quotes)
   ================================================================ */
.testi {
    padding: 2rem 1.5rem;
    border-top: 1px solid var(--line);
    background: transparent;
    height: 100%;
    display: flex; flex-direction: column; gap: .75rem;
}
.testi .stars {
    color: var(--accent);
    letter-spacing: .35em;
    font-size: .9rem;
}
.testi .txt {
    font-family: 'Fraunces', Georgia, serif;
    font-size: 1.25rem;
    line-height: 1.35;
    font-style: italic;
    font-weight: 300;
    color: var(--ink);
}
.testi .who {
    font-family: 'JetBrains Mono', monospace;
    color: var(--muted);
    font-size: .7rem;
    font-weight: 500;
    letter-spacing: .1em;
    text-transform: uppercase;
    margin-top: auto;
}

/* ================================================================
   11. BARBERS / TEAM
   ================================================================ */
.team {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.25rem;
    margin-top: 2rem;
}
@media (max-width: 860px) { .team { grid-template-columns: 1fr; } }
.barber {
    border-radius: 4px;
    overflow: hidden;
    background: transparent;
    border: none;
}
.barber img {
    width: 100%;
    aspect-ratio: 3/4;
    object-fit: cover;
    border-radius: 4px;
    filter: var(--img-filter);
    transition: transform .5s cubic-bezier(.2,.8,.2,1);
}
.barber:hover img { transform: scale(1.02); }
.barber-info { padding: 1rem 0 0; }
.barber-name {
    font-family: 'Fraunces', serif;
    font-size: 1.6rem;
    font-weight: 400;
    color: var(--ink);
}
.barber-role {
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent);
    font-size: .7rem;
    letter-spacing: .15em;
    text-transform: uppercase;
    margin-top: .35rem;
}
.barber-years {
    font-family: 'JetBrains Mono', monospace;
    color: var(--muted);
    font-size: .72rem;
    letter-spacing: .08em;
    margin-top: .4rem;
}

/* ================================================================
   12. ABOUT  (pills)
   ================================================================ */
.pill-list { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1.25rem; }
.pill {
    padding: .45rem 1rem;
    border-radius: 2px;
    background: transparent;
    color: var(--ink);
    border: 1px solid var(--line-strong);
    font-family: 'JetBrains Mono', monospace;
    font-size: .7rem;
    letter-spacing: .1em;
    text-transform: uppercase;
    font-weight: 500;
}

/* ================================================================
   13. FORM INPUTS  (booking)
   ================================================================ */
.stTextInput, .stSelectbox, .stTextArea, .stDateInput, .stTimeInput, .stNumberInput {
    background: transparent !important;
}
.stTextInput > div, .stTextInput > div > div,
.stSelectbox > div, .stSelectbox > div > div,
.stTextArea > div, .stTextArea > div > div,
.stDateInput > div, .stDateInput > div > div,
.stTimeInput > div, .stTimeInput > div > div,
.stNumberInput > div, .stNumberInput > div > div {
    background: transparent !important;
    background-color: transparent !important;
}
div[data-baseweb="input"],
div[data-baseweb="select"],
div[data-baseweb="textarea"],
div[data-baseweb="base-input"],
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] > div,
div[data-baseweb="base-input"] > div {
    background: var(--bg-2) !important;
    background-color: var(--bg-2) !important;
    border-radius: 2px !important;
}
.stSelectbox [data-baseweb="select"] > div,
.stTextInput input, .stTextArea textarea,
.stDateInput input, .stTimeInput input, .stNumberInput input {
    background: var(--bg-2) !important;
    border: 1px solid var(--line) !important;
    border-radius: 2px !important;
    color: var(--ink) !important;
    box-shadow: none !important;
    font-family: 'Inter', sans-serif !important;
}
.stTextInput input:focus,
.stTextArea textarea:focus,
.stDateInput input:focus,
.stTimeInput input:focus,
.stNumberInput input:focus,
.stSelectbox [data-baseweb="select"] > div:focus-within {
    border-color: var(--ink) !important;
    box-shadow: 0 0 0 2px rgba(20,20,20,.1) !important;
    outline: none !important;
}
div[data-baseweb="popover"] > div,
ul[role="listbox"] {
    background: var(--bg-2) !important;
    border: 1px solid var(--line-strong) !important;
    border-radius: 2px !important;
    color: var(--ink) !important;
}
li[role="option"] { background: transparent !important; color: var(--ink) !important; font-family: 'Inter', sans-serif !important; }
li[role="option"]:hover,
li[role="option"][aria-selected="true"] {
    background: var(--ink) !important;
    color: var(--bg) !important;
}
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: var(--muted) !important; opacity: .6;
}
label p {
    color: var(--muted) !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-size: .7rem !important;
    font-weight: 500 !important;
    letter-spacing: .12em !important;
    text-transform: uppercase !important;
}

/* ================================================================
   14. FLOATING WHATSAPP
   ================================================================ */
.wa-float {
    position: fixed; right: 24px; bottom: 24px; z-index: 9999;
    background: #25D366; color: #fff;
    text-decoration: none;
    width: 58px; height: 58px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 12px 30px rgba(37,211,102,.4);
    animation: pulse 2.4s infinite;
    font-size: 28px;
    transition: transform .25s;
}
.wa-float:hover { transform: scale(1.08); }
@keyframes pulse {
    0% { box-shadow: 0 0 0 0 rgba(37,211,102,.55); }
    70% { box-shadow: 0 0 0 20px rgba(37,211,102,0); }
    100% { box-shadow: 0 0 0 0 rgba(37,211,102,0); }
}

/* ================================================================
   15. MAP + CONTACT
   ================================================================ */
.map-wrap {
    border-radius: 4px;
    overflow: hidden;
    border: 1px solid var(--line-strong);
}
.map-wrap iframe {
    display: block; width: 100%; height: 460px;
    border: 0; filter: var(--map-filter);
}

.contact-card {
    padding: 2rem 1.75rem;
    border-radius: 4px;
    background: transparent;
    border: 1px solid var(--line);
}
.contact-card h3 {
    font-family: 'JetBrains Mono', monospace !important;
    color: var(--muted);
    font-size: .72rem;
    letter-spacing: .18em;
    text-transform: uppercase;
    font-weight: 500;
    margin-bottom: .75rem;
    letter-spacing: .18em;
}
.contact-card a { color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--accent); }
.contact-card a:hover { color: var(--accent); }

/* Hours table */
.hours-table { width: 100%; border-collapse: collapse; font-family: 'Inter', sans-serif; }
.hours-table td { padding: .5rem 0; border-bottom: 1px dashed var(--line); }
.hours-table td:first-child {
    color: var(--muted);
    font-family: 'JetBrains Mono', monospace;
    font-size: .72rem;
    letter-spacing: .1em;
    text-transform: uppercase;
}
.hours-table td:last-child { text-align: right; font-weight: 500; color: var(--ink); font-family: 'Inter', sans-serif; }

/* ================================================================
   16. FOOTER
   ================================================================ */
.footer {
    margin-top: 5rem;
    padding: 2.5rem 0 2rem;
    border-top: 1px solid var(--line-strong);
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 1rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--muted);
    font-size: .7rem;
    letter-spacing: .1em;
    text-transform: uppercase;
}

/* ================================================================
   17. OPTION-MENU (streamlit-option-menu)
   ================================================================ */
.nav-link { color: var(--ink) !important; font-weight: 500 !important; font-family: 'JetBrains Mono', monospace !important; font-size: .72rem !important; letter-spacing: .15em !important; text-transform: uppercase !important; }
.nav-link.active { background: var(--ink) !important; color: var(--bg) !important; }
.nav-link.active .icon, .nav-link.active i { color: var(--bg) !important; }
.nav-link:hover { color: var(--accent) !important; background: transparent !important; }
.nav-link i, .nav-link svg { color: var(--accent) !important; }
.nav-link.active i, .nav-link.active svg { color: var(--accent-2) !important; }

/* ================================================================
   18. ENTRANCE ANIMATION
   ================================================================ */
.fade-up { animation: fadeUp .7s ease both; }
.fade-up-delay { animation: fadeUp .7s ease both .1s; }
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}

/* ================================================================
   19. NAV PILL ALIGNMENT  (theme toggle + ES + EN share a centerline)
   ================================================================ */
div[data-testid="stHorizontalBlock"]:has(.nav-pill) {
    align-items: center !important;
    gap: .4rem !important;
}
div[data-testid="stHorizontalBlock"]:has(.nav-pill) [data-testid="column"],
div[data-testid="stHorizontalBlock"]:has(.nav-pill) [data-testid="stColumn"] {
    display: flex !important;
    flex-direction: column !important;
    justify-content: center !important;
}
div[data-testid="stHorizontalBlock"]:has(.nav-pill) [data-testid="stElementContainer"]:has(.nav-pill) {
    margin: 0 !important;
    padding: 0 !important;
    min-height: 0 !important;
    height: 0 !important;
    overflow: hidden !important;
}
div[data-testid="stHorizontalBlock"]:has(.nav-pill) [data-testid="stElementContainer"]:has(.nav-pill) * {
    margin: 0 !important; padding: 0 !important;
}
div[data-testid="stHorizontalBlock"]:has(.nav-pill) [data-testid="stElementContainer"]:has(.stButton) {
    height: 40px !important;
    min-height: 40px !important;
    max-height: 40px !important;
    margin: 0 !important;
    padding: 0 !important;
    display: flex !important;
    align-items: center !important;
}
div[data-testid="stHorizontalBlock"]:has(.nav-pill) .stButton,
div[data-testid="stHorizontalBlock"]:has(.nav-pill) .stButton > button,
div[data-testid="stHorizontalBlock"]:has(.nav-pill) .stButton > button[kind="primary"],
div[data-testid="stHorizontalBlock"]:has(.nav-pill) .stButton > button[kind="secondary"] {
    height: 40px !important;
    min-height: 40px !important;
    max-height: 40px !important;
    border-radius: 2px !important;
    padding: 0 1rem !important;
    margin: 0 !important;
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    line-height: 1 !important;
    font-size: .72rem !important;
    letter-spacing: .15em !important;
    text-transform: uppercase !important;
    font-family: 'JetBrains Mono', monospace !important;
    font-weight: 500 !important;
    width: 100% !important;
    box-sizing: border-box !important;
}
/* Theme toggle = icon-only square */
div[data-testid="stHorizontalBlock"]:has(.theme-toggle-wrap) [data-testid="column"]:first-child .stButton > button {
    background: transparent !important;
    color: var(--ink) !important;
    border: 1px solid var(--line-strong) !important;
    font-size: 1rem !important;
}
div[data-testid="stHorizontalBlock"]:has(.theme-toggle-wrap) [data-testid="column"]:first-child .stButton > button:hover {
    background: var(--ink) !important;
    border-color: var(--ink) !important;
    color: var(--bg) !important;
    transform: translateY(-1px);
}

/* ================================================================
   20. UTILITY
   ================================================================ */
.divider { height: 1px; background: var(--line); margin: 3rem 0; }
.section { margin: 4.5rem 0; }
.split { display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; align-items: start; }
@media (max-width: 900px) { .split { grid-template-columns: 1fr; gap: 1.5rem; } }

/* Section number badge (e.g. "01 — SERVICIOS") */
.sec-num {
    font-family: 'JetBrains Mono', monospace;
    font-size: .7rem;
    color: var(--accent);
    font-weight: 500;
    letter-spacing: .15em;
    margin-right: .75rem;
}

/* "Scroll" hint */
.scroll-hint {
    font-family: 'JetBrains Mono', monospace;
    font-size: .65rem;
    letter-spacing: .3em;
    text-transform: uppercase;
    color: rgba(242,238,230,.5);
    display: flex; align-items: center; justify-content: center; gap: .5rem;
    margin-top: 3rem;
}
.scroll-hint::after {
    content: ""; width: 1px; height: 28px;
    background: linear-gradient(to bottom, rgba(242,238,230,.5), transparent);
    animation: scrollPulse 2s ease-in-out infinite;
}
@keyframes scrollPulse {
    0%, 100% { transform: scaleY(.5); opacity: .4; }
    50% { transform: scaleY(1); opacity: 1; }
}
</style>
"""


def inject_css(theme: str = "light"):
    palette = f"<style>{LIGHT_VARS if theme == 'light' else DARK_VARS}</style>"
    st.markdown(palette + BASE_CSS, unsafe_allow_html=True)


def floating_whatsapp(message: str = "Hola! Quisiera reservar un turno."):
    from urllib.parse import quote
    url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
    html = f"""
    <a href="{url}" target="_blank" class="wa-float" aria-label="WhatsApp">
        <svg width="30" height="30" viewBox="0 0 24 24" fill="#fff" xmlns="http://www.w3.org/2000/svg">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.15-.174.199-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51l-.57-.01c-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893A11.821 11.821 0 0 0 20.464 3.488"/>
        </svg>
    </a>
    """
    st.markdown(html, unsafe_allow_html=True)
