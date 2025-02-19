# Generador de Imágenes AI de Los Simpsons 😶‍🌫️

![Generador de Imágenes AI de Los Simpsons](https://raw.githubusercontent.com/jesusact/stable-diffusion-simpsons/refs/heads/main/assets/banner-simpsons.webp)

## Descripción
Este proyecto es una aplicación web creada con Streamlit que permite generar imágenes de estilo *Los Simpsons* utilizando Stable Diffusion WebUI. Los usuarios pueden seleccionar diferentes categorías y personalizar los detalles de la imagen, como el entorno, la iluminación y el momento del día.

## Características
- Generación de imágenes a partir de prompts estructurados.
- Varias categorías de prompts: personajes, animales, biomas, lugares famosos y flores.
- Personalización de detalles como iluminación, ubicación y momento del día.
- Integración con Stable Diffusion WebUI para la generación de imágenes.
- Interfaz intuitiva construida con Streamlit.

## Requisitos
- Python 3.8+
- Streamlit
- Requests
- Stable Diffusion WebUI corriendo en local
- Modelo de Los Simpsons: [CivitAI - The Simpsons](https://civitai.com/models/1250/the-simpsons)

## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/jesusact/generador-simpsons.git
   cd generador-simpsons
   ```
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Asegúrate de que Stable Diffusion WebUI esté corriendo en `http://127.0.0.1:7860` con el modelo de Los Simpsons cargado.

## Uso
1. Ejecuta la aplicación:
   ```bash
   streamlit run app.py
   ```
2. Abre el navegador en la URL proporcionada por Streamlit.
3. Selecciona una categoría y personaliza los detalles de la imagen.
4. Pulsa "Generar Imagen" y espera el resultado.

