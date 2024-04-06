import serial,time

notShark = True
baudrate = 172100

mdp = ["s", "h", "a", "r", "k", "\n"]


while(notShark):
    with serial.Serial("/dev/tty.usbmodem1103", baudrate, timeout=1) as ser:
        time.sleep(0.1) #wait for serial to open
        if ser.isOpen():
            print("{} connected at baudrate {}!".format(ser.port, baudrate))
        

            for i in mdp:
                    
                ser.write(b's')  # Envoyer "s"
                time.sleep(0.1)  # Attendre un peu pour la réponse
                ser.write(b'h')  # Envoyer "s"
                time.sleep(0.1)  # Attendre un peu pour la réponse
                ser.write(b'a')  # Envoyer "s"
                time.sleep(0.1)  # Attendre un peu pour la réponse
                ser.write(b'r')  # Envoyer "s"
                time.sleep(0.1)  # Attendre un peu pour la réponse
                ser.write(b'k')  # Envoyer "s"
                time.sleep(0.1)  # Attendre un peu pour la réponse
                ser.write(b'\n')  # Envoyer "s"
                time.sleep(0.1)  # Attendre un peu pour la réponse
                # Read data from serial
                line = ser.read(1024).decode().strip()
                print(line)
                if line.isascii():
                    print("Found correct baudrate: ", baudrate)
                    notShark = False
                    break  # Sortir de la boucle while
                baudrate+=100
