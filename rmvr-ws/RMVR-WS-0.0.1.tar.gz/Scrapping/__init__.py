class Scrapping:

    def __init__(self, url):
        self.url_address = url

    def open_web_site(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get(self.url_address)


