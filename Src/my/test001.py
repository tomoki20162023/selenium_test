print("my test 001 global scope.")

class MyLib:

	@staticmethod
	def staVal():
		return "static"

	@classmethod
	def clsVal(cls):
		return -1

	def instVal(self):
		return 7


def dummy():
	print("my test 001.dummy")

def main():
	dummy()

if __name__=="__main__":
	main()

