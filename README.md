An easy-to-use Spotify to MP3 converter with modern and simple UI.


How to Install
--------------

1. Install flash, yt_dlp and tekore using the commands one-by-one


          pip install yt_dlp
          pip install flask
          pip install tekore
2. Go to https://www.gyan.dev/ffmpeg/builds/ and install "Essentials" zip, extract it into a folder and go to "edit the system enviroment variables"
  then enviroment variables and then under system section go to path and click 'edit' then click new and add the path of the bin folder from ffmpeg directrory.
3. Go to Spotify Developers Portal and sign in and then create an webapp. Put the name and description as whatever you wish, for redirect url put http://127.0.0.1:5000/.
4. Copy your client id. client secret and paste it at the required position in mainwebapp.py(highlighted by comments).
5. Now simply run the file and go to the url given in terminal!
-------------

This is a simple yet effective project i decided to make as a means of getting my hands into basic web development.
