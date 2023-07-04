#Program to demonstrate the logging functionality.

import logging

#This program is to demonstrate root log

logging.basicConfig(filename="2.logging_basic.log",format= '%(asctime)s :: %(levelname)s :: %(message)s',filemode='w',
                    level=logging.DEBUG)

logging.info("This is info log")
logging.debug("This is debug log")
logging.warning("This is warning log")
logging.error("This is error log")
logging.critical("This is critical log")