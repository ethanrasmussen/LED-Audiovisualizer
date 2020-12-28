import librosa
import librosa.display
import pygame
import time
import requests


# process audio & return list of 1/10sec LED values
def process_audiofile(audiofile_path:str):
    # process spectrogram w/ librosa
    data, sample_rate = librosa.load(audiofile_path,
                                     sr=22050,
                                     mono=True,
                                     offset=0.0,
                                     duration=50,
                                     res_type='kaiser_best')
    # get amplitude every 1/7 sec (originally 1/10 sec)
    amps = []
    index = 0
    #while len(amps) <= 490:
    while len(amps) <= 343:
        amps.append(data[index])
        index += int(sample_rate / 7)
    # normalize amp data to all be positive
    amps_normalized = []
    for value in amps:
        normalized_val = value + abs(min(amps))
        amps_normalized.append(normalized_val)

    ###
    #print("AMPS:")
    #print(amps)
    #print(min(amps))
    #print(max(amps))
    #print((max(amps) - min(amps)))
    #print("NORMALIZED:")
    #print(amps_normalized)
    #print(min(amps_normalized))
    #print(max(amps_normalized))
    #print((max(amps_normalized) - min(amps_normalized)))
    ###

    # translate normalized amp values to LED values 1-17
    normalized_step = max(amps_normalized) / 17
    led_values = []
    for val in amps_normalized:
        num_leds = int(round(val / normalized_step))
        led_values.append(num_leds)
    #print("LED VALUES:")
    #print(led_values)
    return led_values


# play audio on PC/server & trigger LEDs
def play_visualizer(audiofile_path:str, led_values, rpi_ip:str):
    print(f"Playing {audiofile_path} . . . ")
    # play audio on local speaker
    pygame.mixer.init()
    pygame.mixer.music.load(audiofile_path)
    pygame.mixer.music.play()
    # send LED values to RPi API & trigger visualizer
    for val in led_values:
        r = requests.get(url=f"http://{rpi_ip}/leds?num_leds={val}")
        print(val)
        time.sleep(0.03)
    # reset LED's to 0
    r = requests.get(url=f"http://{rpi_ip}/leds?num_leds=0")
    pygame.mixer.music.stop()