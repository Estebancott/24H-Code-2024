import keyboard
import serial
import time


KEY_PRESSED = 0x01
KEY_RELEASED = 0x00

KEY_UPARROW = 0xAD
KEY_LEFTARROW = 0xAC
KEY_RIGHTARROW = 0xAE
KEY_DOWNARROW = 0xAF
KEY_USE = 0xA2

ser = serial.Serial('COM6', 115200, timeout=1)

def send_command(command):
    combined = (KEY_PRESSED >> 1) | command
    print("Pressing>", bin(combined))
    ser.flushInput()
    ser.flushOutput()
    ser.write(bytes([combined])+b'\n')
    ser.flush() 
    
    combined = (KEY_RELEASED >> 1) | command
    print("Releasing>", bin(combined))
    ser.flushInput()
    ser.flushOutput()
    ser.write(bytes([combined])+b'\n')
    ser.flush() 
    
running = True
while running:
    if keyboard.is_pressed('up'):
        send_command(KEY_UPARROW)
    elif keyboard.is_pressed('left'):
        send_command(KEY_LEFTARROW)
    elif keyboard.is_pressed('right'):
        send_command(KEY_RIGHTARROW)
    elif keyboard.is_pressed('down'):
        send_command(KEY_DOWNARROW)
    elif keyboard.is_pressed('space'):
        send_command(KEY_USE)
    elif keyboard.is_pressed('esc'):
        running = False