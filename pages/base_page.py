class BasePage():
	url = "http://selenium1py.pythonanywhere.com/"
	def __init__(self, browser, url):
    self.browser = browser
    self.url = url

    def open(self):
    self.browser.get(self.url)