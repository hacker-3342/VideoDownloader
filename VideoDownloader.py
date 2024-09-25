#!/usr/bin/env python3.12

import yt_dlp
import customtkinter as ct
import threading

app = ct.CTk()
app.title("VideoDownloader")
app.geometry(f"{620}x{330}")

def create_progress_bar():
    user_download_progressbar.pack(pady=(20, 0))
    user_download_progressbar.start()

def download_video():
    url = user_url_entry.get()
    save_path = user_path_entry.get()

    if user_useffmpeg_switch.get() == 1:
        # Using FFmpeg to merge video and audio
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'quiet': False,
            'noprogress': True,
            'merge_output_format': 'mp4',
        }
    else:
        # Downloading video and audio separately, without merging
        ydl_opts = {
            'format': 'bestvideo[ext=mp4], bestaudio[ext=m4a]/best',
            'outtmpl': f'{save_path}/%(title)s.%(ext)s',
            'quiet': False,
            'noprogress': True,
            'postprocessors': [],
            'merge_output_format': None,
            'keepvideo': True,
        }

    # I have no fucking idea what the following 2 lines do, I just know they start the download
    # (I haven't learnt the "with" function yet)
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Stop the progress bar after download finishes
    app.after(0, user_download_progressbar.destroy)

    # Create popup to notify user of finished download
    user_popup = ct.CTkToplevel(app)
    user_popup.geometry("360x220")
    user_finished_download = ct.CTkLabel(user_popup, text="Download finished successfully.", text_color="#659701")
    user_finished_download.grid(row=0, column=0, padx=10, pady=10)

def start_download():
    thread_download = threading.Thread(target=download_video)
    thread_download.start()

    create_progress_bar()

def apply_theme():
    if user_theme_dropdown.get() == "System":
        ct.set_appearance_mode("system")
    elif user_theme_dropdown.get() == "Light":
        ct.set_appearance_mode("light")
    else:
        ct.set_appearance_mode("dark")

# Configure grid layout
app.grid_columnconfigure(0, weight=0)  # Sidebar column
app.grid_columnconfigure(1, weight=1)  # Main content column
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

# Sidebar
sidebar_frame = ct.CTkFrame(app, width=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsw")
sidebar_frame.grid_rowconfigure(0, weight=1)

# Input fields and UI elements
user_url_entry = ct.CTkEntry(app, placeholder_text="YouTube URL", width=330)
user_url_entry.grid(row=0, column=1, padx=20, pady=10, sticky="ew")

user_path_entry = ct.CTkEntry(app, placeholder_text="Path on which the video will be downloaded", width=330)
user_path_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

# Label to advise of necessary FFmpeg usage
user_ffmpeg_label = ct.CTkLabel(
    app,
    text="All options marked with a '*' will only be functional if FFmpeg is installed.",
    text_color="red"
)
user_ffmpeg_label.grid(row=2, column=1, padx=20, pady=10, sticky="w")

# Switch for FFmpeg usage
user_useffmpeg_switch = ct.CTkSwitch(app, text="Use FFmpeg to merge video and audio files*")
user_useffmpeg_switch.grid(row=3, column=1, padx=20, pady=10, sticky="ew")

# Button to start download
user_download_button = ct.CTkButton(app, text="Start Download", command=start_download)
user_download_button.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

# Dropdown menu to set themes
user_theme_dropdown = ct.CTkComboBox(sidebar_frame, values=["System", "Light", "Dark"])
user_theme_dropdown.grid(row=1, column=0, padx=10, pady=5, sticky="sw")

# Button to apply theme
user_theme_applybutton = ct.CTkButton(sidebar_frame, text="Apply", command=apply_theme)
user_theme_applybutton.grid(row=2, column=0, padx=10, pady=10, sticky="sw")

# VideoDownloader sidebar text
videodownloader_text = ct.CTkLabel(sidebar_frame, text="VideoDownloader", font=ct.CTkFont(size=17, weight="bold"))
videodownloader_text.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

# Progress bar (packed during download)
user_download_progressbar = ct.CTkProgressBar(app, mode="indeterminate")

app.mainloop()
