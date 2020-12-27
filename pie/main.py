from flask import Flask
from flask import *
from flask import request
import RPi.GPIO as gpio


# set list of GPIO pin's that make up LED audiovisualizer
pinlist = [37, 15, 36, 13, 11, 22, 18, 16]
# set GPIO mode and setup pins
gpio.setmode(gpio.BOARD)
for pin in pinlist:
    gpio.setup(pin, gpio.OUT)

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
    num_leds = int(request.args.get('num_leds'))
    print(num_leds)
    # if number of led's to set is higher than possible, set to max
    if num_leds > len(pinlist):
        num_leds = len(pinlist)
    # trigger LEDs
    index = 0
    for pin in pinlist:
        if index + 1 < len(pinlist):
            gpio.ouput(int(pin), True)
        else:
            gpio.ouput(int(pin), False)
    index += 1
    return str(num_leds)

# run app
if __name__ == '__main__':
    app.run(port=80)