#!/usr/bin/env python3.12

import yt_dlp
import customtkinter as ctk
import threading
from CTkMessagebox import CTkMessagebox
from PIL import Image
import sys
import os
import subprocess
import platform

app = ctk.CTk()
app.title("VideoDownloader")
app.geometry(f"{770}x{428}")

# Declare the variable as global here
invalid_url = False
invalid_save_path = False

# Load the image using PIL
logo = Image.open("Assets/logo.png")
logo_image = ctk.CTkImage(light_image=logo, dark_image=logo)

import subprocess
import sys
import os

def open_folder(path):
    if sys.platform.startswith('linux'):
        subprocess.Popen(['xdg-open', path])
    elif sys.platform == 'win32':
        os.startfile(path)
    elif sys.platform == 'darwin':  # For macOS
        subprocess.Popen(['open', path])

def show_checkmark():
    global answer
    # Show the popup with "Reveal location" and "OK" options
    answer = CTkMessagebox(message="The download was finished successfully.", icon="check", option_1="Reveal location", option_2="Ok", button_color="#ff4a38", button_hover_color="#9e2d23").get()
    
    # If the user clicks "Reveal location"
    if answer == "Reveal location":
        # Open the folder in the file explorer
        open_folder(user_path_entry.get())

def show_checkmark_error():
    global invalid_url, invalid_save_path  # Reference the global variables
    message = ""
    if invalid_url:
        message = "Error: The inserted URL is invalid. Try again."
    elif invalid_save_path:
        message = "Error: The inserted save path is invalid. Try again."
    else:
        message = "There was an error. Please write an issue in our GitHub repository to help."

    # Show the error popup and wait for the user's response
    def show_popup():
        response = CTkMessagebox(title="Error while downloading", 
                                  message=message, 
                                  icon="warning" if invalid_url or invalid_save_path else "cancel", 
                                  option_1="Try again").get()
        # Restart the application if "Try again" is clicked
        if response == "Try again":
            python = sys.executable  # Get the path to the Python interpreter
            os.execv(python, ['python'] + sys.argv)  # Restart the program

    app.after(0, show_popup)  # Use after to schedule GUI update in the main thread

def download_video():
    global invalid_url, invalid_save_path  # Reference the global variables
    url = user_url_entry.get()
    save_path = user_path_entry.get()

    # Disable all buttons and entries
    user_url_entry.configure(state="disabled")
    user_path_entry.configure(state="disabled")
    user_useffmpeg_switch.configure(state="disabled")
    user_download_button.configure(state="disabled")

    # Base options for downloading
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a',  # Ensure this is correct
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',  # Set output template
        'postprocessors': [],  # Start with no post-processing
    }

    # Check if URL is valid (e.g., starts with "https://")
    if url.startswith("https://"):
        invalid_url = False  # URL is valid
        if os.path.exists(save_path):
            invalid_save_path = False  # Save path is valid
            try:
                if user_useffmpeg_switch.get() == 1:
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio/best',
                        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                        'quiet': True,
                        'noprogress': True,
                        'merge_output_format': 'mp4',
                    }
                else:
                    ydl_opts = {
                        'format': 'bestvideo[ext=mp4], bestaudio[ext=m4a]/best',
                        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
                        'quiet': True,
                        'noprogress': True,
                        'merge_output_format': None,
                        'keepvideo': True,
                    }

                # Download video and audio
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])

                # Create popup to notify user of finished download
                app.after(0, show_checkmark)

                # Re-enable the buttons and entries
                app.after(0, enable_widgets)
            except Exception as e:
                print(f"An error occurred: {e}")  # Print error for debugging
                app.after(0, show_checkmark_error)  # Schedule error popup in main thread
        else:
            invalid_save_path = True
            app.after(0, show_checkmark_error)  # Schedule error popup in main thread
    else:
        invalid_url = True  # URL is invalid
        app.after(0, show_checkmark_error)  # Schedule error popup in main thread


def enable_widgets():
    user_url_entry.configure(state="normal")
    user_path_entry.configure(state="normal")
    user_useffmpeg_switch.configure(state="normal")
    user_download_button.configure(state="normal")

def start_download():
    thread_download = threading.Thread(target=download_video)
    thread_download.start()

def apply_theme():
    if user_theme_dropdown.get() == "System":
        ctk.set_appearance_mode("system")
    elif user_theme_dropdown.get() == "Light":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")

# Configure grid layout
app.grid_columnconfigure(0, weight=0)  # Sidebar column
app.grid_columnconfigure(1, weight=1)  # Main content column
app.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight=1)

# Sidebar
sidebar_frame = ctk.CTkFrame(app, width=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=6, sticky="nsw")
sidebar_frame.grid_rowconfigure(0, weight=1)

# Input fields and UI elements
user_url_entry = ctk.CTkEntry(app, placeholder_text="YouTube URL", width=330)
user_url_entry.grid(row=1, column=1, padx=20, pady=10, sticky="ew")

user_path_entry = ctk.CTkEntry(app, placeholder_text="Path on which the video will be downloaded", width=330)
user_path_entry.grid(row=2, column=1, padx=20, pady=10, sticky="ew")

# Label to advise of necessary FFmpeg usage
user_ffmpeg_label = ctk.CTkLabel(
    app,
    text="All options marked with a '*' will only be functional if FFmpeg is installed.",
    text_color="red"
)
user_ffmpeg_label.grid(row=3, column=1, padx=20, pady=10, sticky="w")

# Switch for FFmpeg usage
user_useffmpeg_switch = ctk.CTkSwitch(app, text="Use FFmpeg to merge video and audio files*", progress_color="#ff4a38")
user_useffmpeg_switch.grid(row=4, column=1, padx=20, pady=10, sticky="ew")

# Button to start download
user_download_button = ctk.CTkButton(app, text="Start Download", command=start_download, fg_color="#ff4a38", hover_color="#9e2d23")
user_download_button.grid(row=5, column=1, padx=20, pady=10, sticky="ew")

# Dropdown menu to set themes
user_theme_dropdown = ctk.CTkComboBox(sidebar_frame, values=["System", "Light", "Dark"])
user_theme_dropdown.grid(row=6, column=0, padx=10, pady=10, sticky="sw")

# Button to apply theme
user_theme_applybutton = ctk.CTkButton(sidebar_frame, text="Apply", command=apply_theme, fg_color="#ff4a38", hover_color="#9e2d23")
user_theme_applybutton.grid(row=7, column=0, padx=10, pady=11.5, sticky="sw")

my_image = ctk.CTkImage(light_image=Image.open("Assets/logo-light.png"),
                                  dark_image=Image.open("Assets/logo-dark.png"),
                                  size=(500, 150))

image_label = ctk.CTkLabel(app, image=my_image, text="")  # display image with a CTkLabel
image_label.grid(row=0, column=1, padx=10, pady=10)  # Add this line to place the label

app.mainloop()
