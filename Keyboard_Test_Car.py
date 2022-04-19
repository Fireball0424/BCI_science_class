import keyboard
import serial
import time


#### port"COM5"  must be change to suitable port
ser = serial.Serial("COM15", 9600, timeout = 1)

while(True):
    if keyboard.is_pressed('w'):
        print("forward")
        ser.write(b'1')
        time.sleep(0.1)
    elif keyboard.is_pressed('s'):
        print("backward")
        ser.write(b'2')
        time.sleep(0.1)
    elif keyboard.is_pressed('a'):
        print("left")
        ser.write(b'3')
        time.sleep(0.1)
    elif keyboard.is_pressed('d'):
        print("right")
        ser.write(b'4')
        time.sleep(0.1)
    else:
        ser.write(b'0')
        time.sleep(0.1)

