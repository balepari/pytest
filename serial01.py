import serial

ser = serial.Serial('/dev/serial0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, xonxoff=True)

print(ser.name)
ser.write(b'Hello World!')
ser.flush()
letto = ser.read(8)
print(letto)
ser.close()
