import serial
import time

baudrate = 115200

instructions = [
    "go South\n",
    "collect maj\n",
    "collect min\n",
    "display\n"
]

def ecrire(serial, mot):
    for i in mot:
        serial.flushInput()
        serial.flushOutput()
        serial.write(i.encode())
        serial.flush()
        time.sleep(0.1)

with serial.Serial("/dev/tty.usbmodem1103", baudrate, timeout=1) as ser:
    time.sleep(0.1)  # Attendre que la connexion série soit ouverte
    if ser.isOpen():
        for instruction in instructions:
            ecrire(ser, instruction)
            print(ser.read(1024).decode().strip())
