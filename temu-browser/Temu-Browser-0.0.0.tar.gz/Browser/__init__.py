class Browser:
    def __init__(self):
        self.url_address = input("Enter URL Address: ")
    def open_web_site(self):
        from selenium import webdriver
        driver = webdriver.Chrome()
        driver.get(self.url_address)

required_page = Browser()
required_page.open_web_site()