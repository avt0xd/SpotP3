from enum import Enum
from flask import Flask, redirect, url_for, render_template, request,send_file
import tekore as tk
import yt_dlp as yt
import os
import uuid
import shutil

app = Flask(__name__)
from pathlib import Path
import platform
DOWNLOAD_DIR = Path.home() / "Downloads"

os_name = platform.system()

# Initialise the client

cred = tk.Credentials('d26ac3a70d6e48549a5798948e40f696', '2099a8cb775b4c29a02dd735b4d0b21f')  #Enter both inside the inverted commas
token = cred.request_client_token()
import shutil
class TextColor(Enum):
    BLACK   = '\033[30m'
    RED     = '\033[31m'
    GREEN   = '\033[32m'
    YELLOW  = '\033[33m'
    BLUE    = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN    = '\033[36m'
    WHITE   = '\033[37m'
    BRIGHT_BLACK   = '\033[90m'
    BRIGHT_RED     = '\033[91m'
    BRIGHT_GREEN   = '\033[92m'
    BRIGHT_YELLOW  = '\033[93m'
    BRIGHT_BLUE    = '\033[94m'
    RESET   = '\033[0m'

def colortxt(text, color):
    return f"{color.value}{text}{TextColor.RESET.value}"
ffmpeg_path = shutil.which("ffmpeg")
if not ffmpeg_path:
    print(colortxt("The requirement ffmpeg was not found. Please install ffmpeg"), TextColor.RED)
    print(colortxt("⚠️ Make sure to add it to PATH ⚠️", TextColor.BRIGHT_YELLOW))
    exit()
spotify = tk.Spotify(token)


from concurrent.futures import ThreadPoolExecutor

def download(link):
    session_id = str(uuid.uuid4())
    folder_path = os.path.join(DOWNLOAD_DIR, session_id)
    os.makedirs(folder_path)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': ffmpeg_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True
    }

    playlist_id = link[34:56]
    playlist = spotify.playlist_items(playlist_id)

    tasks = []

    def download_track(track_name, artist_name):
        search_query = f"ytsearch:{track_name} {artist_name}"
        try:
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([search_query])
            print(colortxt(f"✔ Downloaded: {track_name} – {artist_name}", TextColor.GREEN))
        except Exception as e:
            print(colortxt(f"✖ Failed: {track_name} – {artist_name}: {e}", TextColor.RED))

    with ThreadPoolExecutor(max_workers=5) as executor:
        for item in playlist.items:
            track = item.track
            tasks.append(executor.submit(download_track, track.name, track.artists[0].name))

    for task in tasks:
        task.result() 

    zip_path = os.path.join(DOWNLOAD_DIR, f"Spotify_2_MP3_Pack_{session_id}.zip")
    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', folder_path)
    shutil.rmtree(folder_path)

    return zip_path


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        global link
        link = request.form.get("spotify_link")
        if not link:
            return "No link provided", 400
        global zip_file
        zip_file = download(link)
        return send_file(zip_file, as_attachment=True)
    return render_template("main.html")

@app.route("/how-it-works")
def how_it_works():
    return render_template("how.html")

@app.route("/contact-me")
def contact():
    return render_template("contact.html")




if __name__=="__main__":
    app.run(debug=True)
