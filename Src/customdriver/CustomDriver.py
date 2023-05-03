import sys
import time
import json
import pathlib
from datetime import datetime
from pprint import pprint


import loggerSetting
from my.seleniumBaseEnv import loadSeleniumSetting, getDriver, BROWSER_CHROME

class CustomDriver:
	loggerSetting = None
	seleniumSetting = None
	logger = None
	driver = None

	@classmethod
	def setUp(cls):
		cls.loggerSetting = loggerSetting.loadLogger()
		if cls.loggerSetting is None:
			print("Error: Failed to load logger settings.")
			exit(1)

		cls.logger = cls.loggerSetting['root']
		cls.logger.info("CustomDriver.logger is initialized.")

		cls.seleniumSetting = loadSeleniumSetting()
		if cls.seleniumSetting is None:
			print("Error: Failed to load logger settings.")
			exit(2)
		else:
			cls.logger.info("CustomDriver.seleniumSetting is initialized.")

		cls.driver = getDriver(BROWSER_CHROME)

	@classmethod
	def tearDown(cls):
		cls.logger.info("CustomDriver tears down.")

	def __init__(self):
		pass

	def login(self, user, password, tag):
		self.logger.info("login : user = {}, password = {}, tag = {}".format(user, password, tag))

	def logout(self):
		self.logger.info("logout : run logout command.")

def main():
	dummy()

if __name__=="__main__":
	main()

