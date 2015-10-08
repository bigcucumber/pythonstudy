__author__ = 'luowen'

"this is a log demo"

import logging

"""
logging.warning("Watch out")
logging.info("this is a information")
logging.debug("this is a debug information")
logging.error("error.")
"""

logging.basicConfig(filename="logDemo.log", format="%(levelname)s: %(asctime)s : %(message)s", level=logging.DEBUG, filemode="w")

logging.info("application startt")

logging.info("application do somesting.")

logging.info("application finished")
