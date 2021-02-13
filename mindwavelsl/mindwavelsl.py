"""
Used to synchronize Mindwave measurments with other tools
through LabStreamingLayer. 
"""
import json
import sys
import time

from logger import *
from outlet import *

log = MindwaveLogger('mindwave-main')

def main():
	mwlsl = MindwaveLSL(
		"localhost",
		"13854",
		file_outlet_path="C:/Temp/brain.csv",
		run_lsl=True,
		mindwave_python_connect=False,
		device="",
		headset_id="",
		open_serial=True
	)

	log.info("Setting up...")
	mwlsl.setup()
	mwlsl.write('{"enableRawOutput": true, "format": "Json"}')

	log.info("Running...")
	mwlsl.run()

if __name__=="__main__":
	main()
