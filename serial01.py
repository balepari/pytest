import serial
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('trace.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

logger.info('Imposto la seriale...')
ser = serial.Serial('/dev/serial0', 115200, serial.EIGHTBITS, serial.PARITY_NONE, serial.STOPBITS_ONE, xonxoff=True)
print(ser.name)
logger.info('Scrivo sulla seriale...')
ser.write(b'Hello World!')
logger.info('Svuoto il buffer...')
ser.flush()
#letto = ser.read(8)
#print(letto)
logger.info('Chiudo la seriale...')
ser.close()
logger.info('Termino...')
