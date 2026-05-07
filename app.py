import streamlit as st
import pandas as pd
import os

# Configuración inicial de la página
st.set_page_config(
    page_title="Protocolo - Alcaldía de Barranquilla",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inyección de CSS para forzar el modo oscuro y estilo institucional
st.markdown("""
    <style>
    /* Fondo general y textos */
    .stApp {
        background-color: #0e1117;
        color: #f5f5f5;
    }
    
    /* Contenedor del Logo y Título */
    .brand-header {
        background: linear-gradient(90deg, #161b22 0%, #0e1117 100%);
        padding: 25px;
        border-radius: 15px;
        border-left: 10px solid #DFFF9A;
        margin-bottom: 30px;
        display: flex;
        align-items: center;
        gap: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    
    .brand-title {
        color: #DFFF9A;
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        font-size: 32px;
        letter-spacing: -1px;
        margin: 0;
        text-transform: uppercase;
    }
    
    .brand-subtitle {
        color: #8b949e;
        font-size: 14px;
        margin: 0;
    }

    /* Estilo de los resultados (Tarjetas) */
    .guest-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-bottom: 15px;
        transition: transform 0.2s;
    }
    
    .guest-card:hover {
        border-color: #DFFF9A;
        transform: translateY(-2px);
    }

    .highlight {
        color: #DFFF9A;
        font-weight: bold;
    }

    /* Sidebar personalizado */
    [data-testid="stSidebar"] {
        background-color: #161b22;
        border-right: 1px solid #30363d;
    }
    </style>
    """, unsafe_allow_html=True)

def cargar_datos():
    archivo = "Acomodación de puestos - CENA.xlsx"
    if os.path.exists(archivo):
        try:
            df = pd.read_excel(archivo)
            # Limpieza de columnas como en tu código original
            df.columns = df.columns.str.strip()
            return df
        except Exception as e:
            st.error(f"Error técnico al leer el archivo: {e}")
            return None
    return None

def mostrar_encabezado():
    st.markdown("""
        <div class="brand-header">
            <img src="https://upload.wikimedia.org/wikipedia/commons/e/ea/Escudo_de_Barranquilla.svg" width="70">
            <div>
                <h1 class="brand-title">ALCALDÍA DE BARRANQUILLA</h1>
                <p class="brand-subtitle">Sistema Digital de Gestión de Protocolo y Eventos</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

def main():
    mostrar_encabezado()
    
    df = cargar_datos()

    if df is not None:
        # --- MENÚ DE GESTIÓN (REEMPLAZA AL WHILE) ---
        with st.sidebar:
            st.image("https://iconape.com/wp-content/files/ts/255586/svg/255586.svg", width=150)
            st.title("MENÚ PRINCIPAL")
            opcion = st.radio(
                "Seleccione una operación:",
                ["1. Buscar Invitado", "2. Listar Idiomas", "3. Ver Base Completa"],
                index=0
            )
            st.markdown("---")
            st.info("Utilice este panel para navegar por la base de datos de la cena oficial.")

        # --- OPCIÓN 1: BÚSQUEDA (TU LÓGICA ORIGINAL) ---
        if "1" in opcion:
            st.subheader("🔍 Buscador de Invitados")
            termino = st.text_input("Ingrese nombre, cargo o palabra clave:", placeholder="Ej: Alcalde, Embajador...").strip()

            if termino:
                # AQUÍ ESTÁ TU LÓGICA EXACTA: Filtramos buscando en todas las columnas
                resultado = df[df.apply(lambda r: r.astype(str).str.contains(termino, case=False).any(), axis=1)]

                if not resultado.empty:
                    st.success(f"Se encontraron {len(resultado)} coincidencia(s):")
                    
                    # --- ESTRUCTURA REPETITIVA (FOR) PARA MOSTRAR RESULTADOS ---
                    for index, fila in resultado.iterrows():
                        st.markdown(f"""
                        <div class="guest-card">
                            <span class="highlight">👤 Invitado:</span> {fila.get('Name', 'N/A')} <br>
                            <span class="highlight">💼 Cargo:</span> {fila.get('Position', 'N/A')} <br>
                            <span class="highlight">🌐 Idioma:</span> {fila.get('Languages', 'N/A')}
                        </div>
                        """, unsafe_allow_html=True)
                else:
                    st.warning(f"No se hallaron resultados para: '{termino}'")

        # --- OPCIÓN 2: LISTAR IDIOMAS ---
        elif "2" in opcion:
            st.subheader("🌐 Idiomas Registrados")
            # Obtenemos idiomas únicos como en tu código original
            if 'Languages' in df.columns:
                lista_idiomas = df['Languages'].unique()
                cols = st.columns(3)
                for i, idioma in enumerate(lista_idiomas):
                    cols[i % 3].markdown(f"✅ {idioma}")
            else:
                st.error("La columna 'Languages' no existe en el archivo.")

        # --- OPCIÓN 3: VER BASE COMPLETA ---
        elif "3" in opcion:
            st.subheader("📋 Listado General de Protocolo")
            st.dataframe(df, use_container_width=True)
            
    else:
        # Fallback si no encuentra el archivo
        st.error("⚠️ Archivo 'Acomodación de puestos - CENA.xlsx' no detectado.")
        st.warning("Por favor, suba el archivo Excel para activar el sistema:")
        archivo_subido = st.file_uploader("Cargar Excel Institucional", type=["xlsx"])
        if archivo_subido:
            df_manual = pd.read_excel(archivo_subido)
            st.success("Archivo cargado temporalmente con éxito.")
            st.dataframe(df_manual)

if __name__ == "__main__":
    main()
