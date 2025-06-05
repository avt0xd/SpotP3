from flask import Flask, redirect, url_for, render_template, request,send_file
import tekore as tk
import yt_dlp as yt
import os
import uuid
import shutil

app = Flask(__name__)
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

# Initialise the client

cred = tk.Credentials('client_id', 'client secret')  #Enter both inside the inverted commas
token = cred.request_client_token()
spotify = tk.Spotify(token)


def download(link):
    
    session_id = str(uuid.uuid4())
    folder_path = os.path.join(DOWNLOAD_DIR, session_id)
    os.makedirs(folder_path)
    
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(folder_path, '%(title)s.%(ext)s'),
        'ffmpeg_location': r'path here',  #Enter the path inside the inverted commas
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    
    playlist_id=link[34:56]

    # Get playlist tracks
    playlist = spotify.playlist_items(playlist_id)

    print("Tracks in playlist:")
    for item in playlist.items:
        track = item.track
        print(f"{track.name} – {track.artists[0].name}")
        print(f"Downloading song")
        try:    
            with yt.YoutubeDL(ydl_opts) as ydl:
                ydl.download([f'ytsearch:{track.name+track.artists[0].name}'])
        except Exception as e:
            return f"Error: {str(e)}"    
    
    zip_path = os.path.join(DOWNLOAD_DIR, f"{session_id}.zip")
    shutil.make_archive(zip_path.replace('.zip', ''), 'zip', folder_path)

    # Clean up mp3 folder
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