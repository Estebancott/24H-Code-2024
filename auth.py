import serial,time

baudrate = 115200
team = "gpt\n"
acknowledge = "ack"
shark = "shark\n"

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
        ser.flushInput()
        ser.flushOutput()
        print("{} connected at baudrate {}!".format(ser.port, baudrate))
        ecrire(ser,team)
        print(ser.read(1024).decode().strip())
        ser.flush()
        
        for i in range(4):
            ecrire(ser,acknowledge)
        while ser.in_waiting:
            print(ser.read(ser.in_waiting))
        ser.flush()
        ser.close()

baudrate = 172100

with serial.Serial("/dev/tty.usbmodem1103", baudrate, timeout=1) as ser:
    time.sleep(1.5) #wait for serial to open
    if ser.isOpen():
        ser.flushInput()
        ser.flushOutput()
        print("{} connected at baudrate {}!".format(ser.port, baudrate))
        ecrire(ser,shark)
        while ser.in_waiting:
            print(ser.read(ser.in_waiting))
        ser.flush()
        ser.write(b'\n')
        ser.close()