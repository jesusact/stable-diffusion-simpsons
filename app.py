import streamlit as st
import requests

# Configuración de la API local de Stable Diffusion WebUI
API_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# Opciones de prompts recomendados
prompt_templates = {
    "Persona/Personaje": "asim style. dramatic beautiful {type} of {subject} {location} with {lighting}. detailed background.",
    "Animal": "asim style. dramatic closeup national geographic image of a {subject} in its natural habitat. at {time}. detailed background."
}

# Opciones para selección
types = ["primer plano", "retrato"]
locations = ["en un jardín", "en un desierto", "en la cima de una montaña", "en una ruina romana", "dentro de una sala de estar lujosa", "en un set de película", "en un espacio oscuro y vacío", "en una biblioteca"]
lightings = ["focos", "luces de neón", "iluminación suave y ambiental"]
times = ["amanecer", "atardecer", "noche", "bajo la lluvia", "con nieve"]

# Interfaz de Streamlit
st.title("Generador de Imágenes AI de Los Simpsons 🎨")
st.sidebar.header("Opciones de Generación")

# Selección de categoría y entrada personalizada
category = st.sidebar.selectbox("Selecciona una categoría:", list(prompt_templates.keys()))
subject = st.sidebar.text_input("Especifica el tema (por ejemplo si es persona 'Donald Trump' y si es animal 'lobo'):")

if category == "Persona/Personaje":
    type_choice = st.sidebar.selectbox("Tipo:", types)
    location_choice = st.sidebar.selectbox("Ubicación:", locations)
    lighting_choice = st.sidebar.selectbox("Iluminación:", lightings)
elif category == "Animal":
    time_choice = st.sidebar.selectbox("Momento del día:", times)


# Generación del prompt
if subject:
    prompt = prompt_templates[category]
    
    if category == "Persona/Personaje":
        prompt = prompt.replace("{type}", "headshot" if type_choice == "primer plano" else "portrait").replace("{subject}", subject).replace("{location}", locations[locations.index(location_choice)]).replace("{lighting}", lightings[lightings.index(lighting_choice)])
    elif category == "Animal":
        prompt = prompt.replace("{subject}", subject).replace("{time}", times[times.index(time_choice)])

    # Botón para generar imagen
    if st.sidebar.button("Generar Imagen"):
        with st.spinner("Generando imagen..."):
            payload = {"prompt": prompt, "steps": 30, "cfg_scale": 7, "width": 300, "height": 300}
            response = requests.post(API_URL, json=payload)
            if response.status_code == 200:
                image_data = response.json()["images"][0]
                st.image(f"data:image/png;base64,{image_data}", caption="Imagen Generada")
            else:
                st.error("Error al generar la imagen. Verifica que Stable Diffusion WebUI está corriendo.")