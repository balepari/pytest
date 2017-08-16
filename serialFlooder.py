## serialFlooder.py
## This program is intended to write as many characters as possbile to serial port
## like it's flooding it.

import os
import sys
import serial
import argparse
import os.path
import json

# custom imports
import serialEnu


def CheckExt(choices):
    class Act(argparse.Action):
        def __call__(self,parser,namespace,fname,option_string=None):
            ext = os.path.splitext(fname)[1][1:]
            if ext not in choices:
                option_string = '({})'.format(option_string) if option_string else ''
                parser.error("configfile doesn't end with one of {}{}".format(choices,option_string))
            else:
                setattr(namespace,self.dest,fname)

    return Act


def loadconfig(argom):

    print('\n\n...Sono dentro a loadconfig...\n')
    cnf = getattr(argom, 'config', None)
    file = getattr(argom, 'configfile', None)

    if cnf:
        # assume that on index[2] of argv there will be the settings.py file
        #try:
        print('\n\nFile: ' + file)

        with open(file, 'r') as f:
            sett = json.load(f)

        print('\nsett is: ' + str(type(sett)))
        for elem in sett:
            print(elem)


        # f = open(file, 'r')
        # a = list(f.readlines())
        # f.close()
        # print('\na is: ' + str(type(a)))
        # for elem in a:
        #     print(elem)

        #exec("import %s" % ext)
        #except ImportError:
        #    print('ERROR: Wrong config file!\nFile should be in python format!\n\n')
    else:
        pass
    return sett

def configure(argom):
    # this function enumerates serial devices to let the user choose the correct one
    cnf = getattr(argom, 'config', None)
    file = getattr(argom, 'configfile', None)

    if args.setup:
        serialEnu.SerialMyEnumerator()
    else:
        return
    com = input('\nNow, please, insert che correct device name for the serial port to use: ')
    print('\nSerial speed:\n1) 9600\n2) 14400\n3) 19200\n4) 28800\n5) 38400\n6) 57600\n7) 115200')
    vel = input('\nSelect a speed (1,2,3,4,5,6 or 7): ')
    databit = input('\nEnter data bits (5, 6, 7 or 8): ')
    parit = input('\nEnter parity (E)ven, (O)dd, (N)one, (M)ark, (S)pace: ')
    stopb = input('\nStopbits\n1) 1 stopbit\n2) 1,5 stopbits\n3) 2 stopbits\n Enter how many stopbits you want: ')
    flowctrl = input('\nDo you want software flow control Xon/Xoff (Y/N)?: ')
    flowctrl.upper()

    sett = {'comport':com}
    sett['speed'] = vel
    sett['databit'] = databit
    sett['parity'] = parit
    sett['stopbit'] = stopb
    sett['flowctrl'] = flowctrl

    with open(file, 'w') as cj:
        json.dump(sett, cj)

    # cf = open('settings.py', 'w', -1, 'utf-8')
    # cf.write('com = \'%s' % com + '\'\n')
    # cf.write('vel = \'%s' % vel + '\'\n')
    # cf.write('databit = \'%s' % databit + '\'\n')
    # cf.write('parit = \'%s' % parit + '\'\n')
    # cf.write('stopb = \'%s' % stopb + '\'\n')
    # cf.write('flowctrl = \'%s' % flowctrl + '\'\n')
    #
    # cf.flush()
    # cf.close()

    print('\n\nConfiguration file created!\nNow call program with "-c ' + file + '" as parameter.\n\n')

    return



parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument('-c', '--config', help='Load config from <configfile>', action='store_true')
parser.add_argument('configfile', help='Configuration file', type=str, action=CheckExt({'json'}))
group.add_argument('-s', '--setup', help='Generate config file', action='store_true')

args = parser.parse_args()
print(type(args))
if args.config:
    conf = loadconfig(args)
    print (conf)
    print(str(type(conf)))
    print('################\n')
    for element in conf:
        print(element, conf[element])
        exec("%s = \'%s\'" % (element, conf[element]))
    print('!!!!!!!!!!!!!!!!!\n')



    print("comport = \'%s\'" % comport)
    print("speed = \'%s\'" % speed)
    print("databit = \'%s\'" % databit)
    print("parity = \'%s\'" % parity)
    print("stopbit = \'%s\'" % stopbit)
    print("flowctrl = \'%s\'" % flowctrl)

if args.setup:
    configure(args)
    exit(0)
"""
print('com = \'%s' % com + '\'\n')
print('vel = \'%s' % vel + '\'\n')
print('databit = \'%s' % databit + '\'\n')
print('parit = \'%s' % parit + '\'\n')
print('stopb = \'%s' % stopb + '\'\n')
print('flowctrl = \'%s' % flowctrl + '\'\n')
"""

# this is the main

ser = serial.Serial(comport, int(speed), int(databit), parity, int(stopbit), True )


"""
ser = serial.Serial('/dev/serial0', 115200, serial.EIGHTBITS, serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,xonxoff=True)
"""
while True:
    try:
        for i in range(33,126):
            ser.write(str(i).encode())
        ser.write(b'\n')
    except KeyboardInterrupt:
        print('Pressed an interruption key (Ctrl+C)... Stoppping serial communication!')
        break
    ser.close()

    