import unittest as ut
from unittest.mock import call, Mock, MagicMock, patch

gLogger = None

"""
def load_tests(loader, tests, pattern):
	suite = ut.TestSuite()
	tests = loader.loadTestsFromTestCase(Test001)
	suite.addTests(tests)
	return suite

	for testcase in dir(Test001):
		if testcase.startswith("test_"):
			suite.addTest(Test001(testcase))
"""

def setUpModule():
	pass

def tearDownModule():
	pass

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
		pass

	def setUp(self):
		# logger.debug("Test001 setup.")
		pass

	def tearDown(self):
		# logger.debug("Test001 teardown.")
		pass

	def test_test001_1(self):
		# logger.debug("Test001 case 1.")
		self.assertTrue(True)
		mock = Mock()
		mock.method()
		mock.method.assert_called()
		mock.method.assert_called_once()


	def test_sample_2(self):
		# logger.debug("Test001 case 2.")
		self.assertTrue(True)
		mock = Mock()
		mock.hello('tom')
		mock.hello.assert_called_with('tom')
		mock.hello.assert_called_once_with('tom')

	def test_append_3(self):
		# logger.debug("Test001 case 3.")
		self.assertTrue(True)
		self.dependent['append_3'] = True
		mock = Mock()
		mock.hello('tom')
		mock.hello('alice')
		mock.hello('bob')
		mock.hello('dad', 'mam')
		mock.hello.assert_any_call('alice')
		mock.hello.assert_any_call('dad', 'mam')

	def test_sample_4(self):
		# logger.debug("Test001 case 4.")
		self.assertTrue(True)
		mock = Mock()
		mock.frac(1)
		mock.frac(2)
		mock.frac(3)
		mock.frac(4)
		mock.frac(5)
		mock.frac.assert_has_calls([call(3), call(4)])
		mock.frac.assert_has_calls([call(5), call(3), call(1)], True)

	def test_append_5(self):
		# logger.debug("Test001 case 5.")
		if not self.dependent['append_3']:
			uc.skipTest('Dependent test is not passed: append_3')

		self.assertTrue(True)

		mock = MagicMock(return_value = 3)
		mock.mock_add_spec(['call_dragon', 'dragon'])
		mock.call_dragon = True
		mock.dragon = MagicMock()
		mock.dragon.assert_not_called()
		mock.dragon('Appeared!')
		mock.dragon.assert_called_with('Appeared!')
		self.assertEqual(mock.dragon.call_args[0][0], 'Appeared!')
		self.assertEqual(mock(), 3)
		self.assertTrue(mock.call_dragon)

def init(_logger):
	global logger
	_logger.debug("test001 init, setup logger.")
	logger = _logger

def main():
	pass

if __name__=="__main__":
	main()

