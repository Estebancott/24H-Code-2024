import serial
import time

baudrate = 115200  

# Define key codes
KEY_RIGHTARROW = 0xAE
KEY_LEFTARROW = 0xAC
KEY_UPARROW = 0xAD
KEY_DOWNARROW = 0xAF
KEY_STRAFE_L = 0xA0
KEY_STRAFE_R = 0xA1
KEY_USE = 0xA2
KEY_FIRE = 0xa3
KEY_ENTER = 0x0A
KEY_HOME=(0x80+0x47)
KEY_PAUSE = 0xff
KEY_PGUP = (0x80+0x49)



KEY_PRESSED = 0x01
KEY_RELEASED = 0x00
# KEY_PRESSED = 1
# KEY_RELEASED = 0

sequence = [KEY_UPARROW,KEY_UPARROW,KEY_UPARROW,KEY_LEFTARROW,KEY_UPARROW,KEY_ENTER]


# Open the serial connection
with serial.Serial('COM6', baudrate, timeout=1) as ser:
    # Loop over each action in the sequence
    for action in sequence:
        # Send the "key press" command
        combined = (KEY_PRESSED >> 1) | action
        print("Pressing>", bin(combined))
        ser.flushInput()
        ser.flushOutput()
        ser.write(bytes([combined])+b'\n')
        # ser.flush() 
        time.sleep(0.5)  # Wait a bit between press and release

        # Send the "key release" command
        combined = (KEY_RELEASED >> 1) | action
        print("Releasing>", bin(combined))
        ser.flushInput()
        ser.flushOutput()
        ser.write(bytes([combined])+b'\n')
        # ser.flush() 
        time.sleep(0.5)  # Wait a bit before the next action

    # Close the serial connection
    ser.close()