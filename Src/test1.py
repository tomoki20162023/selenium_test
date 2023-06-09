from pprint import pprint

import os
import sys
import json
import time
from pathlib import Path
from datetime import datetime
import unittest as ut

import loggerSetting

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

from my.testViewer import TestViewer
from my.imageHolder import ImageHolder
from my.seleniumBaseEnv import loadSeleniumSetting, getDriver, BROWSER_CHROME

from tests import test001
from tests import test002

gLoggers = None

def exec_script(_driver):
	_driver.execute_script("alert('test selenium inner javascript')")

def document_initialized(driver):
	print("wait document initialized.")
	result = driver.execute_script("return app_initialized")
	print("result is {}".format(result))
	return result

def getNowDatetimeStr():
	return datetime.today().strftime("%Y%m%d-%H%M%S")

def sampleAction1(driver, tv):
	print("check text element")
	WebDriverWait(driver, timeout=10).until(document_initialized)
	el = driver.find_element(By.TAG_NAME, "p")
	tv.show_element(el)
	assert el.text == "hello from javascript."
	# print("clear assert check")
	# capturePath = "/mnt/p/captures/img/section/{}/"
	# driver.get_screenshot_as_file(capturePath)
	time.sleep(2)

def sampleAction2(driver):
	try:
		print("file upload action")
		ff = driver.find_element(By.ID, "formfile")
		# 実在するファイルのフルパスをフォームに送ってやると入力可能
		ff.send_keys("C:\\Windows\\write.exe")

		print(ff)
		print("find element")

			# .click(formfile)\
		#ActionChains(driver)\
		#	.send_keys("C:/Users/tom71/macros.ini")\
		#	.perform()
		print("click element and select file")

	except Exception as e:
		print("raised exception")
		print(e)

	# action = ActionChains(driver).send_keys("sample-file.txt").perform()
	time.sleep(3)

def sampleDriverTest(driver):
	tv = TestViewer(driver)

	testNo = 1
	test_urls = [
		"https://www.selenium.dev/documentation/ja/webdriver/browser_manipulation/",
		"file:///E:/programs/html/bootstrap/sample/index.html",
	]
	test_url = test_urls[testNo]

	#print("DOMの読み込み完了待機中")
	#driver.implicitly_wait(1)
	#print("DOMの読み込み完了")

	driver.get(test_url)

	sampleAction1(driver, tv)
	sampleAction2(driver)

	tv.showAllSiteInfo()

	# css = driver.find_element(By.CSS_SELECTOR, "#tabs-1-1-tab")
	# tv.show_element(css)

	print("終了前　5秒待機")
	time.sleep(2)
	print("終了前　待機終了")

	return True


def main():
	try:
		result = False
		# nowStr = getNowDatetimeStr()

		with getDriver(BROWSER_CHROME) as driver:
			if driver is None:
				raise Exception("Error: not init driver.")

			result = sampleDriverTest(driver)
			if result is None:
				result = False

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


	class CustomTestResult(ut.TextTestResult):

		def addSuccess(self, test):
			super().addSuccess(test)
			print("custom add success.")

	result = CustomTestResult(sys.stderr, False, 2)
	runner = ut.TextTestRunner(descriptions=False, verbosity=1)
	# ut.main(verbosity=2)

	main()

"""
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
"""

"""
	テスト
		環境設定
			ロガー
			Selenium
		テストランナー
			スイート
				テストケース

"""

