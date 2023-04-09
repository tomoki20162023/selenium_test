import unittest as ut

gLogger = None

class Test001(ut.TestCase):
	logger = None
	dependent = dict()

	@classmethod
	def setUpClass(cls):
		global gLogger
		cls.logger = gLogger
		print("")
		logger.debug("class test001 setup")

	@classmethod
	def tearDownClass(cls):
		print("")
		logger.debug("class test001 teardown")

	def setUp(self):
		# logger.debug("Test001 setup.")
		pass

	def tearDown(self):
		# logger.debug("Test001 teardown.")
		pass

	def test_test001_1(self):
		# logger.debug("Test001 case 1.")
		self.assertTrue(True)

	def test_sample_2(self):
		# logger.debug("Test001 case 2.")
		self.assertTrue(True)

	def test_append_3(self):
		# logger.debug("Test001 case 3.")
		self.assertTrue(True)
		self.dependent['append_3'] = True

	def test_sample_4(self):
		# logger.debug("Test001 case 4.")
		self.assertTrue(True)

	def test_append_5(self):
		# logger.debug("Test001 case 5.")
		if not self.dependent['append_3']:
			uc.skipTest('Dependent test is not passed: append_3')

		self.assertTrue(True)

def init(_logger):
	global logger
	_logger.debug("test001 init, setup logger.")
	logger = _logger

def getSuite():
	suite = ut.TestSuite()
	for testcase in dir(Test001):
		if testcase.startswith("test_"):
			suite.addTest(Test001(testcase))
	return suite

def main():
	pass

if __name__=="__main__":
	main()

