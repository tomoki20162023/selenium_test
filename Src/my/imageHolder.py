import os
from pathlib import Path

class ImageHolder(object):

	def __init__(self, root, folders=None, filename=None, suffix=None):
		self.root = root
		self.folders = folders
		self.filename = filename
		self.suffix = suffix

	def getPath(self):
		p = self.getFolder()
		return p / (self.filename + self.suffix)

	def getFolder(self):
		p = Path(self.root)
		for f in self.folders:
			p /= f
		return p

	def exists(self):
		return self.getFolder().exists()

	def mkdir(self):
		p = Path(self.root)
		if not p.exists():
			raise FileNotFoundError("存在するルートパスが必要です。")

		for f in self.folders:
			p = p / f
			if p.exists():
				continue
			else:
				p.mkdir()

def main():
	pass

if __name__=="__main__":
	main()

