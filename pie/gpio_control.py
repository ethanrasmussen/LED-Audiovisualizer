import RPi.GPIO as gpio

def set_leds(num_leds:int, pinout_list):
    index = 0
    for pin in pinout_list:
        if index+1 < len(pinout_list):
            gpio.ouput(int(pin), True)
        else:
            gpio.ouput(int(pin), False)
    index += 1