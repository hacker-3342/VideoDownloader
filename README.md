<!-- markdownlint-disable-next-line -->
<p align="center">
  <img src="https://github.com/user-attachments/assets/3c732821-a248-4f94-96d6-8f0a780de016" alt="image" />
</p>

<div align="center">
  <h1>VideoDownloader</h1>
</div>

<div align="center">

![License](https://img.shields.io/github/license/hacker-3342/VideoDownloader)
![Version](https://img.shields.io/github/v/release/hacker-3342/VideoDownloader)
![GitHub Issues](https://img.shields.io/github/issues/hacker-3342/VideoDownloader)
![GitHub Stars](https://img.shields.io/github/stars/hacker-3342/VideoDownloader?style=social)
![GitHub Forks](https://img.shields.io/github/forks/hacker-3342/VideoDownloader?style=social)
![Contributors](https://img.shields.io/github/contributors/hacker-3342/VideoDownloader)
![Platform](https://img.shields.io/badge/platform-windows%20|%20macos%20|%20linux-brightgreen)

</div>

This project is licensed under the [GNU General Public License v3.0](LICENSE).

If you are interested in collaborating, please check out the VideoDownloader trello board: [Trello Board](https://trello.com/invite/b/66f30aed55d15301b18d88ca/ATTIe726635443f96d7ed98c31a6e7850bcb742B1501/videodownloader)

You should have received a copy of the GNU General Public License along with this project. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

If Windows SmartScreen blocks the program, press "More information" and then "Run anyway".

![image](https://github.com/user-attachments/assets/8890bb64-dff0-4783-8d38-cb20c042426c)

This program coded in Python 3 allows the user to insert the URL of a video from youtube.com and create an mp4 file and an m4a file (video and audio).

*The mp4 file will only have both video and audio if the "Use ffmpeg" switch is toggled and FFmpeg is installed.

## Libraries used:

All libraries used are in the 'requirements.txt' file.

## Installation instructions:

The user must have FFmpeg (https://www.gyan.dev/ffmpeg/builds/) installed if they want to use the "Combine into a single file" feature. FFmpeg isn't needed for the rest of the program. 

### Binaries:

#### Windows

Run the setup guided installer.
There will be a portable version in the future.

#### MacOS

Choose your .zip file depending on your Mac's chip architecture. x86_64 for Intel chips, ARM for M1, M2... 
Run the .app file and you are done.

#### Linux

Run the executable file and you are done.
Some text and rendering may look strange, this is due to some CustomTkinter rendering issues on Linux.

Warning:
The Wayland compositor could have issues rendering GUI apps in Python. Using X11 is recommended, but if Wayland is your only option, go ahead and try it.

### Source code

Download the source code.
Create a virtual environment (not necessary, but recommended):
```
python3 -m venv <your environment name here>
```
Activate the virtual environment:

Windows:
```
& <environment name>/Scripts/activate.ps1
```
MacOS and Linux:
```
source <environment name>/bin/activate
```
Install the requirements:
```
pip install -r requirements.txt
```
Run the VideoDownloader.py file:
```
python3 VideoDownloader.py
```

## Feedback and issues:

If there are any errors, please open a discussion here: (https://github.com/hacker-3342/VideoDownloader/issues). Enter the steps to reproduce the error, what you were doing before you received the error and try to provide screenshots and your code.

If you would like to send me feedback on the code, please email me at the following email address: (hectoruru@outlook.es) or start a discussion. All help is appreciated!
