import serial,time

baudrate = 115200

def ecrire(serial,mot) :
    for i in mot:
        serial.flushInput()
        serial.flushOutput()
        serial.write(i.encode())
        serial.flush() 
        time.sleep(0.1)

with serial.Serial("/dev/tty.usbmodem1103", baudrate, timeout=1) as ser:
    time.sleep(0.1) #wait for serial to open
    if ser.isOpen():
        ecrire(ser,"brainy\n")
        ecrire(ser,"\n")
        ecrire(ser,"login C14UD1U5C0rN3DUrU5\n")
        ecrire(ser,"1_H473_01YMP1C5\n")
        ser.close()