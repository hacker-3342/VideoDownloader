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
    ffmpeg_command = f'ffmpeg -i "{video_path}" -i "{audio_path}" -c:v copy -c:a aac "{output_path}" -y'
    subprocess.run(ffmpeg_command, shell=True)

def start_download():
    pytubefix_main_func = YouTube(user_entry_url.get(), use_po_token=True)
    bad_url_popup = ct.CTkToplevel(app)
    bad_url_text = ct.CTkLabel(bad_url_popup, text="The URL you entered isn't valid, please try again.")
    bad_url_text.pack(padx=(10, 0), pady=(10, 0))
        
    app.update()

    video_stream = pytubefix_main_func.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()

    audio_stream = pytubefix_main_func.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

    no_path_popup = None

    if video_stream and audio_stream:
        while True:
            try:
                user_path = user_entry_path.get()
                video_path = video_stream.download(filename="video.mp4", output_path=user_path)
                audio_path = audio_stream.download(filename="audio.mp4", output_path=user_path)
                break
            except TypeError:
                if no_path_popup is None:
                    no_path_popup = ct.CTkToplevel(app)
                    bad_path_text = ct.CTkLabel(no_path_popup, text="The path you introduced wasn't found, please try again.", width=400)
                    bad_path_text.pack(padx=(10, 0), pady=(10, 0))
                app.update()

        final_output_path = os.path.join(user_path, "final_output.mp4")
        if user_useffmpeg.get() == 1:
            combine_video_audio(video_path, audio_path, final_output_path)

        print(f"Download complete: {final_output_path}")
    else:
        print("No suitable streams found!")

    theprogressbar.stop()

    finished_downloading = ct.CTkLabel(app, text="The download has finished successfully!", text_color="#008000")
    finished_downloading.pack(padx=(10, 0), pady=(10, 0))

def start():
    global theprogressbar
    theprogressbar = ct.CTkProgressBar(app, orientation="horizontal", mode="indeterminate")
    theprogressbar.pack(padx=(10, 0), pady=(10, 0))
    theprogressbar.start()

    download_thread = threading.Thread(target=start_download)
    download_thread.start()


user_entry_url = ct.CTkEntry(app, placeholder_text="URL here", width=340)
user_entry_url.pack(padx=(10, 0), pady=(10, 0))

user_entry_path = ct.CTkEntry(app, placeholder_text="Path on which the output will be stored", width=340)
user_entry_path.pack(padx=(10, 0), pady=(10, 0))

user_useffmpeg = ct.CTkSwitch(app, text="Combine video and audio (requires FFmpeg to be installed and in the system's PATH)")
user_useffmpeg.pack(padx=(15, 0), pady=(15, 0))

download_start_button = ct.CTkButton(app, text="Download", command=start)
download_start_button.pack(padx=(20, 0), pady=(20, 0))


app.mainloop()
