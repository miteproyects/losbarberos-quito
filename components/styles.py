"""Custom CSS + a floating WhatsApp button. Modern dark-luxury barbershop theme."""
import streamlit as st
from components.config import WHATSAPP_NUMBER


def init_theme():
    if "theme" not in st.session_state:
        st.session_state.theme = "dark"


def toggle_theme():
    init_theme()
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"


DARK_VARS = """
:root {
    --gold: #D4A24C;
    --gold-soft: #E8C070;
    --ink: #0B0B0D;
    --ink-2: #17171B;
    --ink-3: #1F1F25;
    --line: rgba(212,162,76,.25);
    --text: #F5F5F5;
    --text-dim: #B9B9C0;
    --card-bg: rgba(23,23,27,.6);
    --card-bg-strong: rgba(23,23,27,.85);
    --svc-card-grad: linear-gradient(165deg, rgba(31,31,37,.95), rgba(17,17,22,.95));
    --hero-overlay: linear-gradient(135deg, rgba(11,11,13,.82), rgba(11,11,13,.55) 50%, rgba(11,11,13,.9));
    --app-bg:
        radial-gradient(1200px 500px at 10% -10%, rgba(212,162,76,.12), transparent 60%),
        radial-gradient(900px 500px at 100% 10%, rgba(212,162,76,.06), transparent 60%),
        #0B0B0D;
    --shadow-hero: 0 30px 80px rgba(0,0,0,.6);
    --shadow-card: 0 20px 40px rgba(0,0,0,.5);
    --img-filter: saturate(.9) brightness(.95);
    --map-filter: grayscale(.1) brightness(.9) contrast(1.1);
}
"""

LIGHT_VARS = """
:root {
    --gold: #A8762E;
    --gold-soft: #D4A24C;
    --ink: #F4EEE2;
    --ink-2: #FFFFFF;
    --ink-3: #EAE2D1;
    --line: rgba(168,118,46,.35);
    --text: #1A1A1F;
    --text-dim: #4A4A52;
    --card-bg: rgba(255,255,255,.85);
    --card-bg-strong: rgba(255,255,255,.98);
    --svc-card-grad: linear-gradient(165deg, rgba(255,255,255,.95), rgba(244,238,226,.95));
    /* Hero overlay stays dark regardless of theme so white text stays legible */
    --hero-overlay: linear-gradient(135deg, rgba(11,11,13,.82), rgba(11,11,13,.55) 50%, rgba(11,11,13,.9));
    --app-bg:
        radial-gradient(1200px 500px at 10% -10%, rgba(168,118,46,.18), transparent 60%),
        radial-gradient(900px 500px at 100% 10%, rgba(168,118,46,.08), transparent 60%),
        #F4EEE2;
    --shadow-hero: 0 30px 80px rgba(70,50,20,.28);
    --shadow-card: 0 14px 34px rgba(70,50,20,.14);
    --img-filter: saturate(1.05) brightness(1);
    --map-filter: none;
}
"""

BASE_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,700;1,400&display=swap');

/* ---------- Global ---------- */
html, body, [class*="st-"], [class*="css-"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    color: var(--text);
}

.stApp {
    background: var(--app-bg);
}
/* Every Streamlit layout container must be transparent so the themed --app-bg shows through */
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

/* Hide Streamlit chrome */
#MainMenu, footer, header[data-testid="stHeader"] {visibility: hidden; height: 0;}
.block-container {padding-top: 1rem !important; padding-bottom: 0 !important; max-width: 1200px;}

/* ---------- Typography ---------- */
h1, h2, h3, .display {font-family: 'Bebas Neue', sans-serif !important; letter-spacing: 1px;}
.display-xl {font-size: clamp(3rem, 7vw, 6.5rem); line-height: .95; font-weight: 400; color: var(--text);}
.display-xl em {font-family: 'Playfair Display', serif; font-style: italic; color: var(--gold); font-weight: 400;}
.kicker {font-family: 'Inter', sans-serif; letter-spacing: .3em; font-size: .75rem; font-weight: 600; color: var(--gold); text-transform: uppercase;}
.section-title {font-size: clamp(2rem, 4vw, 3.5rem); line-height: 1; color: var(--text); margin: .25rem 0 1rem 0;}
.muted {color: var(--text-dim); font-size: 1.05rem; line-height: 1.6;}

/* ---------- Navbar ---------- */
.nav-wrap {
    display: flex; align-items: center; justify-content: space-between;
    padding: .75rem 1rem; border-radius: 999px;
    background: var(--card-bg); backdrop-filter: blur(20px);
    border: 1px solid var(--line);
    margin-bottom: 1.5rem;
}
.brand {display: flex; align-items: center; gap: .6rem; font-family: 'Bebas Neue', sans-serif; font-size: 1.4rem; letter-spacing: 2px;}
.brand-dot {width: 10px; height: 10px; border-radius: 50%; background: var(--gold); box-shadow: 0 0 18px var(--gold);}
.brand em {font-family: 'Playfair Display', serif; color: var(--gold); font-weight: 700; font-style: italic;}
.lang-toggle {display: flex; gap: .25rem; background: rgba(0,0,0,.3); padding: 3px; border-radius: 999px; border: 1px solid var(--line);}
.lang-toggle button {background: transparent; border: 0; color: var(--text-dim); padding: .35rem .85rem; border-radius: 999px; cursor: pointer; font-weight: 600;}
.lang-toggle button.on {background: var(--gold); color: #000;}

/* ---------- Hero (always dark overlay over image → always light text) ---------- */
.hero {
    position: relative;
    border-radius: 28px; overflow: hidden;
    padding: clamp(2rem, 5vw, 4rem);
    background:
        var(--hero-overlay),
        url('https://images.unsplash.com/photo-1622287162716-f311baa1a2b8?w=1800') center/cover;
    border: 1px solid rgba(212,162,76,.3);
    box-shadow: var(--shadow-hero);
    color: #F5F5F5;
}
.hero .display-xl {color: #F5F5F5;}
.hero .display-xl em {color: #E8C070;}
.hero-badge {
    display: inline-block; padding: .45rem 1rem;
    border: 1px solid rgba(212,162,76,.3); border-radius: 999px;
    background: rgba(212,162,76,.15); color: #E8C070;
    font-size: .75rem; letter-spacing: .25em; font-weight: 600; margin-bottom: 1.5rem;
}
.hero-sub {font-size: 1.1rem; color: rgba(245,245,245,.85); max-width: 640px; margin-top: 1rem;}
/* Metrics inside hero always stay dark-glass */
.hero .metric {
    background: rgba(23,23,27,.55) !important;
    border: 1px solid rgba(212,162,76,.3) !important;
}
.hero .metric .num {color: #E8C070 !important;}
.hero .metric .lbl {color: #D4D4D8 !important;}

/* ---------- Buttons ---------- */
.btn-row {display: flex; gap: .75rem; margin-top: 1.75rem; flex-wrap: wrap;}
.btn, a.btn {
    display: inline-flex; align-items: center; gap: .5rem;
    padding: .85rem 1.5rem; border-radius: 999px;
    font-weight: 600; letter-spacing: .02em; cursor: pointer;
    border: 1px solid var(--line); text-decoration: none;
    transition: transform .15s ease, box-shadow .2s ease, background .2s;
}
.btn.primary {background: var(--gold); color: #000; border-color: var(--gold);}
.btn.primary:hover {transform: translateY(-2px); box-shadow: 0 12px 30px rgba(212,162,76,.35);}
.btn.ghost {background: rgba(255,255,255,.03); color: var(--text);}
.btn.ghost:hover {background: rgba(212,162,76,.12); border-color: var(--gold);}
.btn.wa {background: #25D366; color: #05240d; border-color: #25D366;}

/* ---------- Streamlit button overrides ---------- */
.stButton > button {
    font-weight: 700 !important;
    border-radius: 999px !important;
    padding: .7rem 1.4rem !important;
    transition: transform .15s, box-shadow .2s, background .2s, color .2s !important;
}
/* Primary = filled gold (active language, submit CTA) */
.stButton > button[kind="primary"] {
    background: var(--gold) !important;
    color: #0B0B0D !important;
    border: 1px solid var(--gold) !important;
    box-shadow: 0 4px 14px rgba(168,118,46,.25) !important;
}
.stButton > button[kind="primary"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(168,118,46,.45) !important;
}
/* Secondary = outlined (inactive language, default buttons) */
.stButton > button[kind="secondary"] {
    background: transparent !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
}
.stButton > button[kind="secondary"]:hover {
    background: rgba(212,162,76,.12) !important;
    border-color: var(--gold) !important;
    color: var(--gold) !important;
}
.stButton > button:focus {box-shadow: 0 0 0 3px rgba(212,162,76,.35) !important;}
/* Disabled (e.g. submit when no slot selected) */
.stButton > button:disabled {opacity: .45 !important; cursor: not-allowed !important;}

/* ---------- Metrics ---------- */
.metrics {display: grid; grid-template-columns: repeat(4, 1fr); gap: 1rem; margin-top: 2rem;}
@media (max-width: 780px) {.metrics {grid-template-columns: repeat(2, 1fr);}}
.metric {
    padding: 1.25rem 1.1rem; border-radius: 18px;
    background: var(--card-bg); border: 1px solid var(--line); backdrop-filter: blur(10px);
}
.metric .num {font-family: 'Bebas Neue'; font-size: 2.5rem; color: var(--gold); line-height: 1;}
.metric .lbl {color: var(--text-dim); font-size: .85rem; margin-top: .25rem;}

/* ---------- Service cards ---------- */
.svc-grid {display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem; margin-top: 1.75rem;}
@media (max-width: 980px) {.svc-grid {grid-template-columns: repeat(2, 1fr);}}
@media (max-width: 620px) {.svc-grid {grid-template-columns: 1fr;}}
.svc-card {
    position: relative; overflow: hidden;
    padding: 1.75rem 1.4rem; border-radius: 22px;
    background: var(--svc-card-grad);
    border: 1px solid var(--line);
    transition: transform .25s, border-color .25s, box-shadow .25s;
}
.svc-card::before {
    content: ""; position: absolute; inset: -1px;
    background: linear-gradient(135deg, transparent 60%, rgba(212,162,76,.2));
    opacity: 0; transition: opacity .3s; pointer-events: none; border-radius: 22px;
}
.svc-card:hover {transform: translateY(-6px); border-color: var(--gold); box-shadow: var(--shadow-card);}
.svc-card:hover::before {opacity: 1;}
.svc-icon {font-size: 2rem;}
.svc-name {font-family: 'Bebas Neue'; font-size: 1.7rem; letter-spacing: 1px; margin: .5rem 0 .35rem 0;}
.svc-desc {color: var(--text-dim); font-size: .95rem; line-height: 1.5;}
.svc-meta {display: flex; justify-content: space-between; align-items: center; margin-top: 1.1rem; padding-top: 1rem; border-top: 1px dashed var(--line);}
.svc-price {font-family: 'Bebas Neue'; font-size: 2rem; color: var(--gold);}
.svc-dur {color: var(--text-dim); font-size: .85rem;}

/* ---------- Gallery ---------- */
.gallery {display: grid; grid-template-columns: repeat(4, 1fr); gap: .5rem; margin-top: 1.5rem;}
@media (max-width: 980px) {.gallery {grid-template-columns: repeat(2, 1fr);}}
.gallery img {width: 100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 14px; transition: transform .3s, filter .3s; filter: var(--img-filter);}
.gallery img:hover {transform: scale(1.02); filter: saturate(1.15) brightness(1.05);}

/* ---------- Testimonials ---------- */
.testi {
    padding: 1.5rem; border-radius: 20px;
    background: var(--card-bg); border: 1px solid var(--line);
    height: 100%;
}
.testi .stars {color: var(--gold); letter-spacing: 2px;}
.testi .txt {font-family: 'Playfair Display', serif; font-size: 1.05rem; line-height: 1.5; font-style: italic; margin: .5rem 0 .75rem 0;}
.testi .who {color: var(--text-dim); font-size: .9rem; font-weight: 600;}

/* ---------- Barber cards ---------- */
.team {display: grid; grid-template-columns: repeat(3, 1fr); gap: 1rem;}
@media (max-width: 860px) {.team {grid-template-columns: 1fr;}}
.barber {
    border-radius: 22px; overflow: hidden;
    background: var(--ink-2); border: 1px solid var(--line);
}
.barber img {width: 100%; aspect-ratio: 3/4; object-fit: cover; filter: var(--img-filter);}
.barber-info {padding: 1rem 1.2rem;}
.barber-name {font-family: 'Bebas Neue'; font-size: 1.6rem; letter-spacing: 1.5px;}
.barber-role {color: var(--gold); font-size: .85rem; letter-spacing: .15em; text-transform: uppercase;}
.barber-years {color: var(--text-dim); font-size: .85rem; margin-top: .5rem;}

/* ---------- About ---------- */
.pill-list {display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1rem;}
.pill {
    padding: .5rem 1rem; border-radius: 999px;
    background: rgba(212,162,76,.08); color: var(--gold);
    border: 1px solid var(--line); font-size: .85rem; font-weight: 600;
}

/* ---------- Booking form ---------- */
/* Kill Streamlit's secondaryBackgroundColor bleed.
   Make every wrapper match the input surface so the 1-2px gap around rounded corners blends. */
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
/* baseweb inner containers get the SAME ink-3 color as the editable surface,
   so corners match whether the browser paints the wrapper or the input */
div[data-baseweb="input"],
div[data-baseweb="select"],
div[data-baseweb="textarea"],
div[data-baseweb="base-input"],
div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div,
div[data-baseweb="textarea"] > div,
div[data-baseweb="base-input"] > div {
    background: var(--ink-3) !important;
    background-color: var(--ink-3) !important;
    border-radius: 14px !important;
}

/* The actual editable surface — same color, matching rounded corners */
.stSelectbox [data-baseweb="select"] > div,
.stTextInput input, .stTextArea textarea,
.stDateInput input, .stTimeInput input, .stNumberInput input {
    background: var(--ink-3) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    color: var(--text) !important;
    box-shadow: none !important;
}
/* Focus */
.stTextInput input:focus,
.stTextArea textarea:focus,
.stDateInput input:focus,
.stTimeInput input:focus,
.stNumberInput input:focus,
.stSelectbox [data-baseweb="select"] > div:focus-within {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(212,162,76,.22) !important;
    outline: none !important;
}
/* Dropdown menu popover (selectbox options list) */
div[data-baseweb="popover"] > div,
ul[role="listbox"] {
    background: var(--ink-2) !important;
    border: 1px solid var(--line) !important;
    border-radius: 14px !important;
    color: var(--text) !important;
}
li[role="option"] {background: transparent !important; color: var(--text) !important;}
li[role="option"]:hover,
li[role="option"][aria-selected="true"] {
    background: rgba(212,162,76,.15) !important;
    color: var(--gold) !important;
}
/* Placeholder color */
.stTextInput input::placeholder, .stTextArea textarea::placeholder {
    color: var(--text-dim) !important; opacity: .7;
}
label p {color: var(--text-dim) !important; font-weight: 600 !important;}

/* ---------- Floating WhatsApp ---------- */
.wa-float {
    position: fixed; right: 20px; bottom: 20px; z-index: 9999;
    background: #25D366; color: #fff; text-decoration: none;
    width: 60px; height: 60px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    box-shadow: 0 10px 30px rgba(37,211,102,.45);
    animation: pulse 2.2s infinite;
    font-size: 28px;
}
.wa-float:hover {transform: scale(1.08);}
@keyframes pulse {
    0% {box-shadow: 0 0 0 0 rgba(37,211,102,.55);}
    70% {box-shadow: 0 0 0 18px rgba(37,211,102,0);}
    100% {box-shadow: 0 0 0 0 rgba(37,211,102,0);}
}

/* ---------- Map ---------- */
.map-wrap {border-radius: 20px; overflow: hidden; border: 1px solid var(--line);}
.map-wrap iframe {display: block; width: 100%; height: 340px; border: 0; filter: var(--map-filter);}

/* ---------- Footer ---------- */
.footer {
    margin-top: 4rem; padding: 2rem 1rem 1.5rem;
    border-top: 1px solid var(--line); color: var(--text-dim); font-size: .9rem;
    display: flex; justify-content: space-between; flex-wrap: wrap; gap: 1rem;
}

/* ---------- Option-menu override (bootstrap-icons based) ---------- */
.nav-link {color: var(--text-dim) !important; font-weight: 600 !important;}
.nav-link.active {background: var(--gold) !important; color: #0B0B0D !important;}
.nav-link.active .icon {color: #0B0B0D !important;}
.nav-link:hover {color: var(--gold) !important;}

/* ---------- Entrance animation ---------- */
.fade-up {animation: fadeUp .6s ease both;}
@keyframes fadeUp {from {opacity: 0; transform: translateY(16px);} to {opacity: 1; transform: translateY(0);}}

/* ---------- Theme toggle button (sun / moon) — matches ES/EN height ---------- */
.theme-toggle-wrap .stButton > button,
.theme-toggle-wrap .stButton > button[kind="primary"],
.theme-toggle-wrap .stButton > button[kind="secondary"] {
    background: var(--card-bg) !important;
    color: var(--gold) !important;
    border: 1px solid var(--line) !important;
    border-radius: 999px !important;
    width: 100% !important;
    min-width: 0 !important;
    height: auto !important;
    padding: .7rem 1.4rem !important;   /* same vertical padding as ES/EN */
    font-size: 1.1rem !important;
    font-weight: 400 !important;
    line-height: 1 !important;
    display: flex !important; align-items: center !important; justify-content: center !important;
    backdrop-filter: blur(20px);
    transition: transform .2s, background .2s, box-shadow .2s, border-color .2s !important;
    box-shadow: none !important;
}
.theme-toggle-wrap .stButton > button:hover {
    transform: translateY(-1px) !important;
    background: rgba(212,162,76,.12) !important;
    border-color: var(--gold) !important;
    color: var(--gold) !important;
    box-shadow: 0 8px 22px rgba(212,162,76,.25) !important;
}

/* ---------- Utility ---------- */
.divider {height: 1px; background: linear-gradient(90deg, transparent, var(--line), transparent); margin: 3rem 0;}
.section {margin: 3.5rem 0;}
</style>
"""


def inject_css(theme: str = "dark"):
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
