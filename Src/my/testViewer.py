class TestViewer:
	def __init__(self, _driver):
		self.driver = _driver

	def showAllSiteInfo(self):
		self.show_site_info()

		ws = self.driver.get_window_size()
		self.show_window_size(ws)

		wp = self.driver.get_window_position()
		self.show_window_position(wp)

	def show_site_info(self):
		print("\n# site info")
		print("  - current URL = " + self.driver.current_url)
		print("  - title = " + self.driver.title)
		print("  - window handle = " + self.driver.current_window_handle)

	def show_element(self, _element):
		print("\n# id Element")
		print("  - id = {0}".format(_element.id))
		print("  - tag = {0}".format(_element.tag_name))
		print("  - text = {0}".format(_element.text))

	def show_window_size(self, _ws):
		print("\n# window size")
		print("  - width = {0}".format(_ws.get('width')))
		print("  - height = {0}".format(_ws.get('height')))

	def show_window_position(self, _wp):
		print("\n# window position")
		print("  - x = ", _wp.get('x'))
		print("  - y = ", _wp.get('y'))


