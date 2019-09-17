import os
import time
import logging

def initialize_logger():
	if not os.path.exists('logs/'): os.mkdir('logs/')
	logname = time.strftime('logs/%Y:%m:%d-%H:%M:%S.log')
	logging.basicConfig(filename=logname, level=logging.DEBUG)