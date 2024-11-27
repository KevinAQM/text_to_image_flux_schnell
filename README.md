## Descripción
Este proyecto permite crear una aplicacion web para generar imagenes con el uso de Inteligencia Artificial.

## Requisitos previos
- Python 3.x
- Una API Key de Together AI.

## Instalación

1. Clonar el repositorio: ```git clone https://github.com/KevinAQM/youtube_comments.git```

2. Dirijirse a la carpeta del proyecto: ```cd text_to_image_flux_schnell```

3. Crear el entorno virtual: ```python -m venv .venv```

4. Activar entorno virtual: ```.venv\Scripts\activate```

5. Instalar dependencias: ```pip install -r requirements.txt```

6. Configurar variables de entorno:
   - Crear el archivo ```.env```
   - Obtener una API KEY en Together AI en: ([Together AI ](https://api.together.ai/))
   - Añadir tu API KEY con el código: ```TOGETHER_API_KEY="PEGAR-TU-API-KEY-AQUI"```

## Uso
En el terminal:
- Ejecutar la aplicación: ```streamlit run app.py```
- Ingresar en el recuadro la descripción de la imagen que quieres crear y dar click al botón "Generar Imagen"
- ¡Listo! Tu imagen se habrá creado en pocos segundos. Puedes guardarlo.

## Licencia
Este proyecto está bajo la Licencia MIT.
