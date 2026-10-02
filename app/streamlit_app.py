import streamlit as st
import pandas as pd
import sqlite3
import base64

st.set_page_config(page_title="Stock de Mode", layout="wide")


def inyectar_css(css):
    abre = chr(60) + "style" + chr(62)
    cierra = chr(60) + "/style" + chr(62)
    st.markdown(abre + css + cierra, unsafe_allow_html=True)


inyectar_css("""
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600&family=Montserrat:wght@300;400&display=swap');

html, body, [class*="css"] {
    font-family: 'Montserrat', sans-serif;
}

h1 {
    font-family: 'Cormorant Garamond', serif !important;
    font-weight: 600 !important;
    font-size: 4.5rem !important;
    letter-spacing: 10px;
    text-transform: uppercase;
    color: #1A1A1A !important;
}

[data-testid="stMetricValue"] {
    font-family: 'Cormorant Garamond', serif;
    font-size: 2.4rem;
}

[data-testid="stMetricLabel"] {
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.75rem;
}

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
    border: 1px solid #D9CFBF;
}
""")

col_logo, col_titulo = st.columns([1, 4])

with col_logo:
    uploaded_logo = st.file_uploader("Logo de marca", type=["png", "jpg", "jpeg"])

with col_titulo:
    st.title("Stock de Mode")
    st.caption("SISTEMA DE CONTROL DE PIEZAS Y STOCK")

if uploaded_logo is not None:
    b64_logo = base64.b64encode(uploaded_logo.getvalue()).decode()
    tipo = uploaded_logo.type
    inyectar_css(
        ".stApp::before {"
        "content: '';"
        "position: fixed;"
        "top: 0; left: 0; right: 0; bottom: 0;"
        "background-image: url('data:" + tipo + ";base64," + b64_logo + "');"
        "background-repeat: no-repeat;"
        "background-position: center;"
        "background-size: 450px;"
        "opacity: 0.08;"
        "pointer-events: none;"
        "z-index: 0;"
        "}"
    )
    with col_logo:
        st.image(uploaded_logo, width=150)

st.divider()

conn = sqlite3.connect("database/inventario.db")
query = """
SELECT p.id_prenda, p.nombre, p.categoria, p.talla, p.color, p.material_principal,
       p.costo_produccion, p.precio_venta, i.cantidad_disponible, i.ubicacion_almacen
FROM prendas p
JOIN inventario i ON p.id_prenda = i.id_prenda
"""
df = pd.read_sql_query(query, conn)
conn.close()

c1, c2, c3 = st.columns(3)
c1.metric("Piezas distintas", df["id_prenda"].nunique())
c2.metric("Unidades en stock", int(df["cantidad_disponible"].sum()))
c3.metric("Valor de inventario", f"{(df['costo_produccion'] * df['cantidad_disponible']).sum():,.0f}")

st.divider()

categoria_filtro = st.selectbox("Filtrar por categoria", ["Todas"] + sorted(df["categoria"].unique().tolist()))
if categoria_filtro != "Todas":
    df = df[df["categoria"] == categoria_filtro]

st.dataframe(df, use_container_width=True)

st.divider()
st.subheader("Piezas con bajo stock")
st.dataframe(df[df["cantidad_disponible"] < 10], use_container_width=True)