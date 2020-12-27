import IPython.display as ipd
import librosa
import librosa.display
import matplotlib.pyplot as plt
import matplotlib
import pygame
import time


# path to audio file / .m4a
audiofile = 'BS_HoaF.wav'

# inline audio player
ipd.Audio(audiofile)

# process spectrogram
plt.figure(figsize=(15,4))
data, sample_rate = librosa.load(audiofile,
                                 sr=22050,
                                 mono=True,
                                 offset=0.0,
                                 duration=50,
                                 res_type='kaiser_best',)
librosa.display.waveplot(data,
                         sr=sample_rate,
                         max_points=50000.0,
                         x_axis='time',
                         offset=0.0,
                         max_sr=10)

# print data
print(data)
print(len(data))
print(sample_rate)

# get & print range
rang = max(data) - min(data)
print(rang)

# compute step
step = rang/8
print(step)

# show waveplot
plt.show()

# get amplitude every 1/10 sec
amps = []
index = 0
while len(amps) <= 490:
    #amps.append(data[index]+abs(min(data)))
    amps.append(data[index])
    index += int(sample_rate/10)
# normalize amp data to all be positive
amps_normalized = []
for value in amps:
    normalized_val = value + abs(min(amps))
    amps_normalized.append(normalized_val)
print("AMPS:")
print(amps)
print(min(amps))
print(max(amps))
print((max(amps)-min(amps)))
print("NORMALIZED:")
print(amps_normalized)
print(min(amps_normalized))
print(max(amps_normalized))
print((max(amps_normalized)-min(amps_normalized)))


# translate normalized amp values to LED values 1-8
normalized_step = max(amps_normalized)/8
led_values = []
for val in amps_normalized:
    num_leds = int(round(val/normalized_step))
    led_values.append(num_leds)
print("LED VALUES:")
print(led_values)

# play audio & trigger LED's
pygame.mixer.init()
pygame.mixer.music.load(audiofile)
pygame.mixer.music.play()
for val in led_values:
    print(val)
    time.sleep(0.1)