"""All website sections rendered as functions."""
from urllib.parse import quote
import streamlit as st


def _flat(html: str) -> str:
    """Strip leading whitespace from each line so Streamlit's markdown
    parser doesn't misinterpret indented HTML as a code block."""
    return "\n".join(line.lstrip() for line in html.splitlines())

from components.i18n import t, tlist
from components.config import (
    BUSINESS_NAME, TAGLINE_ES, TAGLINE_EN,
    WHATSAPP_NUMBER, PHONE_DISPLAY, EMAIL,
    ADDRESS_ES, ADDRESS_EN, GOOGLE_MAPS_EMBED,
    FACEBOOK, INSTAGRAM, TIKTOK,
    HOURS, SERVICES, BARBERS, GALLERY, TESTIMONIALS,
)


def _whatsapp_link(message: str) -> str:
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"


# -----------------------------------------------------------------
# Hero
# -----------------------------------------------------------------
def render_hero():
    lang = st.session_state.lang
    title_html = (
        "Más que un <em>corte</em>.<br/>Una <em>experiencia</em>."
        if lang == "es"
        else "More than a <em>cut</em>.<br/>An <em>experience</em>."
    )
    wa_url = _whatsapp_link("Hola! Me gustaría reservar un turno en Los Barberos.")
    st.markdown(
        _flat(f"""
        <div class="hero fade-up">
            <span class="hero-badge">{t('hero_badge')}</span>
            <h1 class="display-xl">{title_html}</h1>
            <p class="hero-sub">{t('hero_sub')}</p>
            <div class="btn-row">
                <a class="btn primary" href="#booking">✂️ {t('cta_book')}</a>
                <a class="btn wa" href="{wa_url}" target="_blank">💬 {t('cta_whatsapp')}</a>
            </div>
            <div class="metrics">
                <div class="metric"><div class="num">15k+</div><div class="lbl">{t('m_clients')}</div></div>
                <div class="metric"><div class="num">10+</div><div class="lbl">{t('m_years')}</div></div>
                <div class="metric"><div class="num">4.8★</div><div class="lbl">{t('m_rating')}</div></div>
                <div class="metric"><div class="num">{len(BARBERS)}</div><div class="lbl">{t('m_barbers')}</div></div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


# -----------------------------------------------------------------
# Services
# -----------------------------------------------------------------
def render_services():
    lang = st.session_state.lang
    st.markdown('<div id="services" class="section">', unsafe_allow_html=True)
    st.markdown(
        _flat(f"""
        <div class="fade-up">
            <div class="kicker">{t('services_kicker')}</div>
            <h2 class="section-title">{t('services_title')}</h2>
            <p class="muted">{t('services_sub')}</p>
        </div>
        """),
        unsafe_allow_html=True,
    )

    cards = ""
    for s in SERVICES:
        name = s["name_es"] if lang == "es" else s["name_en"]
        desc = s["desc_es"] if lang == "es" else s["desc_en"]
        cards += f"""
        <div class="svc-card fade-up">
            <div class="svc-icon">{s['icon']}</div>
            <div class="svc-name">{name}</div>
            <div class="svc-desc">{desc}</div>
            <div class="svc-meta">
                <div class="svc-price">${s['price']}</div>
                <div class="svc-dur">⏱ {s['duration']} {t('svc_duration')}</div>
            </div>
        </div>
        """
    st.markdown(_flat(f'<div class="svc-grid">{cards}</div>'), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------
# Gallery
# -----------------------------------------------------------------
def render_gallery():
    st.markdown('<div id="gallery" class="section">', unsafe_allow_html=True)
    st.markdown(
        _flat(f"""
        <div class="fade-up">
            <div class="kicker">{t('gallery_kicker')}</div>
            <h2 class="section-title">{t('gallery_title')}</h2>
        </div>
        """),
        unsafe_allow_html=True,
    )
    imgs = "".join([f'<img src="{u}" alt="barbershop"/>' for u in GALLERY])
    st.markdown(f'<div class="gallery fade-up">{imgs}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------
# About + team
# -----------------------------------------------------------------
def render_about():
    lang = st.session_state.lang
    st.markdown('<div id="about" class="section">', unsafe_allow_html=True)
    col1, col2 = st.columns([1.1, 1], gap="large")
    with col1:
        st.markdown(
            _flat(f"""
            <div class="fade-up">
                <div class="kicker">{t('about_kicker')}</div>
                <h2 class="section-title">{t('about_title')}</h2>
                <p class="muted">{t('about_body')}</p>
                <div class="pill-list">
                    {''.join(f'<span class="pill">{v}</span>' for v in tlist('values'))}
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            '<img src="https://images.unsplash.com/photo-1585747860715-2ba37e788b70?w=900" '
            'style="width:100%; border-radius:22px; border:1px solid var(--line);"/>',
            unsafe_allow_html=True,
        )

    # Team
    st.markdown(
        f'<h3 class="section-title" style="margin-top:2.5rem;">{t("team_title")}</h3>',
        unsafe_allow_html=True,
    )
    cards = ""
    for b in BARBERS:
        role = b["role_es"] if lang == "es" else b["role_en"]
        cards += f"""
        <div class="barber fade-up">
            <img src="{b['img']}" alt="{b['name']}"/>
            <div class="barber-info">
                <div class="barber-name">{b['name']}</div>
                <div class="barber-role">{role}</div>
                <div class="barber-years">⏳ {b['years']} {t('years_exp')}</div>
            </div>
        </div>
        """
    st.markdown(_flat(f'<div class="team">{cards}</div>'), unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------
# Testimonials
# -----------------------------------------------------------------
def render_testimonials():
    lang = st.session_state.lang
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown(
        _flat(f"""
        <div class="fade-up">
            <div class="kicker">{t('testi_kicker')}</div>
            <h2 class="section-title">{t('testi_title')}</h2>
        </div>
        """),
        unsafe_allow_html=True,
    )
    cols = st.columns(len(TESTIMONIALS))
    for col, t_ in zip(cols, TESTIMONIALS):
        txt = t_["text_es"] if lang == "es" else t_["text_en"]
        with col:
            st.markdown(
                _flat(f"""
                <div class="testi fade-up">
                    <div class="stars">{'★' * t_['rating']}</div>
                    <div class="txt">"{txt}"</div>
                    <div class="who">— {t_['name']}</div>
                </div>
                """),
                unsafe_allow_html=True,
            )
    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------
# Contact (hours + map + social)
# -----------------------------------------------------------------
DAY_KEYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def render_contact():
    lang = st.session_state.lang
    st.markdown('<div id="contact" class="section">', unsafe_allow_html=True)
    st.markdown(
        _flat(f"""
        <div class="fade-up">
            <div class="kicker">{t('contact_kicker')}</div>
            <h2 class="section-title">{t('contact_title')}</h2>
        </div>
        """),
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1, 1.2], gap="large")
    with col1:
        # Hours
        rows = ""
        for d in DAY_KEYS:
            hours = HOURS.get(d)
            label = t(f"day_{d}")
            val = f"{hours[0]} – {hours[1]}" if hours else t("closed")
            rows += f"<tr><td style='padding:.35rem 0;color:var(--text-dim);'>{label}</td><td style='text-align:right;font-weight:600;'>{val}</td></tr>"
        wa = _whatsapp_link("Hola!")
        addr = ADDRESS_ES if lang == "es" else ADDRESS_EN
        st.markdown(
            _flat(f"""
            <div style="padding:1.5rem; border-radius:20px; background:var(--card-bg); border:1px solid var(--line); backdrop-filter: blur(14px);">
                <h3 style="color:var(--gold); letter-spacing:2px;">{t('contact_hours')}</h3>
                <table style="width:100%; border-collapse:collapse;">{rows}</table>
                <div class="divider" style="margin:1.25rem 0;"></div>
                <h3 style="color:var(--gold); letter-spacing:2px;">{t('contact_where')}</h3>
                <p class="muted">📍 {addr}</p>
                <p class="muted">📱 <a style="color:var(--gold);text-decoration:none;" href="{wa}" target="_blank">{PHONE_DISPLAY}</a></p>
                <p class="muted">✉️ <a style="color:var(--gold);text-decoration:none;" href="mailto:{EMAIL}">{EMAIL}</a></p>
                <div class="divider" style="margin:1.25rem 0;"></div>
                <h3 style="color:var(--gold); letter-spacing:2px;">{t('contact_followus')}</h3>
                <div class="btn-row" style="margin-top:.75rem;">
                    <a class="btn ghost" href="{FACEBOOK}" target="_blank">Facebook</a>
                    <a class="btn ghost" href="{INSTAGRAM}" target="_blank">Instagram</a>
                    <a class="btn ghost" href="{TIKTOK}" target="_blank">TikTok</a>
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            f'<div class="map-wrap"><iframe src="{GOOGLE_MAPS_EMBED}" loading="lazy"></iframe></div>',
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)


# -----------------------------------------------------------------
# Footer
# -----------------------------------------------------------------
def render_footer():
    from datetime import datetime
    year = datetime.now().year
    st.markdown(
        _flat(f"""
        <div class="footer">
            <div>© {year} {BUSINESS_NAME}. {t('footer_rights')}</div>
            <div>{t('footer_made')} 💈</div>
        </div>
        """),
        unsafe_allow_html=True,
    )
