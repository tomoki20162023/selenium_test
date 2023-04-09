import json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


PLATFORM_UBUNTU = 0
PLATFORM_WINDOWS = 1
BROWSER_CHROME = 0
BROWSER_EDGE = 1

env = dict()

def loadSeleniumSetting():
	if 'seleniumSetting' in env:
		if env.seleniumSetting is not None:
			return env.seleniumSetting

	env['seleniumSetting'] = None
	# load selenium setting
	setting_path = "selenium.settings.json"
	try:
		with open(setting_path, 'r') as f:
			env['seleniumSetting'] = json.load(f)
	except JSONDecodeError as e:
		print(e)
		return None

	return env['seleniumSetting']

def getDriver(_target):
	driver = None
	platforms = ["ubuntu", "windows"]
	browsers = ["chrome", "edge"]

	# デフォルトをchromeとする
	if _target is None:
		_target = BROWSER_CHROME

	platformid = PLATFORM_WINDOWS
	platform = platforms[platformid]
	browser = browsers[_target]
	pathWebDriver = env['seleniumSetting'][browser]["driverpath"]

	# プラットフォームがウィンドウズ以外
	if not platformid == PLATFORM_WINDOWS:
		ppath = pathlib.PureWindowsPath(pathWebDriver)
		pathWebDriver = ppath.as_posix().replace("C:", "/mnt/c")
		# print("path = {}".format(pathWebDriver))

	# ターゲットのブラウザドライバー取得
	if _target == BROWSER_CHROME:
		options = webdriver.ChromeOptions()
		options.add_experimental_option("excludeSwitches", [
			"enable-automation",
			"enable-logging",
		])
		options.add_experimental_option("useAutomationExtension", False)
		service = ChromeService(executable_path=pathWebDriver)
		driver = webdriver.Chrome(service=service, options=options)

	elif _target == BROWSER_EDGE:
		driver = webdriver.Edge(pathWebDriver)
	else:
		print("Error: not implement the taget browser {0}".format(_target))

	return driver

