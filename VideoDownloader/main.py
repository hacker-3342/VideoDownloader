#!/usr/bin/env python3

from pytubefix import YouTube
import customtkinter as ct
import threading
import subprocess
import index
import json

def get_po_token_and_visitor_data():
    """Runs index.py and captures po_token and visitor_data."""
    result = subprocess.run(
        ['python', 'index.py'],  # Adjust this to the correct path if necessary
        capture_output=True,
        text=True
    )
    
    try:
        data = json.loads(result.stdout)
        po_token = data.get('po_token')
        visitor_data = data.get('visitor_data')
        return po_token, visitor_data
    except json.JSONDecodeError:
        print("Error: Could not decode JSON output from index.py")
        return None, None



app = ct.CTk()
app.geometry("550x450")
app.title("Youtube Video Downloader")

url = ct.CTkEntry(app, placeholder_text="URL here", width=340)
url.pack(padx=(20, 0), pady=(20, 20))

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

    if video_stream and audio_stream:
        # Download video and audio separately
        video_path = video_stream.download(filename="video.mp4")
        audio_path = audio_stream.download(filename="audio.mp4")

        # Combine video and audio
        output_path = "final_output.mp4"
        combine_video_audio(video_path, audio_path, output_path)

        print(f"Download complete: {output_path}")
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

button = ct.CTkButton(app, text="Download", command=start)
button.pack(padx=(20, 0), pady=(20, 20))

app.mainloop()
