import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Nexus - Monitor Acústico",
    page_icon="🔊",
    layout="wide"
)

# Estilos limpios y profesionales con alto contraste
st.markdown("""
    <style>
    .main {
        background-color: #f1f5f9;
    }
    h1, h2, h3 {
        color: #0f172a;
    }
    </style>
""", unsafe_allow_html=True)

# Panel lateral informativo
with st.sidebar:
    st.header("Panel de Control")
    st.write("**Proyecto:** Teoría de Señales")
    st.write("**Hardware:** ESP32 + Sensor KY-037")
    st.write("**Interfaz:** Python & Streamlit")
    st.divider()
    st.success("🟢 Sistema activo y escuchando señales.")

# Título principal
st.title("🔊 Monitor Inteligente de Detección Acústica")
st.markdown("### *Plataforma de análisis en tiempo real y diferenciación de frecuencias (Hz)*")
st.markdown("")

# Métricas superiores claras y legibles
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Estado del Sistema", value="Activo", delta="En Línea")
with col2:
    st.metric(label="Análisis Espectral", value="Dinámico", delta="Frecuencias en Hz")
with col3:
    st.metric(label="Modo de Registro", value="Automático", delta="CSV + Galería")

st.markdown("---")

try:
    df = pd.read_csv("historial_eventos.csv")
    st.subheader("📋 Historial de Eventos y Frecuencias Detectadas")
    
    if not df.empty:
        st.dataframe(df, use_container_width=True)
    else:
        st.info("El historial está vacío. Esperando registros...")

    st.markdown("---")
    st.subheader("📊 Galería de Gráficas y Frecuencias (Hz) por Evento")
    
    if "Ruta_Imagen" in df.columns and not df.empty:
        # Recorrer del evento más reciente al más antiguo
        for index, row in df.iloc[::-1].iterrows():
            frecuencia_hz = row['Frecuencia_Hz'] if 'Frecuencia_Hz' in df.columns else "No especificada"
            
            with st.container():
                # Tarjeta limpia con fondo blanco y letras oscuras perfectamente legibles
                st.markdown(f"""
                    <div style="background-color: #ffffff; padding: 20px; border-radius: 10px; border-left: 6px solid #ff4b4b; box-shadow: 0 3px 6px rgba(0,0,0,0.08); margin-bottom: 15px;">
                        <h4 style="margin: 0; color: #1e293b;">🎵 Tipo de Sonido: {row['Tipo_Evento']}</h4>
                        <p style="margin: 10px 0 0 0; color: #475569; font-size: 16px;">
                            <b>⚡ Frecuencia Exacta:</b> <span style="color: #2563eb; font-weight: bold; font-size: 18px;">{frecuencia_hz}</span> | 
                            <b>🕒 Fecha y Hora:</b> {row['Fecha_Hora']}
                        </p>
                    </div>
                """, unsafe_allow_html=True)
                
                # Mostrar la gráfica individual correspondiente
                if pd.notna(row['Ruta_Imagen']) and os.path.exists(row['Ruta_Imagen']):
                    st.image(row['Ruta_Imagen'], caption=f"Análisis espectral para {row['Tipo_Evento']} a {frecuencia_hz}", width=700)
                else:
                    st.warning("⚠️ No se encontró la imagen asociada para este registro.")
            st.markdown("---")
    else:
        st.info("🎨 Aún no hay gráficas guardadas en la galería.")

except Exception as e:
    st.info("⚠️ Esperando registros de eventos en el archivo CSV...")