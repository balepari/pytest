## SerialEnu - Serial Enumerator for OS wide compatibility
## returns: nothing

import serial.tools.list_ports

def SerialMyEnumerator():
    print('\n\nLooking for serial ports on your system...\n\n')

    pa = list(serial.tools.list_ports.comports())

    if len(pa) != 0:
        print('Found %d elements\n' % len(pa))

    for port in pa:
        print('\n========================================')
        print('Name: ', port.name)
        print('Desc.: ', port.description)
        print('Device: ', port.device)
        print('HwId: ', port.hwid)
        print('Interface: ', port.interface)
        print('Location: ', port.location)
        print('Manufacturer: ', port.manufacturer)
        print('PID: ', port.pid)
        print('Product: ', port.product)
        print('SerialNumber: ', port.serial_number)
        print('Vid: ', port.vid)
        print('========================================\n')

    return
