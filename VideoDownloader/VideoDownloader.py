#! usr/bin/env/python3

from pytubefix import YouTube
import customtkinter as ct
import threading
import os
import subprocess

print("Current working directory:", os.getcwd())

app = ct.CTk()
app.geometry("650x450")
app.title("VideoDownloader")

def combine_video_audio(video_path, audio_path, output_path):
    """Combines video and audio into one file using FFmpeg."""
    command = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{output_path}" -y'
    subprocess.run(command, shell=True)

def start_download():
    """Handles the video download process in a separate thread."""
    yt = YouTube(url.get(), use_po_token=True)

    # Select the highest resolution video-only stream
    video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()

    # Select the highest quality audio-only stream
    audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

    popup = None

    if video_stream and audio_stream:
        # Download video and audio separately
        while True:
            try:
                # Use the user-defined path
                user_path = thepath.get()
                video_path = video_stream.download(filename="video.mp4", output_path=user_path)
                audio_path = audio_stream.download(filename="audio.mp4", output_path=user_path)
                break
            except TypeError:
                if popup is None:
                    popup = ct.CTkToplevel(app)
                    badpath = ct.CTkLabel(popup, text="The path you introduced wasn't found, please try again.", width=400)
                    badpath.pack(padx=(20, 0), pady=(20, 20))
                app.update()

        # Combine video and audio using the user-defined path
        final_output_path = os.path.join(user_path, "final_output.mp4")
        if useffmpeg.get() == 1:
            combine_video_audio(video_path, audio_path, final_output_path)

        print(f"Download complete: {final_output_path}")
    else:
        print("No suitable streams found!")

    theprogressbar.stop()

    finished_downloading = ct.CTkLabel(app, text="The download has finished successfully!", text_color="#008000")
    finished_downloading.pack(padx=(20, 0), pady=(20, 20))

def start():
    """Starts the progress bar and the download thread."""
    global theprogressbar
    theprogressbar = ct.CTkProgressBar(app, orientation="horizontal", mode="indeterminate")
    theprogressbar.pack(padx=(20, 0), pady=(20, 20))
    theprogressbar.start()

    # Create and start a new thread for downloading the video
    download_thread = threading.Thread(target=start_download)
    download_thread.start()


url = ct.CTkEntry(app, placeholder_text="URL here", width=340)
url.pack(padx=(20, 0), pady=(20, 20))

thepath = ct.CTkEntry(app, placeholder_text="Path on which the output will be stored", width=340)
thepath.pack(padx=(20, 0), pady=(20, 20))

useffmpeg = ct.CTkSwitch(app, text="Combine video and audio (requires FFmpeg to be installed and in the system's PATH)")
useffmpeg.pack(padx=(20, 0), pady=(20, 20))

button = ct.CTkButton(app, text="Download", command=start)
button.pack(padx=(20, 0), pady=(20, 20))


app.mainloop()
