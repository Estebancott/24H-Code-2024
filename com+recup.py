import serial,time

baudrate = 172100

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
        ecrire(ser,"cat ./msg_from_st_team. sixel")
        while 1:
            print(ser.read(1024).decode().strip())