import sys
import time
import json
import pathlib
from datetime import datetime
from pprint import pprint


import loggerSetting
from my.seleniumBaseEnv import getDriver, BROWSER_CHROME

gSeleniumSetting = None
gLoggers = None


def init():

	gLoggers = loggerSetting.loadLogger()
	if gLoggers is None:
		exit(1)

	gSeleniumSetting = loadSeleniumSetting()
	if gSeleniumSetting is None:
		exit(2)


class MyLib:

	@staticmethod
	def staVal():
		return "static"

	@classmethod
	def clsVal(cls):
		return -1

	def instVal(self):
		return 7


def main():
	dummy()

if __name__=="__main__":
	main()

