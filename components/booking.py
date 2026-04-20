"""Booking form with calendar, time-slot picker, SQLite persistence and WhatsApp handoff."""
import os
import sqlite3
from datetime import date, datetime, timedelta
from urllib.parse import quote

import streamlit as st


def _flat(html: str) -> str:
    return "\n".join(line.lstrip() for line in html.splitlines())

from components.i18n import t
from components.config import (
    SERVICES, BARBERS, HOURS, WHATSAPP_NUMBER,
    SLOT_MINUTES, OPEN_HOUR, CLOSE_HOUR,
)

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "bookings.db")
DAY_KEYS = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]


def _init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    with sqlite3.connect(DB_PATH) as con:
        con.execute(
            """
            CREATE TABLE IF NOT EXISTS bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL,
                name TEXT NOT NULL,
                phone TEXT NOT NULL,
                service_key TEXT NOT NULL,
                barber TEXT,
                appt_date TEXT NOT NULL,
                appt_time TEXT NOT NULL,
                notes TEXT
            )
            """
        )


def _save(name, phone, service_key, barber, appt_date, appt_time, notes):
    _init_db()
    with sqlite3.connect(DB_PATH) as con:
        con.execute(
            """INSERT INTO bookings (created_at, name, phone, service_key, barber, appt_date, appt_time, notes)
               VALUES (?,?,?,?,?,?,?,?)""",
            (
                datetime.now().isoformat(timespec="seconds"),
                name, phone, service_key, barber,
                appt_date.isoformat(), appt_time, notes,
            ),
        )


def _slots_for(d: date):
    key = DAY_KEYS[d.weekday()]
    hours = HOURS.get(key)
    if not hours:
        return []
    open_h, close_h = hours
    oh, om = [int(x) for x in open_h.split(":")]
    ch, cm = [int(x) for x in close_h.split(":")]
    start = datetime(d.year, d.month, d.day, oh, om)
    end = datetime(d.year, d.month, d.day, ch, cm)
    out, cur = [], start
    while cur + timedelta(minutes=SLOT_MINUTES) <= end:
        out.append(cur.strftime("%H:%M"))
        cur += timedelta(minutes=SLOT_MINUTES)
    # If booking for today, drop past slots
    if d == date.today():
        now = datetime.now().strftime("%H:%M")
        out = [s for s in out if s > now]
    return out


def render_booking():
    lang = st.session_state.lang
    st.markdown('<div id="booking" class="section">', unsafe_allow_html=True)
    st.markdown(
        _flat(f"""
        <div class="fade-up">
            <div class="kicker"><span class="sec-num">03</span>{t('book_kicker')}</div>
            <h2 class="section-title">{t('book_title')}</h2>
            <p class="muted">{t('book_sub')}</p>
        </div>
        """),
        unsafe_allow_html=True,
    )

    col_form, col_summary = st.columns([1.2, 1], gap="large")

    with col_form:
        # Service dropdown
        service_labels = [
            f"{s['icon']}  {s['name_es'] if lang=='es' else s['name_en']} — ${s['price']} · {s['duration']}{t('svc_duration')}"
            for s in SERVICES
        ]
        svc_idx = st.selectbox(t("f_service"), range(len(SERVICES)),
                               format_func=lambda i: service_labels[i])
        service = SERVICES[svc_idx]

        # Barber dropdown
        barber_options = [t("f_any_barber")] + [b["name"] for b in BARBERS]
        barber = st.selectbox(t("f_barber"), barber_options)

        # Date picker
        today = date.today()
        appt_date = st.date_input(
            t("f_date"),
            value=today,
            min_value=today,
            max_value=today + timedelta(days=60),
        )

        slots = _slots_for(appt_date)
        if not slots:
            st.warning(t("f_closed"))
            appt_time = None
        else:
            appt_time = st.selectbox(t("f_time"), slots)

        c1, c2 = st.columns(2)
        with c1:
            name = st.text_input(t("f_name"))
        with c2:
            phone = st.text_input(t("f_phone"), placeholder="+593 ...")
        notes = st.text_area(t("f_notes"), height=80)

        submit = st.button(t("f_submit"), use_container_width=True, disabled=appt_time is None, type="primary")

    with col_summary:
        svc_name = service["name_es"] if lang == "es" else service["name_en"]
        st.markdown(
            _flat(f"""
            <div class="contact-card fade-up" style="position:sticky; top:1rem;">
                <h3>{t('summary_title')}</h3>
                <table class="hours-table" style="margin-top:.75rem;">
                    <tr><td>{t('f_service')}</td><td>{service['icon']} {svc_name}</td></tr>
                    <tr><td>{t('f_barber')}</td><td>{barber}</td></tr>
                    <tr><td>{t('f_date')}</td><td>{appt_date}</td></tr>
                    <tr><td>{t('f_time')}</td><td>{appt_time or '—'}</td></tr>
                </table>
                <div class="divider" style="margin:1.25rem 0;"></div>
                <div style="display:flex; justify-content:space-between; align-items:baseline;">
                    <span style="font-family:'JetBrains Mono', monospace; font-size:.72rem; letter-spacing:.15em; text-transform:uppercase; color:var(--muted);">Total</span>
                    <span style="font-family:'Fraunces', serif; font-style:italic; font-weight:300; font-size:2.5rem; color:var(--accent);">${service['price']}</span>
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

    if submit:
        if not name.strip() or not phone.strip():
            st.error(t("f_required"))
            return
        try:
            _save(name.strip(), phone.strip(), service["key"], barber,
                  appt_date, appt_time, notes.strip())
        except Exception as e:
            st.warning(f"DB warning: {e}")  # non-fatal

        svc_name = service["name_es"] if lang == "es" else service["name_en"]
        msg_es = (
            f"Hola! Soy {name}. Quiero confirmar mi reserva:\n"
            f"• Servicio: {svc_name} (${service['price']})\n"
            f"• Barbero: {barber}\n"
            f"• Fecha: {appt_date}\n"
            f"• Hora: {appt_time}\n"
            f"{('• Notas: ' + notes) if notes.strip() else ''}"
        )
        msg_en = (
            f"Hi! I'm {name}. I'd like to confirm my booking:\n"
            f"• Service: {svc_name} (${service['price']})\n"
            f"• Barber: {barber}\n"
            f"• Date: {appt_date}\n"
            f"• Time: {appt_time}\n"
            f"{('• Notes: ' + notes) if notes.strip() else ''}"
        )
        message = msg_es if lang == "es" else msg_en
        wa_url = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"

        st.success(t("f_success"))
        st.markdown(
            _flat(f"""
            <a href="{wa_url}" target="_blank" class="btn wa" style="margin-top:1rem;">
                💬 {t('f_whatsapp_cta')}
            </a>
            """),
            unsafe_allow_html=True,
        )
        st.balloons()

    st.markdown('</div>', unsafe_allow_html=True)
