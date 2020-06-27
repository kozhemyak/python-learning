
# https://docs.python.org/3/library/

# -----------------------------------------------
import sys

version = sys.version_info
print('Python version is', version.major)

# -----------------------------------------------
import os
import platform
import logging

directory = 'data'
logging_file = os.path.join(directory, 'test.log')

if not os.path.exists(directory):
    os.mkdir(directory)

print("Logging to", logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s : %(levelname)s : %(message)s',
    filename=logging_file,
    filemode='w',
)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")



