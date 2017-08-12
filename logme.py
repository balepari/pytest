## This library is for semplify logging operation in python programs
## it permits to log to console or to a file


import logging


def logme(name='main', filename='log.log', msg='This is a message'):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # create a file handler
    handler = logging.FileHandler(filename)
    handler.setLevel(logging.INFO)

    # create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)

    logger.info(msg)
    handler.close()
    