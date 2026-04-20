"""Spanish / English translations. Default language: ES."""
import streamlit as st

DEFAULT_LANG = "es"

TRANSLATIONS = {
    # --- Navigation ---
    "nav_home": {"es": "Inicio", "en": "Home"},
    "nav_services": {"es": "Servicios", "en": "Services"},
    "nav_gallery": {"es": "Galería", "en": "Gallery"},
    "nav_booking": {"es": "Reservar", "en": "Book"},
    "nav_about": {"es": "Nosotros", "en": "About"},
    "nav_market": {"es": "Mercado", "en": "Market"},
    "nav_contact": {"es": "Contacto", "en": "Contact"},

    # --- Hero ---
    "hero_badge": {"es": "💈 BARBERÍA PREMIUM EN QUITO", "en": "💈 PREMIUM BARBERSHOP IN QUITO"},
    "hero_title": {"es": "Más que un corte.\nUna experiencia.", "en": "More than a cut.\nAn experience."},
    "hero_sub": {
        "es": "Barberos expertos, ambiente único y el mejor servicio en el corazón de Quito. Reserva tu turno en 30 segundos.",
        "en": "Expert barbers, unique atmosphere, and top-tier service in the heart of Quito. Book your slot in 30 seconds.",
    },
    "cta_book": {"es": "Reservar turno", "en": "Book now"},
    "cta_whatsapp": {"es": "Escribir por WhatsApp", "en": "Message on WhatsApp"},

    # --- Metrics ---
    "m_clients": {"es": "Clientes felices", "en": "Happy clients"},
    "m_years": {"es": "Años cortando", "en": "Years of craft"},
    "m_rating": {"es": "Calificación Google", "en": "Google rating"},
    "m_barbers": {"es": "Barberos expertos", "en": "Expert barbers"},

    # --- Services ---
    "services_kicker": {"es": "NUESTROS SERVICIOS", "en": "OUR SERVICES"},
    "services_title": {"es": "Cortes, barbas y estilo", "en": "Cuts, beards & style"},
    "services_sub": {
        "es": "Cada servicio incluye consulta, lavado y detalles finales.",
        "en": "Every service includes consultation, wash and finishing touches.",
    },
    "svc_duration": {"es": "min", "en": "min"},
    "svc_book": {"es": "Reservar", "en": "Book"},

    # --- Gallery ---
    "gallery_kicker": {"es": "GALERÍA", "en": "GALLERY"},
    "gallery_title": {"es": "El trabajo habla por sí solo", "en": "The work speaks for itself"},

    # --- About ---
    "about_kicker": {"es": "NOSOTROS", "en": "ABOUT US"},
    "about_title": {"es": "Tradición con vibra moderna", "en": "Tradition with a modern vibe"},
    "about_body": {
        "es": "Los Barberos es un espacio donde se mezclan técnica, música y comunidad. Somos barberos apasionados por el oficio: cortes clásicos, fades de precisión, arreglo de barba con toalla caliente y el detalle que marca la diferencia. Pet friendly, café de cortesía y siempre la mejor playlist.",
        "en": "Los Barberos is a space where technique, music and community meet. We are barbers passionate about the craft: classic cuts, precision fades, hot-towel beard work and the details that make the difference. Pet friendly, complimentary coffee and always the best playlist.",
    },
    "about_values_title": {"es": "Lo que nos define", "en": "What defines us"},
    "values": {
        "es": ["Precisión técnica", "Ambiente pet friendly", "Higiene certificada", "Música y café", "Barberos certificados"],
        "en": ["Technical precision", "Pet-friendly space", "Certified hygiene", "Music & coffee", "Certified barbers"],
    },
    "team_title": {"es": "Nuestro equipo", "en": "Our team"},
    "years_exp": {"es": "años de experiencia", "en": "years of experience"},

    # --- Testimonials ---
    "testi_kicker": {"es": "OPINIONES", "en": "REVIEWS"},
    "testi_title": {"es": "Lo que dicen nuestros clientes", "en": "What our clients say"},

    # --- Booking ---
    "book_kicker": {"es": "RESERVAR TURNO", "en": "BOOK APPOINTMENT"},
    "book_title": {"es": "Agenda tu cita", "en": "Schedule your visit"},
    "book_sub": {
        "es": "Elige el servicio, fecha y hora. Recibirás confirmación por WhatsApp al instante.",
        "en": "Pick service, date and time. You'll get WhatsApp confirmation instantly.",
    },
    "f_service": {"es": "Servicio", "en": "Service"},
    "f_barber": {"es": "Barbero (opcional)", "en": "Barber (optional)"},
    "f_any_barber": {"es": "Cualquiera disponible", "en": "Any available"},
    "f_date": {"es": "Fecha", "en": "Date"},
    "f_time": {"es": "Hora", "en": "Time"},
    "f_name": {"es": "Tu nombre", "en": "Your name"},
    "f_phone": {"es": "Teléfono / WhatsApp", "en": "Phone / WhatsApp"},
    "f_notes": {"es": "Notas (opcional)", "en": "Notes (optional)"},
    "f_submit": {"es": "Confirmar por WhatsApp", "en": "Confirm via WhatsApp"},
    "f_success": {"es": "¡Reserva guardada! Toca el botón abajo para confirmar por WhatsApp.", "en": "Booking saved! Tap the button below to confirm on WhatsApp."},
    "f_whatsapp_cta": {"es": "Abrir WhatsApp", "en": "Open WhatsApp"},
    "f_required": {"es": "Por favor completa nombre y teléfono.", "en": "Please fill in name and phone."},
    "f_closed": {"es": "Cerrado ese día. Elige otra fecha.", "en": "Closed on that day. Pick another date."},
    "summary_title": {"es": "Resumen de tu reserva", "en": "Booking summary"},

    # --- Market ---
    "market_kicker": {"es": "ANÁLISIS DE MERCADO", "en": "MARKET ANALYSIS"},
    "market_title": {"es": "Oportunidad de crecimiento en Quito", "en": "Growth opportunity in Quito"},
    "market_sub": {
        "es": "Datos e insights para atraer más clientes a Los Barberos.",
        "en": "Data and insights to attract more customers to Los Barberos.",
    },

    # --- Contact ---
    "contact_kicker": {"es": "CONTACTO", "en": "CONTACT"},
    "contact_title": {"es": "Visítanos", "en": "Come visit us"},
    "contact_hours": {"es": "Horarios", "en": "Hours"},
    "contact_where": {"es": "Ubicación", "en": "Location"},
    "contact_followus": {"es": "Síguenos", "en": "Follow us"},
    "closed": {"es": "Cerrado", "en": "Closed"},

    # --- Days ---
    "day_mon": {"es": "Lunes", "en": "Monday"},
    "day_tue": {"es": "Martes", "en": "Tuesday"},
    "day_wed": {"es": "Miércoles", "en": "Wednesday"},
    "day_thu": {"es": "Jueves", "en": "Thursday"},
    "day_fri": {"es": "Viernes", "en": "Friday"},
    "day_sat": {"es": "Sábado", "en": "Saturday"},
    "day_sun": {"es": "Domingo", "en": "Sunday"},

    # --- Footer ---
    "footer_rights": {"es": "Todos los derechos reservados.", "en": "All rights reserved."},
    "footer_made": {"es": "Hecho con ♥ en Quito", "en": "Made with ♥ in Quito"},
}


def init_lang():
    if "lang" not in st.session_state:
        st.session_state.lang = DEFAULT_LANG


def t(key: str) -> str:
    """Translate a key for the current language."""
    init_lang()
    entry = TRANSLATIONS.get(key)
    if entry is None:
        return key
    return entry.get(st.session_state.lang, entry.get("es", key))


def tlist(key: str) -> list:
    init_lang()
    entry = TRANSLATIONS.get(key, {})
    return entry.get(st.session_state.lang, entry.get("es", []))


def set_lang(lang: str):
    if lang in ("es", "en"):
        st.session_state.lang = lang
