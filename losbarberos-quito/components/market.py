"""Market analysis page with interactive Plotly charts + growth-strategy playbook."""
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

from components.i18n import t

def _plotly_theme():
    """Theme-aware Plotly layout dict — pulls palette from st.session_state.theme."""
    is_dark = st.session_state.get("theme", "dark") == "dark"
    text_color = "#F5F5F5" if is_dark else "#1A1A1F"
    grid_color = "rgba(255,255,255,.08)" if is_dark else "rgba(0,0,0,.08)"
    return dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color=text_color, family="Inter"),
        colorway=["#D4A24C", "#E8C070", "#C0904A", "#8B6A32", "#4D3C1D"],
        margin=dict(l=10, r=10, t=30, b=10),
        legend=dict(bgcolor="rgba(0,0,0,0)"),
        xaxis=dict(gridcolor=grid_color, zerolinecolor=grid_color),
        yaxis=dict(gridcolor=grid_color, zerolinecolor=grid_color),
    )


# Back-compat alias: keep PLOTLY_THEME name but resolve at call-time via a lazy dict.
PLOTLY_THEME = _plotly_theme  # noqa: N816  (callable, see usage)


def _flat(html: str) -> str:
    return "\n".join(line.lstrip() for line in html.splitlines())


def _card(body_html):
    st.markdown(
        _flat(
            f'<div style="padding:1.25rem; border-radius:20px; background:var(--card-bg); '
            f'border:1px solid var(--line); backdrop-filter: blur(14px);">{body_html}</div>'
        ),
        unsafe_allow_html=True,
    )


def render_market():
    lang = st.session_state.lang
    st.markdown('<div id="market" class="section">', unsafe_allow_html=True)
    st.markdown(
        _flat(f"""
        <div class="fade-up">
            <div class="kicker">{t('market_kicker')}</div>
            <h2 class="section-title">{t('market_title')}</h2>
            <p class="muted">{t('market_sub')}</p>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # --- Headline metrics ---
    m1, m2, m3, m4 = st.columns(4)
    metrics = [
        ("$26.7B", "Global barber market 2026", "4.8% CAGR 2021-26"),
        ("4.2★",  "Promedio Quito (883 reseñas)" if lang == "es" else "Quito avg rating (883 reviews)",
                  "Google Maps"),
        ("+68%",  "Gasto grooming masculino 2020-26" if lang == "es" else "Male grooming spend 2020-26",
                  "LATAM"),
        ("75%",   "Clientes reservan por WhatsApp" if lang == "es" else "Clients book via WhatsApp",
                  "Ecuador SMB survey"),
    ]
    for col, (big, lbl, sub) in zip([m1, m2, m3, m4], metrics):
        with col:
            st.markdown(
                _flat(f"""
                <div class="metric">
                    <div class="num">{big}</div>
                    <div class="lbl">{lbl}</div>
                    <div style="color:var(--text-dim);font-size:.75rem;margin-top:.25rem;">{sub}</div>
                </div>
                """),
                unsafe_allow_html=True,
            )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # --- Growth projection ---
    col1, col2 = st.columns(2, gap="large")
    with col1:
        years = list(range(2021, 2027))
        values = [19.5, 20.7, 22.0, 23.4, 25.0, 26.7]  # $B global
        df = pd.DataFrame({"Year": years, "USD (B)": values})
        fig = px.area(df, x="Year", y="USD (B)",
                      title="Global barbershop market size ($B)" if lang == "en"
                      else "Tamaño del mercado global (mmUSD)")
        fig.update_traces(line_color="#D4A24C", fillcolor="rgba(212,162,76,.25)")
        fig.update_layout(**_plotly_theme())
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Quito competitor landscape
        competitors = pd.DataFrame({
            "Barbershop": ["The Barber Club", "Razors Edge", "Barber House Cumbaya",
                           "755 Barber Studio", "Ace Barber", "El Bigotte",
                           "Urban Barber 593", "Los Barberos Quito"],
            "Rating": [4.2, 4.6, 4.9, 4.9, 4.8, 4.9, 4.85, 4.7],
            "Reviews": [139, 105, 94, 168, 231, 20, 55, 70],
        })
        fig2 = px.scatter(
            competitors, x="Reviews", y="Rating", text="Barbershop", size="Reviews",
            title=("Competitive landscape — Quito" if lang == "en"
                   else "Paisaje competitivo — Quito"),
            size_max=40,
        )
        fig2.update_traces(textposition="top center",
                           marker=dict(color="#D4A24C", line=dict(color="#E8C070", width=1)))
        _theme = _plotly_theme()
        _theme["yaxis"] = dict(range=[4.0, 5.05], gridcolor=_theme["yaxis"]["gridcolor"])
        fig2.update_layout(**_theme)
        st.plotly_chart(fig2, use_container_width=True)

    # --- Target customer personas ---
    st.markdown('<h3 class="section-title" style="margin-top:2.5rem;">'
                + ("Target customer personas" if lang == "en" else "Personas objetivo")
                + '</h3>', unsafe_allow_html=True)

    personas = [
        {
            "emoji": "💼",
            "name_es": "El Profesional (25-40)", "name_en": "The Professional (25-40)",
            "need_es": "Cortes ejecutivos recurrentes, puntualidad, reserva fácil.",
            "need_en": "Recurring executive cuts, punctuality, easy booking.",
            "channel": "LinkedIn Ads · Google local · WhatsApp",
        },
        {
            "emoji": "🎨",
            "name_es": "El Creativo (18-28)", "name_en": "The Creative (18-28)",
            "need_es": "Fades, diseños, line-ups, fotos para IG.",
            "need_en": "Fades, designs, line-ups, IG-worthy photos.",
            "channel": "Instagram Reels · TikTok · Referidos",
        },
        {
            "emoji": "👨‍👦",
            "name_es": "Papá e hijo", "name_en": "Father & son",
            "need_es": "Experiencia familiar, ambiente amigable.",
            "need_en": "Family experience, kid-friendly vibe.",
            "channel": "Facebook · Grupos de colegios",
        },
        {
            "emoji": "✈️",
            "name_es": "Expats / turistas", "name_en": "Expats / tourists",
            "need_es": "Barbería con inglés, pagos con tarjeta, Google Maps.",
            "need_en": "English-speaking, card payments, Google Maps presence.",
            "channel": "TripAdvisor · Google · Airbnb guides",
        },
    ]
    cols = st.columns(4)
    for col, p in zip(cols, personas):
        name = p["name_es"] if lang == "es" else p["name_en"]
        need = p["need_es"] if lang == "es" else p["need_en"]
        with col:
            _card(
                f"""
                <div style="font-size:2rem">{p['emoji']}</div>
                <div style="font-family:'Bebas Neue';font-size:1.35rem;letter-spacing:1px;">{name}</div>
                <div style="color:var(--text-dim); font-size:.9rem; margin-top:.4rem;">{need}</div>
                <div style="margin-top:.75rem; color:var(--gold); font-size:.78rem; letter-spacing:.15em;">
                    {p['channel']}
                </div>
                """
            )

    # --- SWOT ---
    st.markdown('<h3 class="section-title" style="margin-top:2.5rem;">SWOT</h3>',
                unsafe_allow_html=True)
    swot = {
        "S": ("Strengths" if lang == "en" else "Fortalezas",
              ["10+ years in Quito" if lang == "en" else "10+ años en Quito",
               "Pet-friendly differentiation",
               "Music & community vibe" if lang == "en" else "Ambiente de comunidad",
               "Active social media presence" if lang == "en" else "Presencia activa en redes"]),
        "W": ("Weaknesses" if lang == "en" else "Debilidades",
              ["Limited online booking" if lang == "en" else "Reservas online limitadas",
               "No bilingual website yet" if lang == "en" else "Sin sitio bilingüe aún",
               "Price opacity" if lang == "en" else "Precios no publicados",
               "No loyalty program" if lang == "en" else "Sin programa de lealtad"]),
        "O": ("Opportunities" if lang == "en" else "Oportunidades",
              ["Grooming spend growing +68%" if lang == "en" else "Gasto grooming +68%",
               "WhatsApp Business API automation",
               "Corporate partnerships (offices)" if lang == "en" else "Convenios corporativos",
               "Retail: beard oils, pomades"]),
        "T": ("Threats" if lang == "en" else "Amenazas",
              ["8+ premium competitors" if lang == "en" else "8+ competidores premium",
               "Fresha / Booksy entering LATAM",
               "Economic downturns",
               "Barber talent churn"]),
    }
    c = st.columns(4)
    colors = ["#4ADE80", "#F97316", "#60A5FA", "#F43F5E"]
    for col, (k, (title, items)), color in zip(c, swot.items(), colors):
        with col:
            bullet_html = "".join(f"<li style='margin:.3rem 0;'>{i}</li>" for i in items)
            _card(
                f"""
                <div style="color:{color}; font-weight:700; letter-spacing:.2em; font-size:.75rem;">{k} · {title.upper()}</div>
                <ul style="margin-top:.5rem; padding-left:1rem; color:var(--text-dim); font-size:.92rem;">{bullet_html}</ul>
                """
            )

    # --- Growth playbook ---
    st.markdown('<h3 class="section-title" style="margin-top:2.5rem;">'
                + ("90-day growth playbook" if lang == "en" else "Plan de crecimiento a 90 días")
                + '</h3>', unsafe_allow_html=True)

    plays = [
        {"when": "Day 0-15", "title_es": "Captura digital", "title_en": "Digital capture",
         "body_es": "Lanzar este sitio, activar Google Business, publicar precios y horarios, activar WhatsApp Business con catálogo.",
         "body_en": "Launch this site, activate Google Business, publish prices & hours, enable WhatsApp Business with catalog."},
        {"when": "Day 15-30", "title_es": "Contenido viral", "title_en": "Viral content",
         "body_es": "3 Reels/semana: antes-después, time-lapse fades, retos con clientes. Colabs con micro-influencers locales.",
         "body_en": "3 Reels/week: before-after, time-lapse fades, challenges with clients. Collabs with local micro-influencers."},
        {"when": "Day 30-60", "title_es": "Lealtad & referidos", "title_en": "Loyalty & referrals",
         "body_es": "Programa 5+1 (6º corte gratis). Código de referido: amigo recibe 20% off, tú $5 de crédito.",
         "body_en": "5+1 punch card (6th cut free). Referral code: friend gets 20% off, you get $5 credit."},
        {"when": "Day 60-90", "title_es": "Alianzas B2B", "title_en": "B2B partnerships",
         "body_es": "Convenios con 5 oficinas/coworkings en Cumbayá, González Suárez, La Carolina. Barber-in-office 1x/mes.",
         "body_en": "Partnerships with 5 offices/coworkings in Cumbayá, González Suárez, La Carolina. Barber-in-office 1x/month."},
        {"when": "Day 60-90", "title_es": "Upsell de retail", "title_en": "Retail upsell",
         "body_es": "Pomadas, aceites, kits de barba con la marca. Margen 50-70%. Mostrador visible + showcase IG.",
         "body_en": "Pomades, oils, branded beard kits. 50-70% margin. Visible counter + IG showcase."},
        {"when": "Ongoing", "title_es": "Automatización", "title_en": "Automation",
         "body_es": "Recordatorios WhatsApp 24h antes. Reactivación automática de clientes inactivos (>45 días).",
         "body_en": "WhatsApp reminders 24h before. Auto-reactivation of dormant clients (>45 days)."},
    ]
    cols = st.columns(3)
    for i, p in enumerate(plays):
        with cols[i % 3]:
            title = p["title_es"] if lang == "es" else p["title_en"]
            body = p["body_es"] if lang == "es" else p["body_en"]
            _card(
                f"""
                <div style="color:var(--gold); font-size:.75rem; letter-spacing:.2em;">{p['when']}</div>
                <div style="font-family:'Bebas Neue';font-size:1.4rem;letter-spacing:1px;margin:.3rem 0;">{title}</div>
                <div style="color:var(--text-dim); font-size:.92rem; line-height:1.5;">{body}</div>
                """
            )

    # --- Channel mix recommendation ---
    st.markdown('<h3 class="section-title" style="margin-top:2.5rem;">'
                + ("Recommended channel mix" if lang == "en" else "Mix de canales recomendado")
                + '</h3>', unsafe_allow_html=True)
    channel_df = pd.DataFrame({
        "Channel": ["Instagram/TikTok", "WhatsApp Business", "Google Maps / SEO",
                    "Referral program", "Google Ads (local)", "Corporate B2B"],
        "Budget %": [28, 10, 12, 15, 20, 15],
        "Expected CAC $": [6.5, 2.0, 4.5, 3.8, 9.0, 7.0],
    })
    fig3 = go.Figure()
    fig3.add_trace(go.Bar(
        x=channel_df["Channel"], y=channel_df["Budget %"],
        name="Budget %", marker_color="#D4A24C",
    ))
    fig3.add_trace(go.Scatter(
        x=channel_df["Channel"], y=channel_df["Expected CAC $"],
        name="Expected CAC ($)", mode="lines+markers",
        line=dict(color="#E8C070", width=3), yaxis="y2",
    ))
    _theme = _plotly_theme()
    _theme["yaxis"] = dict(title="Budget %", gridcolor=_theme["yaxis"]["gridcolor"])
    _theme["legend"] = dict(orientation="h", y=1.15, bgcolor="rgba(0,0,0,0)")
    _theme["yaxis2"] = dict(title="CAC $", overlaying="y", side="right")
    fig3.update_layout(**_theme)
    st.plotly_chart(fig3, use_container_width=True)

    st.markdown('</div>', unsafe_allow_html=True)
