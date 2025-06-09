An easy-to-use Spotify to MP3 converter with modern and simple UI.


How to Install
--------------

1. Install flash, yt_dlp and tekore using the commands one-by-one


          pip install yt_dlp
          pip install flask
          pip install tekore
2. Go to https://www.gyan.dev/ffmpeg/builds/ and install "Essentials" zip, extract it into a folder and go to "edit the system enviroment variables"
  then enviroment variables and then under system section go to path, click 'edit' then click new and add the path of the bin folder from ffmpeg directrory.
3. Go to Spotify Developers Portal, sign-in to create a webapp. Write the name and description as whatever you wish, for redirect url paste http://127.0.0.1:5000/.
4. Copy your client id., client secret and paste at the required position in mainwebapp.py(highlighted by comments).
5. Now simply run the file and visit the url given in terminal!
-------------

This is a simple yet effective project I decided to make as a means of getting my hands into basic web development.

Changes(9 June, 2025)
--------------------
1. Added support for Threading, i.e. now multiple songs can download simultaneously thereby reducing the waiting time.
2. Reduced the clutter in terminal while downloading songs by a simple message of confirmation of a song being successfully downloaded.
3. Added colours to terminal output to make it look cleaner.
