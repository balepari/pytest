import serial
import logme

logme.logme(name='serial', filename='trace.log', msg='Imposto la seriale...')
ser = serial.Serial('/dev/serial0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, xonxoff=True)

print(ser.name)

logme.logme(name='serial', filename='trace.log', msg='Scrivo sulla seriale...')
ser.write(b'Hello World!')
logme.logme(name='serial', filename='trace.log', msg='Svuoto il buffer...')
ser.flush()
#letto = ser.read(8)
#print(letto)
logme.logme(name='serial', filename='trace.log', msg='Chiudo la seriale...')
ser.close()
logme.logme(name='serial', filename='trace.log', msg='Termino...')
