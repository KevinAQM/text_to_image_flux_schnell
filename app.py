import streamlit as st
import os
from together import Together
from dotenv import load_dotenv
import requests
from io import BytesIO
from PIL import Image
import time

# Cargar variables de entorno
load_dotenv()

# Configurar Together API
together_key = os.getenv("TOGETHER_API_KEY")
client = Together()

# Configuración de la página
st.set_page_config(
    page_title="Generador de Imágenes con IA",
    page_icon="🎨",
    layout="centered"
)

# Estilos CSS personalizados
st.markdown("""
    <style>
    .stButton > button {
        width: 100%;
        border-radius: 8px;
        background-color: #007bff;
        color: white;
        border: none;
        padding: 12px 20px;
        font-size: 16px;
        font-weight: 500;
        transition: background-color 0.3s ease, color 0.3s ease;
    }
    .stButton > button:disabled {
        background-color: #6c757d;
        cursor: not-allowed;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicializar variables de estado
if "button_disabled" not in st.session_state:
    st.session_state.button_disabled = False
if "image_generated" not in st.session_state:
    st.session_state.image_generated = None
if "countdown_start" not in st.session_state:
    st.session_state.countdown_start = None

# Función para iniciar el temporizador
def start_timer():
    st.session_state.button_disabled = True
    st.session_state.countdown_start = time.time()
    st.session_state.total_countdown_time = 30  # Establecer tiempo total de cuenta regresiva

# Función para verificar el temporizador
def check_timer():
    if st.session_state.button_disabled and st.session_state.countdown_start:
        elapsed_time = time.time() - st.session_state.countdown_start
        remaining_time = max(st.session_state.total_countdown_time - elapsed_time, 0)
        
        if remaining_time <= 0:
            st.session_state.button_disabled = False
            st.session_state.countdown_start = None
            st.session_state.total_countdown_time = 0
            return 0
        
        return int(remaining_time)
    return 0

# Título principal
st.title("🦙 Generador de Imágenes con IA")
st.markdown("---")

# Área de entrada del prompt
prompt = st.text_area(
    "Describe la imagen que deseas crear:",
    placeholder="Ejemplo: Un gato volando sobre una ciudad futurista al atardecer...",
    height=68
)

# Parámetros de generación
st.sidebar.header("Configuración avanzada")
steps = st.sidebar.slider("Pasos de generación:", min_value=1, max_value=4, value=4, step=1)
style = st.sidebar.selectbox(
    "Estilo artístico:",
    ["Realista", "Anime", "Acuarela", "Óleo", "Digital Art"]
)

# Verificar el estado del temporizador
remaining_time = check_timer()

# Botón de generación
if st.button("🚀 Generar Imagen", disabled=st.session_state.button_disabled):
    if prompt:
        try:
            with st.spinner('Generando tu imagen... Por favor espera.'):
                # Modificar el prompt según el estilo seleccionado
                styled_prompt = f"{prompt}, style: {style.lower()}"

                # Generar imagen
                response = client.images.generate(
                    prompt=styled_prompt,
                    model="black-forest-labs/FLUX.1-schnell-Free",
                    steps=steps
                )

                image_url = response.data[0].url

                # Descargar la imagen
                response = requests.get(image_url)
                img = Image.open(BytesIO(response.content))

                # Almacenar la imagen en el estado
                st.session_state.image_generated = img

                # Iniciar el temporizador
                start_timer()

        except Exception as e:
            st.error(f"Ocurrió un error: {str(e)}")
    else:
        st.warning("Por favor, ingresa una descripción para la imagen.")

# Mostrar imagen generada previamente
if st.session_state.image_generated:
    st.image(st.session_state.image_generated, caption="", use_container_width=True)

    # Convertir imagen para descarga
    buf = BytesIO()
    st.session_state.image_generated.save(buf, format="PNG")
    byte_im = buf.getvalue()

    # Botón de descarga
    st.download_button(
        label="📥 Descargar imagen",
        data=byte_im,
        file_name="imagen_ia.png",
        mime="image/png"
    )

# Mostrar mensaje del temporizador si está activo
if st.session_state.button_disabled:
    # Mensaje inicial mostrando 30 segundos totales
    if st.session_state.countdown_start and time.time() - st.session_state.countdown_start < 1:
        st.info("Por favor, espera 30 segundos antes de generar otra imagen.")
    else:
        remaining_time = check_timer()
        st.info(f"Por favor, espera {remaining_time} segundos antes de generar otra imagen.")