from flask import Flask
from flask import request
from flask import *
from flask_ngrok import run_with_ngrok
import os
from werkzeug.utils import secure_filename
import website.visualizer_control as vc


# init Flask app
app = Flask(__name__)
run_with_ngrok(app)

# limit file size for uploads (to 10MB) & must be .wav
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024 * 10
app.config['UPLOAD_EXTENSIONS'] = ['.wav']
app.config['UPLOAD_PATH'] = 'audiofiles'

# global vars
IS_PLAYING = False
NOW_PLAYING = ""
RPI_API = None


# index/main upload page
@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

# file upload on home page
@app.route('/', methods=['POST'])
def upload_audio():
    audiofile = request.files['file']
    filename = secure_filename(audiofile.filename)
    if audiofile.filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)
        audiofile.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        # set audio as playing
        NOW_PLAYING = filename
        IS_PLAYING = True
        # process audio & trigger LEDs
        led_values = vc.process_audiofile(f"audiofiles/{filename}")
        vc.play_visualizer(filename, led_values, RPI_API)
    return redirect(url_for('nowplaying'))

# now playing
@app.route('/nowplaying')
def nowplaying():
    if IS_PLAYING:
        return NOW_PLAYING
    else:
        return "Nothing is playing right now!"

# please wait
@app.route('/pleasewait')
def pleasewait():
    return 'Something is currently playing, please wait!'




# run & get RPi API URL/URI
if __name__ == '__main__':
    print("Please enter URL/URI for RPi API:")
    RPI_API = input()
    app.run()