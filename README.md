# Video Downloader: Versión beta 1.0.0

Este programa codificado en Python 3.12.5 permite al usuario insertar la URL de un vídeo de youtube.com y crear 3 archivos con la extensión ".mp4".

1. audio.mp3
2. video.mp3
3. final_result.mp3

La forma en la que el código funciona es la siguiente:

Primero detecta si tienes las credenciales "visitor_data" y "po_token". En el caso de tenerlas, empieza la descarga. En el caso de no tenerlas, el maravilloso programa de python
de unixfox (https://github.com/iv-org/youtube-trusted-session-generator) creará esas dos credenciales y las transmitirá al programa principal.

## Librerías usadas:

pytubefix==6.15.4
pillow==10.4.0
customtkinter==5.2.2

## Instrucciones de instalación:

El usuario debe tener instalado FFmpeg (https://www.gyan.dev/ffmpeg/builds/). En el caso de ser un novato en cuanto a añadir programas a el PATH de su ordenador, el siguiente 
artículo de WikiHow explica de una forma muy clara y sencilla cómo instalar y añadir al PATH FFmpeg (https://www.wikihow.com/Install-FFmpeg-on-Windows)

### Windows (único sistema operativo con una distribución)

El archivo ejecutable se encuentra dentro de la carpeta "main.dist". El nombre del archivo ejecutable es main.exe. Para ejecutar el programa sólo se necesita abrir el archivo ejecutable y listo.

## Feedback y errores:

Si hay algún error, por favor abra una discusión aquí: (https://github.com/hacker-3342/VideoDownloader/issues). Introduzca los pasos para reproducir el error, qué estaba haciendo antes de recibir el error y si está usando la versión más reciente del programa. Los errores en versiones más antiguas **NO SE ATENDERÁN.**

Si desea enviarme feedback sobre el código, por favor escriba un email a la siguiente dirección de correo electrónico: (hectoruru@outlook.es). ¡Toda ayuda se aprecia!