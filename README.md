# Generador de Imágenes AI de Los Simpsons 🎨

![Generador de Imágenes AI de Los Simpsons](https://raw.githubusercontent.com/jesusact/stable-diffusion-simpsons/refs/heads/main/assets/banner-simpsons.webp)

## Descripción
Este proyecto es una aplicación web creada con Streamlit que permite generar imágenes de estilo *Los Simpsons* utilizando Stable Diffusion WebUI. Los usuarios pueden seleccionar diferentes categorías y personalizar los detalles de la imagen, como el tipo, la ubicación, la iluminación y el momento del día.

## Características
- Generación de imágenes a partir de prompts estructurados.
- Categorías de prompts disponibles: personajes y animales.
- Personalización de detalles como tipo de imagen, ubicación, iluminación y momento del día.
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
3. Selecciona una categoría (Persona/Personaje o Animal).
4. Introduce el tema (por ejemplo, "Homer Simpson" o "lobo").
5. Personaliza los detalles como tipo de imagen, ubicación, iluminación o momento del día.
6. Pulsa "Generar Imagen" y espera el resultado.

## Ejemplos de Generación
### Interfaz en uso
Ejemplo de la aplicación generando una imagen de Vin Diesel en un set de película con luces de focos.

![Imagen interfaz](https://github.com/jesusact/stable-diffusion-simpsons/blob/673a508e70c998cbd7f6a2ca278aec15d19dffbd/assets/imagen_app.png)

### Otras Imágenes Generadas
#### Donald Trump en un jardín
![Donald Trump](https://github.com/jesusact/stable-diffusion-simpsons/blob/673a508e70c998cbd7f6a2ca278aec15d19dffbd/assets/trump_generado.png)

#### Un león al atardecer
![León](https://github.com/jesusact/stable-diffusion-simpsons/blob/673a508e70c998cbd7f6a2ca278aec15d19dffbd/assets/leon.png)

#### Leo Messi en una biblioteca
![Messi](https://github.com/jesusact/stable-diffusion-simpsons/blob/673a508e70c998cbd7f6a2ca278aec15d19dffbd/assets/messi.png)

### Desarrolladores
- [@jesusact](https://github.com/jesusact)  
- [@boorjabraavo21](https://github.com/boorjabraavo21)
