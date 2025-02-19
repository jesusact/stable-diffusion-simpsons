import streamlit as st
import requests
import random

# Configuración de la API local de Stable Diffusion WebUI
API_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# Opciones de prompts recomendados
prompt_templates = {
    "Persona/Personaje": "asim style. dramatic beautiful {type} of {subject} {location} with {lighting}. detailed background.",
    "Animal": "asim style. dramatic closeup national geographic image of a {subject} in its natural habitat. at {time}. detailed background.",
    "Bioma": "asim style. a beautiful {season} landscape panorama painting of {biome} {time}.",
    "Lugar Famoso": "asim style. a beautiful panorama view of {place} {time}.",
    "Flor": "asim style. a beautiful vase of {flower} flowers. on a balcony table at {time} . nearby a {object}."
}

# Opciones para selección
types = ["primer plano", "retrato"]
locations = ["afuera en un jardín", "en un desierto", "en la cima de una montaña", "en una ruina romana", "dentro de una sala de estar lujosa", "en un set de película", "en un espacio oscuro y vacío", "en un caleidoscopio", "en una biblioteca antigua"]
lightings = ["focos", "luces de neón", "iluminación suave y ambiental", "luces de luciérnagas"]
times = ["amanecer", "atardecer", "noche", "una tarde nublada", "bajo la lluvia", "con nieve"]
seasons = ["verano", "otoño", "invierno", "primavera"]
structures = ["biblioteca steampunk", "torre de babel", "casa en el árbol", "victoriano encantado"]
biomes = ["bosque", "desierto", "océano", "tundra", "jungla"]
places = ["Torre Eiffel", "Machu Picchu", "Gran Cañón", "Muralla China"]
flowers = ["rosa", "tulipán", "girasol", "orquídea"]
objects = ["botella de cerveza y un vaso medio vacío", "botella de vino y un vaso medio vacío", "cuenco de frutas"]

# Interfaz de Streamlit
st.title("Generador de Imágenes AI de Los Simpsons 🎨")
st.sidebar.header("Opciones de Generación")

# Selección de categoría y entrada personalizada
category = st.sidebar.selectbox("Selecciona una categoría:", list(prompt_templates.keys()))
subject = st.sidebar.text_input("Especifica el tema (por ejemplo, 'Homer Simpson', 'lobo', 'Torre Eiffel'):")

if category == "Persona/Personaje":
    type_choice = st.sidebar.selectbox("Tipo:", types)
    location_choice = st.sidebar.selectbox("Ubicación:", locations)
    lighting_choice = st.sidebar.selectbox("Iluminación:", lightings)
elif category == "Animal":
    time_choice = st.sidebar.selectbox("Momento del día:", times)
elif category == "Bioma":
    season_choice = st.sidebar.selectbox("Estación:", seasons)
    biome_choice = st.sidebar.selectbox("Bioma:", biomes)
    time_choice = st.sidebar.selectbox("Momento del día:", times)
elif category == "Lugar Famoso":
    place_choice = st.sidebar.selectbox("Lugar famoso:", places)
    time_choice = st.sidebar.selectbox("Momento del día:", times)
elif category == "Flor":
    flower_choice = st.sidebar.selectbox("Flor:", flowers)
    time_choice = st.sidebar.selectbox("Momento del día:", times)
    object_choice = st.sidebar.selectbox("Objeto cercano:", objects)

# Generación del prompt
if subject:
    prompt = prompt_templates[category]
    
    if category == "Persona/Personaje":
        prompt = prompt.replace("{type}", "headshot" if type_choice == "primer plano" else "portrait").replace("{subject}", subject).replace("{location}", locations[locations.index(location_choice)]).replace("{lighting}", lightings[lightings.index(lighting_choice)])
    elif category == "Animal":
        prompt = prompt.replace("{subject}", subject).replace("{time}", times[times.index(time_choice)])
    elif category == "Bioma":
        prompt = prompt.replace("{season}", seasons[seasons.index(season_choice)]).replace("{biome}", biomes[biomes.index(biome_choice)]).replace("{time}", times[times.index(time_choice)])
    elif category == "Lugar Famoso":
        prompt = prompt.replace("{place}", places[places.index(place_choice)]).replace("{time}", times[times.index(time_choice)])
    elif category == "Flor":
        prompt = prompt.replace("{flower}", flowers[flowers.index(flower_choice)]).replace("{time}", times[times.index(time_choice)]).replace("{object}", objects[objects.index(object_choice)])

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