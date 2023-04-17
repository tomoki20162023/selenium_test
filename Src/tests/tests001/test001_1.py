import unittest as ut
from unittest.mock import call, Mock, MagicMock, patch

gName = "test001_1"
gLogger = None

def setUpModule():
	pass

def tearDownModule():
	pass

class Test001_1Base(ut.TestCase):
	name = "Test001_1Base"
	logger = None

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


class Test001_1(Test001_1Base):
	# name = "Test001_1"
	# logger = None
	dependent = dict()

	@classmethod
	def setUpClass(cls):
		# global gLogger
		# cls.logger = gLogger
		# print("")
		# cls.logger.debug("class {} setup".format(cls.name))
		super().setUpClass()
		pass

	@classmethod
	def tearDownClass(cls):
		# print("")
		# cls.logger.debug("class {} teardown".format(cls.name))
		super().tearDownClass()
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
		res = 99
		self.assertEqual(res, 99)

def init(_logger):
	global gLogger
	_logger.debug("{} init, setup logger.".format(gName))
	gLogger = _logger

def main():
	pass

if __name__=="__main__":
	main()


