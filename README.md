# VideoDownloader Suite: Versión 1.1.0

## License

This project is licensed under the [GNU General Public License v3.0](LICENSE).

You should have received a copy of the GNU General Public License along with this project. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

![image](https://github.com/user-attachments/assets/a6d28209-a21c-4746-a25f-6511b4326e58)

# English:

IF Windows SmartScreen blocks the program, press "More information" and then "Run anyway".

![image](https://github.com/user-attachments/assets/8890bb64-dff0-4783-8d38-cb20c042426c)

This program coded in Python 3.12.5 allows the user to insert the URL of a video from youtube.com and create 3 files with the extension “.mp4”.

1. audio.mp3
2. video.mp3
3. final_result.mp3 (only available of FFmpeg is installed properly)

The way the code works is as follows:

First it detects if you have the credentials “visitor_data” and “po_token”. If you have them, it starts the download. In case you don't have them, the program CredentialGenerator.py will provide you those.
When you get your credentials, you can paste them onto the terminal of the main program and wait for the download to finish.

## Libraries used:

pytubefix==6.15.4
pillow==10.4.0
customtkinter==5.2.2
websockets==13.0.1
nodriver==0.32

## Installation instructions:

The user must have FFmpeg (https://www.gyan.dev/ffmpeg/builds/) installed if they want to use the "Combine into a single file" feature. FFmpeg isn't needed for the rest of the program. In case you are new to adding programs to your computer's PATH, the following WikiHow article explains how to do it. 
WikiHow article explains in a very clear and simple way how to install and add FFmpeg (https://www.wikihow.com/Install-FFmpeg-on-Windows) to the PATH.

If you have added FFmpeg to your system PATH, but Windows still does not recognize FFmpeg from the terminal, try doing the following:

![image](https://github.com/user-attachments/assets/45b4a3f9-1796-4961-b580-89a0e3011fd2)

### Windows (only operating system with a distribution)

The executable file is located inside the “VideoDownloader.dist” folder. The name of the executable file is VideoDownloader.exe. To run the program just open the executable file and you are done.
Same is said about the CredentialGenerator executable file. It is in the "CredentialGenerator.dist".

## Feedback and issues:

If there are any errors, please open a discussion here: (https://github.com/hacker-3342/VideoDownloader/issues). Enter the steps to reproduce the error, what you were doing before you received the error, and if you are using the most recent version of the program. Errors in older versions **WON'T BE ATTENDED**.

If you would like to send me feedback on the code, please email me at the following email address: (hectoruru@outlook.es). All help is appreciated!

# Español:

SI Windows SmartScreen bloquea el programa, pulse «Más información» y luego «Ejecutar de todos modos».

![image](https://github.com/user-attachments/assets/8890bb64-dff0-4783-8d38-cb20c042426c)

Este programa codificado en Python 3.12.5 permite al usuario insertar la URL de un video de youtube.com y crear 3 archivos con la extensión «.mp4».

1. audio.mp3
2. video.mp3
3. final_result.mp3 (sólo disponible si FFmpeg está instalado correctamente)

El funcionamiento del código es el siguiente:

Primero detecta si tienes las credenciales «visitor_data» y «po_token». Si las tienes, inicia la descarga. En caso de que no las tengas, el programa CredentialGenerator.py te las proporcionará.
Cuando tengas tus credenciales, puedes pegarlas en el terminal del programa principal y esperar a que termine la descarga.

## Librerías usadas:

pytubefix==6.15.4
pillow==10.4.0
customtkinter==5.2.2
websockets==13.0.1
nodriver==0.32

## Instrucciones de instalación:

El usuario debe tener FFmpeg (https://www.gyan.dev/ffmpeg/builds/) instalado si quiere usar la función «Combinar en un solo archivo». FFmpeg no es necesario para el resto del programa. En caso de que seas nuevo en esto de añadir programas al PATH de tu ordenador, el siguiente artículo de WikiHow explica cómo hacerlo. 
El artículo de WikiHow explica de forma muy clara y sencilla cómo instalar y añadir FFmpeg (https://www.wikihow.com/Install-FFmpeg-on-Windows) al PATH.

Si has añadido FFmpeg al PATH de tu sistema, pero Windows sigue sin reconocer FFmpeg desde el terminal, prueba a hacer lo siguiente:

![image](https://github.com/user-attachments/assets/45b4a3f9-1796-4961-b580-89a0e3011fd2)

### Windows (único sistema operativo con distribución)

El archivo ejecutable se encuentra dentro de la carpeta «VideoDownloader.dist». El nombre del archivo ejecutable es VideoDownloader.exe. Para ejecutar el programa basta con abrir el archivo ejecutable y listo.
Lo mismo ocurre con el archivo ejecutable CredentialGenerator. Se encuentra en el «CredentialGenerator.dist».

## Comentarios y problemas:

Si hay algún error, por favor abra una discusión aquí: (https://github.com/hacker-3342/VideoDownloader/issues). Introduce los pasos para reproducir el error, qué estabas haciendo antes de recibir el error, y si estás usando la versión más reciente del programa. Los errores en versiones anteriores **NO SERÁN ATENDIDOS**.

Si desea enviarme comentarios sobre el código, envíeme un correo electrónico a la siguiente dirección (hectoruru@outlook.es). ¡Toda ayuda es apreciada!
