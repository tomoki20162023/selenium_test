import unittest as ut
from unittest.mock import call, Mock, MagicMock, patch

gName = "test002_1"
gLogger = None


def setUpModule():
	pass

def tearDownModule():
	pass

class Test002_1(ut.TestCase):
	name = "Test002_1"
	logger = None
	dependent = dict()

	@classmethod
	def setUpClass(cls):
		global gLogger
		cls.logger = gLogger
		print("")
		cls.logger.debug("class {} setup".format(cls.name))

	@classmethod
	def tearDownClass(cls):
		print("")
		cls.logger.debug("class {} teardown".format(cls.name))
		pass

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_001(self):
		self.assertTrue(True)


	def test_002(self):
		self.assertTrue(True)

	def test_003(self):
		self.assertTrue(True)

	def test_004(self):
		self.assertTrue(True)

	def test_005(self):
		self.assertTrue(True)

def init(_logger):
	global gLogger
	_logger.debug("{} init, setup logger.".format(gName))
	gLogger = _logger

def main():
	pass

if __name__=="__main__":
	main()



