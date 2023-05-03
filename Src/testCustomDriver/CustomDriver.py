from pprint import pprint

import time

import unittest as ut
from unittest.mock import call, Mock, MagicMock, patch

from customdriver.CustomDriver import CustomDriver

def setUpModule():
	pass

def tearDownModule():
	pass

class CustomDriverTest(ut.TestCase):
	customDriver = None

	@classmethod
	def setUpClass(cls):
		cls.customDriver = CustomDriver()

	@classmethod
	def tearDownClass(cls):
		cls.customDriver.tearDown()
		cls.customDriver = None

	def test_001_init(self):
		self.assertIsNone(self.customDriver.loggerSetting)
		self.assertIsNone(self.customDriver.seleniumSetting)
		self.assertIsNone(self.customDriver.logger)
		self.assertIsNone(self.customDriver.driver)

	def test_002_class_setUp(self):
		self.customDriver.setUp()
		self.assertIsNotNone(self.customDriver.loggerSetting)
		self.assertIsNotNone(self.customDriver.seleniumSetting)
		self.assertIsNotNone(self.customDriver.logger)
		self.assertIsNotNone(self.customDriver.driver)
		time.sleep(3)

	def test_003_login(self):
		self.customDriver.login("user", "****", None)

	def test_004_logout(self):
		self.customDriver.logout()


def main():
	pass

if __name__=="__main__":
	main()

