import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit_antd_components as sac
import base64

# ── Page Config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="RideRepublic Analytics", page_icon="riderepublic_logo.png", layout="wide")

# ── Logo Helper ───────────────────────────────────────────────────────────────
def get_logo_base64(path="riderepublic_logo.png"):
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    except:
        return None

logo_b64 = get_logo_base64()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    mode = sac.switch(label='Theme', align='start', size='md', on_label='🌙', off_label='☀️')
    st.markdown("<hr style='border-color: rgba(128,128,128,0.2);'>", unsafe_allow_html=True)
    if st.button("⬅️ Back to Home"):
        st.switch_page("app.py")

# ── Theme Colors ──────────────────────────────────────────────────────────────
DARK_BG    = "#0A0A0F"
DARK_CARD  = "#13131A"
DARK_BORDER= "#2A2A3A"
ACCENT     = "#E8B84B"
LIGHT_BG   = "#F4F1EC"
LIGHT_CARD = "#FFFFFF"
LIGHT_BORDER = "#E0D9CF"

if mode:
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
    html, body, [class*="css"] {{ font-family: 'DM Sans', sans-serif; }}
    .stApp {{
        background-color: {DARK_BG};
        background-image: radial-gradient(ellipse at 80% 0%, rgba(232,184,75,0.06) 0%, transparent 60%);
        color: #E8E8F0;
    }}
    section[data-testid="stSidebar"] {{
        background-color: {DARK_CARD} !important;
        border-right: 1px solid {DARK_BORDER} !important;
    }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}
    div.stButton > button {{
        background: linear-gradient(135deg, {ACCENT} 0%, #D4A43A 100%) !important;
        color: #0A0A0F !important;
        border: none !important;
        border-radius: 12px !important;
        font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important;
        width: 100% !important;
        box-shadow: 0 4px 20px rgba(232,184,75,0.3) !important;
    }}
    .hero-section {{
        background: linear-gradient(135deg, {DARK_CARD} 0%, #1A1A2E 100%);
        border: 1px solid {DARK_BORDER};
        border-radius: 24px;
        padding: 2rem 2.5rem;
        margin-bottom: 2rem;
    }}
    .hero-title {{
        font-family: 'Syne', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: #FFFFFF;
        margin: 0;
        letter-spacing: -0.5px;
    }}
    .hero-accent {{ color: {ACCENT}; }}
    .hero-sub {{ font-size: 0.95rem; color: #8888AA; margin-top: 0.3rem; }}
    .hero-badge {{
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(232,184,75,0.12); border: 1px solid rgba(232,184,75,0.3);
        color: {ACCENT}; border-radius: 50px; padding: 4px 14px;
        font-size: 0.75rem; font-weight: 600; letter-spacing: 0.5px; margin-bottom: 0.8rem;
    }}
    .stat-card {{
        background: {DARK_CARD};
        border: 1px solid {DARK_BORDER};
        border-radius: 16px;
        padding: 1.3rem 1.5rem;
        text-align: center;
        transition: border-color 0.2s;
    }}
    .stat-card:hover {{ border-color: {ACCENT}; }}
    .stat-value {{
        font-family: 'Syne', sans-serif;
        font-size: 1.8rem; font-weight: 800; color: {ACCENT};
    }}
    .stat-label {{
        font-size: 0.75rem; color: #8888AA;
        text-transform: uppercase; letter-spacing: 0.8px; margin-top: 3px;
    }}
    .section-header {{
        font-family: 'Syne', sans-serif;
        font-size: 1.2rem; font-weight: 700; color: #FFFFFF;
        margin: 1.5rem 0 0.8rem 0;
        display: flex; align-items: center; gap: 10px;
    }}
    .section-header::after {{
        content: ''; flex: 1; height: 1px;
        background: linear-gradient(90deg, {DARK_BORDER}, transparent);
    }}
    .perf-card {{
        background: {DARK_CARD};
        border: 1px solid {DARK_BORDER};
        border-radius: 20px;
        padding: 2rem;
    }}
    [data-testid="stMetricValue"] {{ color: {ACCENT} !important; font-family: 'Syne', sans-serif !important; font-size: 1.6rem !important; }}
    [data-testid="stMetricLabel"] {{ color: #8888AA !important; font-size: 0.8rem !important; }}
    .footer-bar {{
        background: {DARK_CARD}; border-top: 1px solid {DARK_BORDER};
        border-radius: 16px; padding: 1rem 2rem;
        text-align: center; color: #555570; font-size: 0.8rem; margin-top: 2rem;
    }}
    </style>
    """, unsafe_allow_html=True)
else:
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');
    html, body, [class*="css"] {{ font-family: 'DM Sans', sans-serif; }}
    .stApp {{
        background-color: {LIGHT_BG};
        color: #1A1A2E;
    }}
    section[data-testid="stSidebar"] {{
        background-color: {LIGHT_CARD} !important;
        border-right: 1px solid {LIGHT_BORDER} !important;
    }}
    [data-testid="stSidebarNav"] {{ display: none !important; }}
    div.stButton > button {{
        background: linear-gradient(135deg, #1A1A2E 0%, #2A2A4E 100%) !important;
        color: white !important; border: none !important;
        border-radius: 12px !important; font-family: 'Syne', sans-serif !important;
        font-weight: 700 !important; width: 100% !important;
    }}
    .hero-section {{
        background: linear-gradient(135deg, #1A1A2E 0%, #2D2D5E 100%);
        border-radius: 24px; padding: 2rem 2.5rem; margin-bottom: 2rem;
    }}
    .hero-title {{
        font-family: 'Syne', sans-serif; font-size: 2.2rem;
        font-weight: 800; color: #FFFFFF; margin: 0; letter-spacing: -0.5px;
    }}
    .hero-accent {{ color: {ACCENT}; }}
    .hero-sub {{ font-size: 0.95rem; color: rgba(255,255,255,0.55); margin-top: 0.3rem; }}
    .hero-badge {{
        display: inline-flex; align-items: center; gap: 6px;
        background: rgba(232,184,75,0.15); border: 1px solid rgba(232,184,75,0.4);
        color: {ACCENT}; border-radius: 50px; padding: 4px 14px;
        font-size: 0.75rem; font-weight: 600; letter-spacing: 0.5px; margin-bottom: 0.8rem;
    }}
    .stat-card {{
        background: {LIGHT_CARD}; border: 1px solid {LIGHT_BORDER};
        border-radius: 16px; padding: 1.3rem 1.5rem; text-align: center;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06); transition: all 0.2s;
    }}
    .stat-card:hover {{ border-color: #1A1A2E; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
    .stat-value {{ font-family: 'Syne', sans-serif; font-size: 1.8rem; font-weight: 800; color: #1A1A2E; }}
    .stat-label {{ font-size: 0.75rem; color: #888; text-transform: uppercase; letter-spacing: 0.8px; margin-top: 3px; }}
    .section-header {{
        font-family: 'Syne', sans-serif; font-size: 1.2rem; font-weight: 700; color: #1A1A2E;
        margin: 1.5rem 0 0.8rem 0; display: flex; align-items: center; gap: 10px;
    }}
    .section-header::after {{
        content: ''; flex: 1; height: 1px;
        background: linear-gradient(90deg, {LIGHT_BORDER}, transparent);
    }}
    .perf-card {{
        background: {LIGHT_CARD}; border: 1px solid {LIGHT_BORDER};
        border-radius: 20px; padding: 2rem;
        box-shadow: 0 2px 12px rgba(0,0,0,0.06);
    }}
    [data-testid="stMetricValue"] {{ color: #1A1A2E !important; font-family: 'Syne', sans-serif !important; font-size: 1.6rem !important; }}
    [data-testid="stMetricLabel"] {{ color: #888 !important; font-size: 0.8rem !important; }}
    .footer-bar {{
        background: {LIGHT_CARD}; border: 1px solid {LIGHT_BORDER};
        border-radius: 16px; padding: 1rem 2rem;
        text-align: center; color: #AAA; font-size: 0.8rem; margin-top: 2rem;
    }}
    </style>
    """, unsafe_allow_html=True)

# ── Hero ──────────────────────────────────────────────────────────────────────
logo_html = f'<img src="data:image/png;base64,{logo_b64}" style="width:56px;height:56px;border-radius:50%;object-fit:cover;" />' if logo_b64 else "📊"

st.markdown(f"""
<div class="hero-section">
    <div style="display:flex; align-items:center; gap:18px;">
        <div>{logo_html}</div>
        <div>
            <div class="hero-badge">✦ DATA INSIGHTS</div>
            <h1 class="hero-title">Ride<span class="hero-accent">Republic</span> Analytics</h1>
            <p class="hero-sub">Dataset insights, distribution analysis & model performance</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── Load Data ─────────────────────────────────────────────────────────────────
df = pd.read_csv('cleaned_car_datas.csv')
df['price_lakh'] = df['selling_price'] / 100000

chart_bg   = 'rgba(0,0,0,0)'
grid_color = 'rgba(128,128,128,0.1)'
font_color = '#888888' if mode else '#555555'
text_color = '#FFFFFF' if mode else '#1A1A2E'

def styled_layout(fig, title=""):
    fig.update_layout(
        title=dict(text=title, font=dict(family='Syne', size=15, color=text_color)),
        paper_bgcolor=chart_bg, plot_bgcolor=chart_bg,
        font=dict(color=font_color, family='DM Sans'),
        margin=dict(t=45, b=30, l=20, r=20),
        xaxis=dict(gridcolor=grid_color, showline=False),
        yaxis=dict(gridcolor=grid_color, showline=False),
    )
    return fig

# ── Dataset Summary KPIs ──────────────────────────────────────────────────────
st.markdown("<p class='section-header'>📊 Dataset Overview</p>", unsafe_allow_html=True)

k1, k2, k3, k4, k5 = st.columns(5)
stats = [
    ("🗂️", f"{len(df):,}", "Total Records"),
    ("🚗", str(df['brand'].nunique() if 'brand' in df.columns else "14"), "Brands"),
    ("💰", f"₹{df['price_lakh'].mean():.1f}L", "Avg Price"),
    ("📅", f"{int(df['year'].min())}–{int(df['year'].max())}", "Year Range"),
    ("🛣️", f"{int(df['km_driven'].median()/1000)}K", "Median KM"),
]
for col, (icon, val, label) in zip([k1,k2,k3,k4,k5], stats):
    with col:
        st.markdown(f"""
        <div class="stat-card">
            <div style="font-size:1.5rem;">{icon}</div>
            <div class="stat-value">{val}</div>
            <div class="stat-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ── Charts Row 1 ──────────────────────────────────────────────────────────────
st.markdown("<p class='section-header'>💰 Price Analysis</p>", unsafe_allow_html=True)
ch1, ch2 = st.columns(2)

with ch1:
    fig = px.histogram(df, x="price_lakh", nbins=20,
                       labels={'price_lakh':'Price (₹ Lakhs)'},
                       color_discrete_sequence=[ACCENT])
    fig = styled_layout(fig, "Price Distribution")
    fig.update_traces(marker_line_color='rgba(0,0,0,0.2)', marker_line_width=0.5)
    st.plotly_chart(fig, use_container_width=True)

with ch2:
    fig = px.scatter(df, x='year', y='price_lakh',
                     labels={'price_lakh':'Price (₹ Lakhs)', 'year':'Year'},
                     color_discrete_sequence=['#6C8EBF'], opacity=0.6)
    fig.update_traces(marker=dict(size=5))
    fig = styled_layout(fig, "Price vs Manufacturing Year")
    st.plotly_chart(fig, use_container_width=True)

# ── Charts Row 2 ──────────────────────────────────────────────────────────────
st.markdown("<p class='section-header'>🚗 Brand & Usage</p>", unsafe_allow_html=True)
ch3, ch4 = st.columns(2)

with ch3:
    brand_price = df.groupby("brand")["price_lakh"].mean().reset_index()
    brand_price = brand_price.sort_values("price_lakh", ascending=True).tail(10)
    fig = px.bar(brand_price, x="price_lakh", y="brand", orientation='h',
                 labels={"price_lakh":"Avg Price (₹ Lakhs)", "brand":"Brand"},
                 color="price_lakh", color_continuous_scale=[[0,'#355C7D'],[1,ACCENT]])
    fig.update_layout(coloraxis_showscale=False)
    fig = styled_layout(fig, "Top 10 Brands by Avg Price")
    st.plotly_chart(fig, use_container_width=True)

with ch4:
    fig = px.scatter(df, x="km_driven", y="price_lakh",
                     labels={"km_driven":"KM Driven", "price_lakh":"Price (₹ Lakhs)"},
                     color_discrete_sequence=["#2ca02c"], opacity=0.5)
    fig.update_traces(marker=dict(size=5))
    fig = styled_layout(fig, "KM Driven vs Price")
    st.plotly_chart(fig, use_container_width=True)

# ── Charts Row 3 ──────────────────────────────────────────────────────────────
st.markdown("<p class='section-header'>⚙️ Vehicle Characteristics</p>", unsafe_allow_html=True)
ch5, ch6, ch7 = st.columns(3)

with ch5:
    fuel_counts = df["fuel"].value_counts().reset_index()
    fuel_counts.columns = ["Fuel Type", "Count"]
    fig = px.pie(fuel_counts, names="Fuel Type", values="Count",
                 color_discrete_sequence=[ACCENT, '#355C7D', '#FF6B6B'],
                 hole=0.45)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig = styled_layout(fig, "Fuel Type Distribution")
    st.plotly_chart(fig, use_container_width=True)

with ch6:
    fig = px.pie(df, names="transmission",
                 color_discrete_sequence=['#1A1A2E', ACCENT],
                 hole=0.45)
    fig.update_traces(textposition='inside', textinfo='percent+label')
    fig = styled_layout(fig, "Transmission Distribution")
    st.plotly_chart(fig, use_container_width=True)

with ch7:
    owner_counts = df["owner"].value_counts().reset_index()
    owner_counts.columns = ["Owner Type", "Count"]
    fig = px.bar(owner_counts, x="Owner Type", y="Count",
                 color_discrete_sequence=[ACCENT])
    fig.update_traces(marker_line_width=0)
    fig = styled_layout(fig, "Ownership Distribution")
    st.plotly_chart(fig, use_container_width=True)

# ── Charts Row 4 ──────────────────────────────────────────────────────────────
st.markdown("<p class='section-header'>🔬 Advanced Analysis</p>", unsafe_allow_html=True)
ch8, ch9 = st.columns(2)

with ch8:
    fig = px.scatter(df, x="mileage(km/ltr/kg)", y="price_lakh",
                     labels={"mileage(km/ltr/kg)":"Mileage (km/l)", "price_lakh":"Price (₹ Lakhs)"},
                     color_discrete_sequence=["#17becf"], opacity=0.6)
    fig.update_traces(marker=dict(size=5))
    fig = styled_layout(fig, "Mileage vs Price")
    st.plotly_chart(fig, use_container_width=True)

with ch9:
    corr = df.select_dtypes(include=['int64','float64']).corr()
    fig = px.imshow(corr, text_auto=".2f", color_continuous_scale="RdBu",
                    aspect="auto")
    fig.update_layout(
        paper_bgcolor=chart_bg, plot_bgcolor=chart_bg,
        font=dict(color=font_color, size=11),
        margin=dict(t=30, b=10, l=10, r=10),
        title=dict(text="Feature Correlation Heatmap", font=dict(family='Syne', size=15, color=text_color))
    )
    st.plotly_chart(fig, use_container_width=True)

# ── Model Performance ─────────────────────────────────────────────────────────
st.markdown("<p class='section-header'>🏆 Model Performance</p>", unsafe_allow_html=True)

st.markdown('<div class="perf-card">', unsafe_allow_html=True)
p1, p2, p3, p4 = st.columns(4)
perf = [("Train R²", "0.83", "↑"), ("Test R²", "0.82", "↑"), ("MAE", "₹77,695", ""), ("RMSE", "₹1,06,605", "")]
for col, (label, val, delta) in zip([p1,p2,p3,p4], perf):
    with col:
        st.metric(label=label, value=val)
st.markdown('</div>', unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer-bar">
    RideRepublic Analytics © 2026 &nbsp;·&nbsp; Python &nbsp;·&nbsp;
    Scikit-Learn &nbsp;·&nbsp; Streamlit &nbsp;·&nbsp; Plotly
</div>
""", unsafe_allow_html=True)
