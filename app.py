import streamlit as st
import pandas as pd
import os
import base64

st.set_page_config(
    page_title="Protocolo - Alcaldía de Barranquilla",
    page_icon="🏛️",
    layout="wide"
)

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception:
        return None

def apply_custom_styles(side_bg):
    bin_str = get_base64_of_bin_file(side_bg)
    # Si no encuentra el archivo local, usa una imagen de respaldo de la ciudad
    bg_img = f"data:image/jpeg;base64,{bin_str}" if bin_str else "https://www.swedishnomad.com/wp-content/images/2020/03/Barranquilla.jpg"
    
    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Urbanist:wght@300;400;700&display=swap');

    .stApp {{
        background-image: url("{bg_img}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Capa azul oscura opaca para legibilidad total */
    .stApp::before {{
        content: "";
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: rgba(0, 15, 35, 0.92); 
        backdrop-filter: blur(8px);
        z-index: -1;
    }}

    .main-header {{
        text-align: center;
        padding: 2.5rem 0 0.5rem 0;
    }}

    .baq-title {{
        color: #FFFFFF;
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(30px, 5vw, 55px);
        font-weight: 900;
        text-transform: uppercase;
        margin: 0;
        letter-spacing: -1px;
    }}

    .baq-slogan {{
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2rem;
        font-weight: 900;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-top: 5px;
    }}
    .slogan-white {{ color: #FFFFFF; }}
    .slogan-yellow {{ color: #DFFF9A; }}

    .metrics-row {{
        display: flex;
        justify-content: center;
        gap: 30px;
        margin: 15px 0 30px 0;
        padding-bottom: 15px;
        border-bottom: 1px solid rgba(223, 255, 154, 0.1);
    }}

    .metric-item {{
        text-align: center;
    }}

    .metric-num {{
        color: #DFFF9A;
        font-size: 1.8rem;
        font-weight: 900;
        font-family: 'Montserrat', sans-serif;
        display: block;
    }}

    .metric-txt {{
        color: rgba(255, 255, 255, 0.6);
        font-size: 0.65rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        font-weight: 700;
    }}

    .search-container {{
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(223, 255, 154, 0.15);
        border-radius: 12px;
        padding: 25px;
        max-width: 850px;
        margin: 0 auto;
    }}

    .guest-card {{
        background: rgba(255, 255, 255, 0.05);
        border-left: 4px solid #DFFF9A;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 12px;
        transition: 0.3s;
    }}
    
    .guest-card:hover {{
        background: rgba(255, 255, 255, 0.08);
        transform: scale(1.01);
    }}

    .baq-footer {{
        margin-top: 40px;
        padding: 25px 0;
        background: rgba(0,0,0,0.2);
        border-top: 1px solid rgba(223, 255, 154, 0.1);
    }}

    [data-testid="stSidebar"] {{
        background-color: #0c1219 !important;
        border-right: 1px solid rgba(223, 255, 154, 0.1);
    }}
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
        except Exception:
            return None
    return None

def main():
    apply_custom_styles("fondo.jpeg")
    
    with st.sidebar:
        st.image("https://upload.wikimedia.org/wikipedia/commons/e/ea/Escudo_de_Barranquilla.svg", width=100)
        st.markdown("<h3 style='color:#DFFF9A; margin-top:10px;'>PANEL DE PROTOCOLO</h3>", unsafe_allow_html=True)
        menu = st.radio(
            "SELECCIONE UNA ACCIÓN:",
            ["🔍 Buscar por nombre o cargo", "🌐 Filtrar por Idioma", "📋 Mostrar lista completa"],
            index=0
        )
        st.markdown("---")
        st.caption("Sistema de Gestión de Eventos • V.2.7")

    st.markdown(f"""
        <div class="main-header">
            <h1 class="baq-title">ALCALDÍA DE BARRANQUILLA</h1>
            <p class="baq-slogan">
                <span class="slogan-white">Barranquilla</span> 
                <span class="slogan-yellow">está de moda</span>
            </p>
        </div>
    """, unsafe_allow_html=True)

    df = cargar_datos()

    if df is not None:
        # Cálculo de métricas
        total_invitados = len(df)
        total_idiomas = df['Languages'].nunique() if 'Languages' in df.columns else 0
        
        # Fila de métricas estilizada
        st.markdown(f"""
            <div class="metrics-row">
                <div class="metric-item">
                    <span class="metric-num">{total_invitados}</span>
                    <span class="metric-txt">Invitados</span>
                </div>
                <div class="metric-item">
                    <span class="metric-num">{total_idiomas}</span>
                    <span class="metric-txt">Idiomas</span>
                </div>
                <div class="metric-item">
                    <span class="metric-num">100%</span>
                    <span class="metric-txt">Aforo</span>
                </div>
            </div>
        """, unsafe_allow_html=True)

        if menu == "🔍 Buscar por nombre o cargo":
            st.markdown('<div class="search-container">', unsafe_allow_html=True)
            termino = st.text_input("Buscador de Protocolo:", placeholder="Escriba nombre o cargo...").strip()
            st.markdown('</div><br>', unsafe_allow_html=True)
            
            if termino:
                res = df[df.apply(lambda r: r.astype(str).str.contains(termino, case=False).any(), axis=1)]
                if not res.empty:
                    for _, fila in res.iterrows():
                        st.markdown(f"""
                        <div class="guest-card">
                            <div style="display:flex; justify-content:space-between; align-items: center;">
                                <span style="color:#DFFF9A; font-size:20px; font-weight:800; font-family:'Montserrat';">{fila.get('Name', 'N/A')}</span>
                                <span style="background:#DFFF9A; color:#001a35; padding: 2px 8px; border-radius:4px; font-weight:bold; font-size:10px;">MESA ASIGNADA</span>
                            </div>
                            <div style="margin-top:8px; display:grid; grid-template-columns: 1fr 1fr 1fr; gap: 10px; font-size:13px; opacity:0.8;">
                                <span><i class="fa-solid fa-briefcase" style="color:#DFFF9A;"></i> {fila.get('Position', 'N/A')}</span>
                                <span><i class="fa-solid fa-building" style="color:#DFFF9A;"></i> {fila.get('Organisation', 'N/A')}</span>
                                <span><i class="fa-solid fa-language" style="color:#DFFF9A;"></i> {fila.get('Languages', 'N/A')}</span>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning("No se encontraron resultados.")

        elif menu == "🌐 Filtrar por Idioma":
            st.subheader("Filtrado por Idioma")
            if 'Languages' in df.columns:
                idiomas = ["Todos"] + list(df['Languages'].dropna().unique())
                sel = st.selectbox("Idioma:", idiomas)
                res = df if sel == "Todos" else df[df['Languages'] == sel]
                st.dataframe(res[['Name', 'Position', 'Organisation', 'Languages']], use_container_width=True)

        elif menu == "📋 Mostrar lista completa":
            st.subheader("Base de Datos Maestra")
            st.dataframe(df, use_container_width=True)

        st.markdown("""
            <div class="baq-footer">
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; max-width: 900px; margin: 0 auto; text-align: center;">
                    <div>
                        <h4 style="color:#DFFF9A; margin-bottom:10px; font-size:14px;">CONTACTO OFICIAL</h4>
                        <p style="font-size:12px; color:rgba(255,255,255,0.6);"><i class="fas fa-map-marker-alt"></i> Centro Histórico, Barranquilla</p>
                        <p style="font-size:12px; color:rgba(255,255,255,0.6);"><i class="fas fa-phone"></i> Línea de Protocolo: 195</p>
                    </div>
                    <div>
                        <h4 style="color:#DFFF9A; margin-bottom:10px; font-size:14px;">REDES DE PROTOCOLO</h4>
                        <p style="font-size:12px; color:rgba(255,255,255,0.6);"><i class="fab fa-instagram"></i> @ProtocoloDistritalBAQ</p>
                        <p style="font-size:12px; color:rgba(255,255,255,0.6);"><i class="fab fa-twitter"></i> @GobiernoDigitalBAQ</p>
                    </div>
                </div>
            </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Cargue el archivo Excel para activar el sistema.")
        file = st.file_uploader("Subir base de datos (XLSX):", type=["xlsx"])
        if file:
            st.session_state['df'] = pd.read_excel(file)
            st.rerun()

if __name__ == "__main__":
    main()
