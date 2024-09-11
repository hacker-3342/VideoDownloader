# Video Downloader: Versión 1.0.1

# Español:

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

Si ha añadido FFmpeg a el PATH de su sistema, pero todavía Windows no reconoce FFmpeg desde la terminal, pruebe a hacer lo siguiente:

![image](https://github.com/user-attachments/assets/45b4a3f9-1796-4961-b580-89a0e3011fd2)

### Windows (único sistema operativo con una distribución)

El archivo ejecutable se encuentra dentro de la carpeta "main.dist". El nombre del archivo ejecutable es main.exe. Para ejecutar el programa sólo se necesita abrir el archivo ejecutable y listo.

## Feedback y errores:

Si hay algún error, por favor abra una discusión aquí: (https://github.com/hacker-3342/VideoDownloader/issues). Introduzca los pasos para reproducir el error, qué estaba haciendo antes de recibir el error y si está usando la versión más reciente del programa. Los errores en versiones más antiguas **NO SE ATENDERÁN.**

Si desea enviarme feedback sobre el código, por favor escriba un email a la siguiente dirección de correo electrónico: (hectoruru@outlook.es). ¡Toda ayuda se aprecia!

# English:

This program coded in Python 3.12.5 allows the user to insert the URL of a video from youtube.com and create 3 files with the extension “.mp4”.

1. audio.mp3
2. video.mp3
3. final_result.mp3

The way the code works is as follows:

First it detects if you have the credentials “visitor_data” and “po_token”. If you have them, it starts the download. In case you don't have them, the wonderful python program
of unixfox (https://github.com/iv-org/youtube-trusted-session-generator) will create those two credentials and transmit them to the main program.

## Libraries used:

pytubefix==6.15.4
pillow==10.4.0
customtkinter==5.2.2

## Installation instructions:

The user must have FFmpeg (https://www.gyan.dev/ffmpeg/builds/) installed. In case you are new to adding programs to your computer's PATH, the following WikiHow article explains how to do it. 
WikiHow article explains in a very clear and simple way how to install and add FFmpeg (https://www.wikihow.com/Install-FFmpeg-on-Windows) to the PATH.

If you have added FFmpeg to your system PATH, but Windows still does not recognize FFmpeg from the terminal, try doing the following:

![image](https://github.com/user-attachments/assets/45b4a3f9-1796-4961-b580-89a0e3011fd2)

### Windows (only operating system with a distribution)

The executable file is located inside the “main.dist” folder. The name of the executable file is main.exe. To run the program just open the executable file and you are done.

## Feedback and issues:

If there are any errors, please open a discussion here: (https://github.com/hacker-3342/VideoDownloader/issues). Enter the steps to reproduce the error, what you were doing before you received the error, and if you are using the most recent version of the program. Errors in older versions **WON'T BE ATTENDED**.

If you would like to send me feedback on the code, please email me at the following email address: (hectoruru@outlook.es). All help is appreciated!
