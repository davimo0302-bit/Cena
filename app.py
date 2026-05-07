import streamlit as st
import pandas as pd
import os
from PIL import Image

st.set_page_config(
    page_title="Protocolo - Alcaldía de Barranquilla",
    page_icon="🏛️",
    layout="wide"
)

# Nota: Asumimos que tu imagen se llama 'fondo.jpg'
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Urbanist:wght@300;400;700&display=swap');

    /* Capa de fondo con imagen desenfocada */
    .stApp {
        background: url("https://images.unsplash.com/photo-1599839624912-67609f194286?q=80&w=2070&auto=format&fit=crop") no-repeat center center fixed;
        background-size: cover;
    }

    /* Overlay oscuro para legibilidad */
    .stApp::before {
        content: "";
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(0, 26, 53, 0.85); /* Azul institucional con transparencia */
        backdrop-filter: blur(8px); /* AQUÍ ESTÁ EL DESENFOQUE */
        z-index: -1;
    }

    /* Estilo del Header Institucional */
    .header-container {
        text-align: center;
        padding: 2.5rem 0;
        margin-bottom: 2rem;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        border-bottom: 4px solid #DFFF9A;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }

    .baq-title {
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
        font-size: 55px;
        font-weight: 900;
        letter-spacing: 2px;
        margin-bottom: 0;
        text-transform: uppercase;
    }

    /* Slogan con tipografía solicitada (Montserrat 900) */
    .baq-slogan {
        font-family: 'Montserrat', sans-serif;
        font-size: 1.8rem;
        font-weight: 900;
        margin-top: 5px;
        text-transform: uppercase;
    }

    .slogan-white { color: #FFFFFF; }
    .slogan-yellow { 
        color: #FFD700; 
        text-shadow: 0px 0px 15px rgba(255, 215, 0, 0.6); 
    }

    /* Métricas con diseño moderno */
    .metric-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(223, 255, 154, 0.2);
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        background: rgba(223, 255, 154, 0.15);
        transform: translateY(-5px);
    }
    .metric-val { color: #DFFF9A; font-size: 2.5rem; font-weight: 800; }
    .metric-lab { font-family: 'Urbanist'; color: #cbd5e0; font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; }

    /* Tarjetas de invitados optimizadas */
    .guest-card {
        background: rgba(0, 45, 90, 0.8);
        border: 1px solid #003d7a;
        border-left: 8px solid #DFFF9A;
        padding: 1.8rem;
        border-radius: 12px;
        margin-bottom: 1.2rem;
        box-shadow: 5px 5px 20px rgba(0,0,0,0.3);
    }

    .baq-footer {
        background-color: rgba(0, 9, 20, 0.9);
        padding: 3rem 2rem;
        border-top: 4px solid #DFFF9A;
        margin-top: 4rem;
        border-radius: 20px 20px 0 0;
    }

    /* Ajuste de nitidez para el logo */
    img {
        image-rendering: -webkit-optimize-contrast;
        filter: drop-shadow(0px 0px 10px rgba(0,0,0,0.5));
    }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True)

def cargar_datos():
    archivo = "Alojamiento de puestos - CENA.xlsx"
    if os.path.exists(archivo):
        try:
            df = pd.read_excel(archivo)
            df.columns = df.columns.str.strip()
            return df
        except Exception as e:
            st.error(f"Error al leer Excel: {e}")
            return None
    return None

def main():
    logo_path = "logo.png"
    
    st.markdown('<div class="header-container">', unsafe_allow_html=True)
    if os.path.exists(logo_path):
        st.image(logo_path, width=130)
    else:
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Escudo_de_Barranquilla.svg", width=100)
        
    st.markdown('''
        <h1 class="baq-title">ALCALDÍA DE BARRANQUILLA</h1>
        <p class="baq-slogan">
            <span class="slogan-white">Barranquilla</span> 
            <span class="slogan-yellow">está de moda</span>
        </p>
    ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    df = cargar_datos()

    if df is not None:
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown(f'<div class="metric-card"><div class="metric-val">{len(df)}</div><div class="metric-lab">Invitados</div></div>', unsafe_allow_html=True)
        with c2:
            idiomas_count = df['Languages'].nunique() if 'Languages' in df.columns else 0
            st.markdown(f'<div class="metric-card"><div class="metric-val">{idiomas_count}</div><div class="metric-lab">Idiomas</div></div>', unsafe_allow_html=True)
        with c3:
            org_count = df['Organisation'].nunique() if 'Organisation' in df.columns else 0
            st.markdown(f'<div class="metric-card"><div class="metric-val">{org_count}</div><div class="metric-lab">Entidades</div></div>', unsafe_allow_html=True)
        with c4:
            st.markdown(f'<div class="metric-card"><div class="metric-val">100%</div><div class="metric-lab">Seguro</div></div>', unsafe_allow_html=True)

        with st.sidebar:
            if os.path.exists(logo_path):
                st.image(logo_path, width=150)
            else:
                st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Escudo_de_Barranquilla.svg", width=120)
            st.markdown("### OPERACIÓN PROTOCOLO")
            opcion = st.selectbox("Menú Principal", ["🔍 Buscador Inteligente", "🌐 Mapa de Idiomas", "📊 Reporte General"])
            st.divider()
            st.caption("Barranquilla Imparable 2024")

        if "Buscador" in opcion:
            st.markdown("<br>", unsafe_allow_html=True)
            termino = st.text_input("Busca por nombre, cargo o mesa:", placeholder="Ej. Alex Char").strip()

            if termino:
                res = df[df.apply(lambda r: r.astype(str).str.contains(termino, case=False).any(), axis=1)]
                if not res.empty:
                    st.success(f"Se encontraron {len(res)} coincidencias:")
                    for _, fila in res.iterrows():
                        st.markdown(f"""
                        <div class="guest-card">
                            <div style="display:flex; justify-content:space-between; align-items:center;">
                                <span style="color:#DFFF9A; font-size:26px; font-weight:800;">{fila.get('Name', 'N/A')}</span>
                                <span style="background:#DFFF9A; color:#000; padding:4px 15px; border-radius:20px; font-weight:bold; font-size:12px;">REGISTRADO</span>
                            </div>
                            <div style="margin-top:15px; display:grid; grid-template-columns: 1fr 1fr; gap: 10px;">
                                <p style="margin:0;"><i class="fa-solid fa-briefcase" style="color:#DFFF9A"></i> <b>Cargo:</b> {fila.get('Position', 'N/A')}</p>
                                <p style="margin:0;"><i class="fa-solid fa-building" style="color:#DFFF9A"></i> <b>Entidad:</b> {fila.get('Organisation', 'N/A')}</p>
                                <p style="margin:0;"><i class="fa-solid fa-language" style="color:#DFFF9A"></i> <b>Idioma:</b> {fila.get('Languages', 'N/A')}</p>
                                <p style="margin:0;"><i class="fa-solid fa-chair" style="color:#DFFF9A"></i> <b>Ubicación:</b> Salón Principal</p>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.error("No se encontraron resultados para su búsqueda.")

        st.markdown("""
            <div class="baq-footer">
                <div style="display: flex; flex-wrap: wrap; justify-content: space-around; gap: 30px; max-width: 1200px; margin: 0 auto;">
                    <div>
                        <h4 style="color:#DFFF9A;">CONTACTO OFICIAL</h4>
                        <p style="font-size:0.9rem; color:#cbd5e0;"><i class="fas fa-map-marker-alt"></i> Calle 78 # 53 - 70<br>Barranquilla, Colombia</p>
                        <p style="font-size:0.9rem; color:#cbd5e0;"><i class="fas fa-phone"></i> +57 (605) 339-9999</p>
                    </div>
                    <div>
                        <h4 style="color:#DFFF9A;">SÍGUENOS</h4>
                        <div style="display:flex; gap:20px; font-size:1.8rem; color: #DFFF9A;">
                            <i class="fab fa-facebook"></i> <i class="fab fa-twitter"></i> <i class="fab fa-instagram"></i>
                        </div>
                    </div>
                </div>
                <p style="text-align:center; margin-top:3rem; opacity:0.4; font-size:0.8rem;">© 2024 Alcaldía de Barranquilla • Actividad Académica de Protocolo</p>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Cargue el archivo Excel para iniciar.")
        man = st.file_uploader("Subir Archivo:", type=["xlsx"])
        if man:
            st.session_state['df'] = pd.read_excel(man)
            st.rerun()

if __name__ == "__main__":
    main()
