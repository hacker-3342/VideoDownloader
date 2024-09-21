#!/usr/bin/env python3.12

import yt_dlp
import customtkinter as ct
import threading

app = ct.CTk()
app.title("VideoDownloader")
app.geometry("660x440")

def create_progress_bar():
    user_download_progressbar.pack(pady=(20, 0))
    user_download_progressbar.start()

def download_video():
    url = user_url_entry.get()
    save_path = user_path_entry.get()

    if user_useffmpeg_switch.get() == 1:
        # Using FFmpeg to merge video and audio
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Merge video and audio if FFmpeg is selected
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'quiet': False,
            'noprogress': True,
            'merge_output_format': 'mp4',  # Allow merging into mp4 if FFmpeg is selected
        }
    else:
        # Downloading video and audio separately, without merging
        ydl_opts = {
            'format': 'bestvideo[ext=mp4], bestaudio[ext=m4a]/best',  # Separate video and audio files
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Save separately
            'quiet': False,
            'noprogress': True,
            'postprocessors': [],  # Disable automatic merging of video and audio
            'merge_output_format': None,  # Explicitly prevent merging
            'keepvideo': True,  # Optionally, keep video and audio files
        }

    # Start the download process
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Stop the progress bar after download finishes
    app.after(0, user_download_progressbar.stop)

def start_download():
    thread_download = threading.Thread(target=download_video)
    thread_download.start()

    create_progress_bar()

# Input fields and UI elements
user_url_entry = ct.CTkEntry(app, placeholder_text="YouTube URL", width=330)
user_url_entry.pack(pady=(10, 0))

user_path_entry = ct.CTkEntry(app, placeholder_text="Path on which the video will be downloaded", width=330)
user_path_entry.pack(pady=(10, 0))

# Switch for FFmpeg usage
user_useffmpeg_switch = ct.CTkSwitch(app, text="Use FFmpeg to merge video and audio files")
user_useffmpeg_switch.pack(pady=(10, 0))

# Button to start download
user_download_button = ct.CTkButton(app, text="Start Download", command=start_download)
user_download_button.pack(pady=(20, 0))

# Progress bar (packed during download)
user_download_progressbar = ct.CTkProgressBar(app, mode="indeterminate")

app.mainloop()
