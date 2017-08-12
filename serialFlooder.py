## serialFlooder.py
## This program is intended to write as many characters as possbile to serial port
## like it's flooding it.

import serial

ser = serial.Serial('/dev/serial0', 115200, serial.EIGHTBITS, serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,xonxoff=True)

while True:
    for i in range(33,126):

        ser.write(ascii(i).encode('ascii'))
