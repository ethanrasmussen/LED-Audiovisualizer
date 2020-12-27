from flask import Flask
from flask import *
from flask import request


# init Flask app
app = Flask(__name__)

# index route
@app.route('/')
def index():
    return render_template('index.html')

# led trigger route
@app.route('/leds', methods=['GET'])
def leds():
    # process arg to get num led's to enable
    num_leds = request.args.get('num_leds')
    print(num_leds)
    # trigger LEDs
    return num_leds

# run app
if __name__ == '__main__':
    app.run(port=80)