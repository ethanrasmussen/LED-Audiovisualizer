from flask import Flask
from flask import *
from flask import request
from pie.gpio_control import set_leds


# set list of GPIO pin's that make up LED audiovisualizer
pinlist = []

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
    # if number of led's to set is higher than possible, set to max
    if num_leds > len(pinlist):
        num_leds = len(pinlist)
    # trigger LEDs
    set_leds(num_leds, pinlist)
    return num_leds

# run app
if __name__ == '__main__':
    app.run(port=80)