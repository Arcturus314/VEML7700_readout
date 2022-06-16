import serial
import subprocess
import random
import time
import os

# finding Arduino-like serial port
arduino_port = ""
devs = os.listdir("/dev")
for d in devs:
    if "usbmodem" in d: arduino_port = "/dev/"+d

print("Guessing Arduino is on port:",arduino_port)


# opening serial port
ser = serial.Serial(arduino_port, 9600)

# creating / erasing file
f = open("loggedlux.txt","w")
f.close()

launched = False

starttime = time.time()

while True:
    f = open("loggedlux.txt", "a")
    f.write(str(time.time() - starttime) + "," + ser.readline().decode('utf-8'))
    f.close()
    if not launched:
        print("launching plotter")
        # starting plotter
        subprocess.Popen(['python3', 'pythonplotter.py'])
        launched = True

    time.sleep(0.1)
