"""
Global configuration for Los Barberos Quito website.

EDIT THIS FILE to replace placeholders with real business info.
All values marked with `# TODO` should be updated before going live.
"""

# ---- Business identity ----
BUSINESS_NAME = "Los Barberos Quito"
TAGLINE_ES = "Barbería premium en Quito · Estilo, precisión y comunidad"
TAGLINE_EN = "Premium barbershop in Quito · Style, precision & community"

# ---- Contact ----
WHATSAPP_NUMBER = "593999273444"
PHONE_DISPLAY = "+593 99 927 3444"
EMAIL = "hola@losbarberosquito.com"  # TODO

# ---- Location ----
# TODO: replace with real address
ADDRESS_ES = "Quito, Ecuador"
ADDRESS_EN = "Quito, Ecuador"
GOOGLE_MAPS_EMBED = (
    # Default: Quito city center. Replace with a real Google Maps embed src.
    "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d15949.07!2d-78.48!3d-0.18!"
    "2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMMKwMTAnNDguMCJTIDc4wrAyOCc0OC4wIlc!5e0"
)

# ---- Social ----
FACEBOOK = "https://www.facebook.com/LosBarberosQuito/"
INSTAGRAM = "https://www.instagram.com/losbarberosquito/"
TIKTOK = "https://www.tiktok.com/@losbarberosquito"  # TODO verify

# ---- Hours ----
# 7-day schedule (24h). Use None for closed.
HOURS = {
    "mon": ("10:00", "20:00"),
    "tue": ("10:00", "20:00"),
    "wed": ("10:00", "20:00"),
    "thu": ("10:00", "20:00"),
    "fri": ("10:00", "21:00"),
    "sat": ("09:00", "20:00"),
    "sun": None,
}

# ---- Services & pricing (USD — Ecuador uses USD) ----
SERVICES = [
    {
        "key": "classic_cut",
        "name_es": "Corte Clásico",
        "name_en": "Classic Haircut",
        "duration": 40,
        "price": 12,
        "desc_es": "Corte con tijera y máquina, lavado y peinado incluidos.",
        "desc_en": "Scissor + clipper cut, wash and styling included.",
        "icon": "✂️",
    },
    {
        "key": "fade",
        "name_es": "Fade / Degradado",
        "name_en": "Fade",
        "duration": 50,
        "price": 15,
        "desc_es": "Degradado de precisión con transiciones suaves.",
        "desc_en": "Precision fade with smooth blending.",
        "icon": "💈",
    },
    {
        "key": "beard",
        "name_es": "Arreglo de Barba",
        "name_en": "Beard Trim",
        "duration": 30,
        "price": 10,
        "desc_es": "Perfilado y contorno con toalla caliente y aceite.",
        "desc_en": "Shaping and contouring with hot towel and oil.",
        "icon": "🧔",
    },
    {
        "key": "combo",
        "name_es": "Combo Corte + Barba",
        "name_en": "Haircut + Beard Combo",
        "duration": 70,
        "price": 22,
        "desc_es": "Nuestra experiencia completa. Cuidado total en una sola visita.",
        "desc_en": "Our full experience. Complete grooming in a single visit.",
        "icon": "🔥",
    },
    {
        "key": "kids",
        "name_es": "Corte Infantil",
        "name_en": "Kids' Haircut",
        "duration": 30,
        "price": 10,
        "desc_es": "Corte para menores de 12 años con juegos y atención especial.",
        "desc_en": "Cut for children under 12 with a kid-friendly touch.",
        "icon": "👦",
    },
    {
        "key": "design",
        "name_es": "Diseño / Line-Up",
        "name_en": "Hair Design / Line-Up",
        "duration": 20,
        "price": 8,
        "desc_es": "Líneas, diseños personalizados y line-up de precisión.",
        "desc_en": "Lines, custom designs and precision line-ups.",
        "icon": "✨",
    },
]

# ---- Barbers ----
BARBERS = [
    {"name": "Carlos M.", "role_es": "Master Barber · Fundador", "role_en": "Master Barber · Founder", "years": 12, "img": "https://images.unsplash.com/photo-1621605815971-fbc98d665033?w=600"},
    {"name": "Andrés P.", "role_es": "Especialista en Fade", "role_en": "Fade Specialist", "years": 7, "img": "https://images.unsplash.com/photo-1599351431202-1e0f0137899a?w=600"},
    {"name": "Mateo R.", "role_es": "Diseño y Barba", "role_en": "Design & Beard Pro", "years": 5, "img": "https://images.unsplash.com/photo-1584316712724-f5d4b188fee2?w=600"},
]

# ---- Time slots for booking ----
SLOT_MINUTES = 30
OPEN_HOUR = 10
CLOSE_HOUR = 20

# ---- Gallery images (Unsplash free) ----
GALLERY = [
    "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?w=900",
    "https://images.unsplash.com/photo-1562004760-aceed7bb0fe3?w=900",
    "https://images.unsplash.com/photo-1622296089863-eb7fc530daa8?w=900",
    "https://images.unsplash.com/photo-1517832606299-7ae9b720a186?w=900",
    "https://images.unsplash.com/photo-1605497788044-5a32c7078486?w=900",
    "https://images.unsplash.com/photo-1635273051839-003bf06a8751?w=900",
    "https://images.unsplash.com/photo-1599351431202-1e0f0137899a?w=900",
    "https://images.unsplash.com/photo-1521322714240-ee1d383eab62?w=900",
]

# ---- Testimonials ----
TESTIMONIALS = [
    {"name": "Javier L.", "text_es": "El mejor fade de Quito, sin exagerar. Ambiente top.", "text_en": "The best fade in Quito, no exaggeration. Top vibes.", "rating": 5},
    {"name": "Andrea V.", "text_es": "Llevé a mi esposo y salió feliz. Atención 10/10.", "text_en": "Brought my husband and he left happy. 10/10 service.", "rating": 5},
    {"name": "Luis T.", "text_es": "Música, cerveza y un corte perfecto. Vuelvo siempre.", "text_en": "Music, beer and a perfect cut. I keep coming back.", "rating": 5},
    {"name": "Camila R.", "text_es": "Pet friendly y muy profesional. Recomendado 100%.", "text_en": "Pet friendly and very professional. 100% recommended.", "rating": 5},
]
