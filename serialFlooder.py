## serialFlooder.py
## This program is intended to write as many characters as possbile to serial port
## like it's flooding it.

import os
import sys
import serial

# custom imports
import serialEnu


def loadconfig():
    if sys.argv[1] == '-c':
        # assume that on index[2] of argv there will be the settings.py file
        try:
            f=sys.argv[2]
            if f.endswith('.py'):
                import sys.argv[2]
            else:
                raise ImportError
        except ImportError:
            print('ERROR: Wrong config file!\nFile should be in python format!\n\n')
    else:
        pass

def configure():
    # this function enumerates serial devices to let the user choose the correct one
    if sys.argv[1] == '-s':
        if sys.argv[2] != '': ## argv[2] NON VIENE RICONOSCIUTO !!! ERRORE !!!!
            print('ERROR! Can\'t use -s with other parameters. -s should be called alone.\n\n')
        else:
            serialEnu.SerialMyEnumerator()
    else:
        return
    com = input('\nNow, please, insert che correct device name for the serial port to use: ')
    print('\nSerial speed:\n1) 9600\n2) 14400\n3) 19200\n4) 28800\n5) 38400\n6) 57600\n7) 115200')
    vel = input('\nSelect a speed (1,2,3,4,5,6 or 7): ')
    databit = input('\nEnter data bits (5, 6, 7 or 8): ')
    parit = input('\nEnter parity (E)ven, (O)dd, (N)one, (M)ark, (S)pace: ')
    stopb = input('\nStopbits\n1) 1 stopbit\n2) 1,5 stopbits\n3) 2 stopbits\n Enter how many stopbits you want: ')
    flowctrl = input('Do you want software flow control Xon/Xoff (Y/N)?: ')
    flowctrl.upper()

    cf=open('settings.py','w',-1,'utf-8')
    cf.write('com = \'%s' % com + '\'\n')
    cf.write('vel = \'%s' % vel + '\'\n')
    cf.write('databit = \'%s' % databit + '\'\n')
    cf.write('parit = \'%s' % parit + '\'\n')
    cf.write('stopb = \'%s' % stopb + '\'\n')
    cf.write('flowctrl = \'%s' % flowctrl + '\'\n')

    cf.flush()
    cf.close()
    print('\n\nConfiguration file created!\nNow call program with "-c settings.py" as parameter.\n\n')

    return




# this is the main

ser = serial.Serial('/dev/serial0', 115200, serial.EIGHTBITS, serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,xonxoff=True)

while True:
    try:
        for i in range(33,126):
            ser.write(str(i))
        ser.write(b'\n')
    except KeyboardInterrupt:
        print('Pressed an interruption key (Ctrl+C)... Stoppping serial communication!')
        break
    ser.close()

    