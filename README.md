# LED Audiovisualizer
## Summary:
![GIF demonstrating audiovisualizer](https://drive.google.com/uc?export=view&id=1jVq34Tla5I_UKwAHjr2YCN34t--xtW5Z)  

This LED Audiovisualizer uses a RPi 2B to sync LED's to music! You can upload your music/audio to a basic website, click submit, and watch it go!
## Explanation:
This LED Audiovisalizer works by running an API on a Raspberry Pi to trigger LED's via the GPIO pins. This API is then called by the webserver/API (ran on a separate server/device) when a file is uploaded & submitted. Upon submission, the audio file will be processed and played through the speakers of the webserver device, while the LED's connected to the Raspberry Pi will be synced to the audio (based on amplitude). The audio-processing function calculates the number of LED's to light up by taking the range of amplitude throughout the audio and calculating a "step value" that plots amplitude values within a range of 1 to 17 LEDs.
## Setup / Usage:
#### Step 1: Build Circuit
First, you'll need to build a circuit like the one below. I used 17 LED's, each connected to a GPIO pin with a jumper wire, one 330 ohm resister per LED, and one jumper wire for grounding the circuit. If you use a different number of LED's, or connect the wires to different pins, make sure to adjust the code accordingly!  

![Circuit/LED diagram](https://raw.githubusercontent.com/ethanrasmussen/LED-Audiovisualizer/master/docs/audiovis-circuit-diagram.PNG)
#### Step 2: Install dependencies & clone code
Next, you'll need to install the dependencies listed below on the RPi & webserver host (I used my laptop, but you can use just about any computer with speakers). You'll also need to make sure you have Python 3. In addition, you'll need to clone the code to each device. For the webserver host, you can just download & unzip from Github. For the RPi, you can enter ```sudo git clone https://github.com/ethanrasmussen/LED-Audiovisualizer``` in the terminal.  
#### Step 3: Run RPi API using ngrok
Once you've cloned the code and added dependencies, you'll want to run the code on the RPi by navigating into the ```LED-Audiovisualizer\pie``` directory, and running the command ```sudo python3 main.py```  
From here, you'll want to install & setup ngrok on your RPi as shown in [this tutorial](https://www.dexterindustries.com/howto/access-your-raspberry-pi-from-outside-your-home-or-local-network/), and run the command ```./ngrok http 80```
#### Step 4: Install & authenticate with ngrok on the webserver host
Now, on the webserver host, you'll want to do essentially the same process as on the RPi. You'll need to follow the instructions on ngrok's website, install ngrok according to your OS instructions, and enter your authtoken. (Note: You may find it necessary to use a second account to run ngrok tunnels on both the webserver host & RPi)
#### Step 5: Launch webserver & upload audio files
Now, you just need to run `main.py` inside the `LED-Audiovisualizer\website` directory, and you'll have a webserver up & running (ngrok will automatically launch). You'll be prompted to enter the URL/URI for the RPi API, which should be something along the lines of `<numbers>.ngrok.io`. Now, you can go to the URL displayed in the console output, upload a file, sit back, and enjoy the audiovisual show!
## Dependencies:
Flask == 1.1.2  
flask-ngrok == 0.0.25  
gpiozero == 1.5.1  
librosa == 0.8.0  
pigpio == 1.78  
pygame == 2.0.1  
requests == 2.25.1  
Werkzeug == 1.0.1  
