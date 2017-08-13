import serial.tools.list_ports
pa = list(serial.tools.list_ports.comports())
for port in pa:
    print('0: ', port[0])
    print('1: ', port[1])
    print('2: ', port[2])

