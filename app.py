"""
Los Barberos Quito — bilingual Streamlit website.

Run locally:
    pip install -r requirements.txt
    streamlit run app.py
"""
import streamlit as st
from streamlit_option_menu import option_menu

from components.i18n import init_lang, set_lang, t
from components.styles import inject_css, floating_whatsapp, init_theme, toggle_theme
from components.config import BUSINESS_NAME
from components.sections import (
    render_hero, render_services, render_gallery, render_about,
    render_testimonials, render_contact, render_footer,
)
from components.booking import render_booking


# ---- Page config ----
st.set_page_config(
    page_title=f"{BUSINESS_NAME} · Premium Barbershop",
    page_icon="💈",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        "Get Help": "https://www.facebook.com/LosBarberosQuito/",
        "About": f"{BUSINESS_NAME} · bilingual website powered by Streamlit.",
    },
)

init_lang()
init_theme()
inject_css(st.session_state.theme)


# ---- Navbar (brand + theme toggle + language buttons) ----
is_dark = st.session_state.theme == "dark"

nav_col_brand, nav_col_actions = st.columns([3, 1.25])
with nav_col_brand:
    st.markdown(
        """
        <div class="brand">
            <span class="brand-dot"></span>
            LOS <em>BARBEROS</em> · QUITO
        </div>
        """,
        unsafe_allow_html=True,
    )
with nav_col_actions:
    tcol, escol, encol = st.columns([1, 1, 1])
    with tcol:
        st.markdown('<div class="theme-toggle-wrap">', unsafe_allow_html=True)
        theme_icon = "🌙" if is_dark else "☀️"
        theme_help = "Switch to light mode" if is_dark else "Switch to dark mode"
        if st.button(theme_icon, key="theme_toggle_top", help=theme_help,
                     use_container_width=True):
            toggle_theme()
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    with escol:
        if st.button("ES", use_container_width=True, key="lang_es",
                     type="primary" if st.session_state.lang == "es" else "secondary"):
            set_lang("es")
            st.rerun()
    with encol:
        if st.button("EN", use_container_width=True, key="lang_en",
                     type="primary" if st.session_state.lang == "en" else "secondary"):
            set_lang("en")
            st.rerun()


# ---- Section menu ----
menu_keys = ["home", "services", "gallery", "booking", "about", "contact"]
menu_labels = [
    t("nav_home"), t("nav_services"), t("nav_gallery"),
    t("nav_booking"), t("nav_about"), t("nav_contact"),
]
icons = ["house", "scissors", "images", "calendar-check", "people", "geo-alt"]

menu_bg = "rgba(23,23,27,.65)" if is_dark else "rgba(255,255,255,.85)"
menu_link_color = "#B9B9C0" if is_dark else "#4A4A52"
menu_link_selected_color = "#0B0B0D"

selected = option_menu(
    menu_title=None,
    options=menu_labels,
    icons=icons,
    orientation="horizontal",
    default_index=0,
    styles={
        "container": {"background-color": menu_bg, "border-radius": "999px",
                      "padding": "6px", "border": "1px solid rgba(212,162,76,.25)"},
        "icon": {"color": "#D4A24C", "font-size": "16px"},
        "nav-link": {"font-size": "14px", "text-align": "center", "margin": "0px",
                     "color": menu_link_color, "--hover-color": "rgba(212,162,76,.12)",
                     "border-radius": "999px"},
        "nav-link-selected": {"background-color": "#D4A24C", "color": menu_link_selected_color,
                              "font-weight": "700"},
    },
)
selected_key = menu_keys[menu_labels.index(selected)]


# ---- Route ----
if selected_key == "home":
    render_hero()
    render_services()
    render_gallery()
    render_booking()
    render_testimonials()
elif selected_key == "services":
    render_services()
elif selected_key == "gallery":
    render_gallery()
elif selected_key == "booking":
    render_booking()
elif selected_key == "about":
    render_about()
    render_testimonials()
elif selected_key == "contact":
    render_contact()


# ---- Footer + floating WhatsApp ----
render_footer()
floating_whatsapp(
    "Hola! Quisiera reservar un turno en Los Barberos."
    if st.session_state.lang == "es"
    else "Hi! I'd like to book a slot at Los Barberos."
)
