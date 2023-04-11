import unittest as ut
from unittest.mock import call, Mock, MagicMock, patch

gLogger = None

class Test002(ut.TestCase):
	logger = None
	dependent = dict()

	@classmethod
	def setUpClass(cls):
		global gLogger
		cls.logger = gLogger
		print("")
		logger.debug("class test002 setup")

	@classmethod
	def tearDownClass(cls):
		print("")
		logger.debug("class test002 teardown")

	def setUp(self):
		# logger.debug("Test002 setup.")
		self.driver = MagicMock()
		self.driver.add_spec('dummy')
		self.driver.dummy = True
		pass

	def tearDown(self):
		# logger.debug("Test002 teardown.")
		pass

	def test_001_test002_1(self):
		self.assertTrue(True)
		self.assertFalse(False)
		self.assertTrue(self.driver.dummy)

	def test_002_sample_2(self):
		self.assertTrue(True)
		self.assertFalse(False)

	def test_003_append_3(self):
		self.assertTrue(True)
		self.dependent['append_3'] = True

	def test_004_sample_4(self):
		self.assertTrue(True)

	def test_005_append_5(self):
		if not self.dependent['append_3']:
			uc.skipTest('Dependent test is not passed: append_3')

		self.assertTrue(True)
		self.assertFalse(False)
		self.assertFalse(False)

def init(_logger):
	global logger
	_logger.debug("test002 init, setup logger.")
	logger = _logger

def getSuite():
	suite = ut.TestSuite()
	for testcase in dir(Test002):
		if testcase.startswith("test_"):
			suite.addTest(Test002(testcase))
	return suite

def main():
	pass

if __name__=="__main__":
	main()


