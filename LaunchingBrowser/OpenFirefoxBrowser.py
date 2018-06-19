from selenium import webdriver

class openBrowser:

    def openFirefox(self):
        driver=webdriver.Firefox()
        driver.get("https://www.facebook.com")

ff=openBrowser()
ff.openFirefox()