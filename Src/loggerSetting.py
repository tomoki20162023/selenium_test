import yaml

import logging
import logging.config

print("loggerSetting global scope.")

def loadLogger():
	try:
		with open('selenium_logger.yml', 'r') as f:
			dic = yaml.safe_load(f)

		logging.config.dictConfig(dic)

		loggers = dict()
		targetLoggers = ['root', 'seleniumLogger']
		for target in targetLoggers:
			logger = logging.getLogger(target)
			logger.debug("{} is initialized.".format(target))
			loggers[target] = logger

		return loggers

	except yaml.scanner.ScannerError as e:
		print(e)

	return None


def main():
	pass

if __name__=="__main__":
	main()

