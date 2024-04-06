import serial,time

brainy = True

if brainy:
    baudrate = 115200
else:
    baudrate = 172100 
    
def ecrire(serial,mot) :
    for i in mot:
        serial.flushInput()
        serial.flushOutput()
        serial.write(i.encode())
        serial.flush() 
        time.sleep(0.1)


def ouvrirSerial():
    with serial.Serial("/dev/tty.usbmodem1103", baudrate, timeout=1) as ser:
        if ser.isOpen():
            return ser

def fermerSerial(serial):
    serial.close()
    
serial_port = ouvrirSerial()

commandes = ["commande1", "commande2", "commande3"]
for commande in commandes:
    ecrire(serial_port, commande)
    time.sleep(1)

fermerSerial(serial_port)


