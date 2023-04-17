from pprint import pprint
import json
import time
import pathlib
from datetime import datetime
import unittest as ut

import loggerSetting
from my.seleniumBaseEnv import *
from my.testViewer import *

from tests import test001
from tests import test002

gSeleniumSetting = None
gLoggers = None


def exec_script(_driver):
	_driver.execute_script("alert('test selenium inner javascript')")

def document_initialized(driver):
	result = driver.execute_script("return app_initialized")
	print("result is {}".format(result))
	return result

def main():
	try:
		result = False
		testNo = 1
		test_urls = [
			"https://www.selenium.dev/documentation/ja/webdriver/browser_manipulation/",
			"file:///E:/programs/html/bootstrap/sample/index.html",
		]
		test_url = test_urls[testNo]

		with getDriver(BROWSER_CHROME) as driver:
			if driver is None:
				raise Exception("Error: not init driver.")

			tv = TestViewer(driver)

			#print("DOMの読み込み完了待機中")
			#driver.implicitly_wait(1)
			#print("DOMの読み込み完了")

			driver.get(test_url)
			print("check text element")
			WebDriverWait(driver, timeout=10).until(document_initialized)
			el = driver.find_element(By.TAG_NAME, "p")
			tv.show_element(el)
			assert el.text == "hello from javascript."
			# print("clear assert check")
			now = datetime.today()
			capturePath = "img/test-img-{}.png".format(now.strftime("%Y%m%d-%H%M%S"))
			driver.get_screenshot_as_file(capturePath)

			tv.show_site_info()

			# css = driver.find_element(By.CSS_SELECTOR, "#tabs-1-1-tab")
			# tv.show_element(css)

			ws = driver.get_window_size()
			tv.show_window_size(ws)

			wp = driver.get_window_position()
			tv.show_window_position(wp)

			print("終了前　5秒待機")
			time.sleep(2)
			print("終了前　待機終了")

			result = True

	except Exception as e:
		pprint(e)

	finally:
		print("test finished.")

	return result


class MainTest(ut.TestCase):
	def setUp(self):
		gLoggers['root'].debug("main test setup.")

	def tearDown(self):
		gLoggers['root'].debug("main test teardown.")

	def test_main(self):
		self.assertTrue(main())

def wholeTestSuite():
	suites = []

	testmods = [
		test001,
		test002,
	]

	rootLogger = gLoggers['root']
	for mod in testmods:
		print(mod.__name__)
		mod.init(rootLogger.getChild(mod.__name__.split('.')[-1]))

	# suite = ut.TestSuite()
	# suite.addTest(MainTest('test_main'))
	# suites.append(suite)
	for mod in testmods:
		suite = ut.TestSuite()
		tests1 = ut.defaultTestLoader.loadTestsFromModule(mod)
		if not tests1 is None:
			suite.addTests(tests1)

		tests2 = mod.getSuite()
		if not tests2 is None:
			suite.addTests(tests2)

		suites.append(suite)

		# suite.addTest(mod.getSuite())

	return suites

if __name__ == "__main__":
	import doctest
	doctest.testmod()

	gLoggers = loggerSetting.loadLogger()
	if gLoggers is None:
		exit(1)

	gSeleniumSetting = loadSeleniumSetting()
	if gSeleniumSetting is None:
		exit(2)


	class CustomTestResult(ut.TextTestResult):

		def addSuccess(self, test):
			super().addSuccess(test)
			print("custom add success.")

	import sys
	result = CustomTestResult(sys.stderr, False, 2)
	runner = ut.TextTestRunner(descriptions=False, verbosity=1)
	# ut.main(verbosity=2)

	suites = wholeTestSuite()
	for suite in suites:
		# suite.run(result)
		result = runner.run(suite)
		# pprint(result)
		pprint({
			'run': result.testsRun,
			'failure': len(result.failures),
			'errors': len(result.errors)
		})

	# pprint(dir(result))

"""
	テスト
		環境設定
			ロガー
			Selenium
		テストランナー
			スイート
				テストケース

"""

