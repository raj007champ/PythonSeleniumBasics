from selenium import webdriver
import os
class OpenChrome:

    def chromeopentest(self):
        driverLocation = 'D:\Shishu Raj Pandey\Software\Browser Drivers\chromedriver\chromedriver.exe'
        os.environ["webdriver.chrome.driver"] = driverLocation
        driver = webdriver.Chrome(driverLocation)
        driver.get("https://www.facebook.com")

ch=OpenChrome()
ch.chromeopentest();

