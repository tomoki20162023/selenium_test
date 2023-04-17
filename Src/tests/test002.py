import unittest as ut
from unittest.mock import call, Mock, MagicMock, patch

from tests.tests002 import test002_1
from my.test001 import MyLib

gName = "test002"
gLogger = None

class Test002(ut.TestCase):
	logger = None
	dependent = dict()

	@classmethod
	def setUpClass(cls):
		cls.logger = gLogger
		print("")
		cls.logger.debug("class test002 setup")

	@classmethod
	def tearDownClass(cls):
		print("")
		cls.logger.debug("class test002 teardown")

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

	@patch("my.test001.MyLib.instVal")
	@patch("my.test001.MyLib.clsVal")
	@patch("my.test001.MyLib.staVal")
	def test_004_sample_4(self, pstaVal, pclsVal, pinstVal):
		pstaVal.return_value = "dummy"
		pclsVal.return_value = 7
		pinstVal.return_value = 99

		lib = MyLib()
		self.assertEqual(MyLib.staVal(), "dummy")
		self.assertEqual(lib.clsVal(), 7)
		self.assertEqual(lib.instVal(), 99)

	def test_005_append_5(self):
		if not self.dependent['append_3']:
			uc.skipTest('Dependent test is not passed: append_3')

		self.assertTrue(True)
		self.assertFalse(False)
		self.assertFalse(False)

def getSuite():
	suites = []

	testmods = [
		test002_1,
	]

	rootLogger = gLogger
	for mod in testmods:
		print(mod.__name__)
		mod.init(rootLogger.getChild(mod.__name__.split('.')[-1]))

	for mod in testmods:
		suite = ut.TestSuite()
		tests = ut.defaultTestLoader.loadTestsFromModule(mod)
		suite.addTests(tests)
		suites.append(suite)
		# suite.addTest(mod.getSuite())
	return suites

def init(_logger):
	global gLogger
	_logger.debug("{} init, setup logger.".format(gName))
	gLogger = _logger

def main():
	pass

if __name__=="__main__":
	main()


