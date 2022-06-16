import serial
import subprocess
import random
import time

# opening serial port
ser = serial.Serial('/dev/cu.usbmodem143101', 9600)

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
