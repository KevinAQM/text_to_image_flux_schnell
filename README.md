Descripción
Este proyecto permite extraer los comentarios de un video de YouTube utilizando la API oficial de Google/YouTube.

Requisitos previos
Python 3.x
Una API Key de YouTube
Instalación
Clonar el repositorio: git clone https://github.com/KevinAQM/youtube_comments.git

Dirijirse a la carpeta del proyecto: cd youtube_comments

Crear el entorno virtual: python -m venv .venv

Activar entorno virtual: .venv\Scripts\activate

Instalar dependencias: pip install -r requirements.txt

Configurar variables de entorno:

Renombrar el archivo .env.example a .env
Obtener una API KEY de YouTube (YouTube Data API v3)
Añadir tu API KEY en el archivo .env
Uso
En el terminal:

Ejecutar la aplicación: python main.py
Ingresar la URL del video de YouTube.
¡Listo! Tu resultado se habrá guardado en la carpeta 'outputs' como un archivo CSV.
Licencia
Este proyecto está bajo la Licencia MIT.
