import unittest
import os

from my.imageHolder import ImageHolder

class ImageHolderTest(unittest.TestCase):

	def setUp(self):
		self.dummyHolder = ImageHolder("dummy/img/test", ["path", "to"], "image", ".png")
		self.validHolder = ImageHolder(".", ["tests"], "image", ".png")

	def tearDown(self):
		self.dummyHolder = None

	def test_000_valid_path(self):
		h = self.dummyHolder
		hp = h.getPath().parts
		p = h.root.split("/")
		p.extend(h.folders)
		p.append(h.filename + h.suffix)
		for a, b in zip(hp, p):
			self.assertEqual(a, b)

	def test_000_valid_folder(self):
		h = self.dummyHolder
		hp = h.getFolder().parts
		p = h.root.split("/")
		p.extend(h.folders)
		for a, b in zip(hp, p):
			self.assertEqual(a, b)

	def test_001_not_exists(self):
		h = self.dummyHolder
		self.assertFalse(h.exists())

	def test_002_exists(self):
		h = self.validHolder
		self.assertTrue(h.exists())

	def test_003_parent_exists(self):
		h = self.validHolder
		p = h.getPath().parent
		self.assertTrue(p.exists())

def main():
	pass

if __name__=="__main__":
	main()

