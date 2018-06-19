from selenium import webdriver
import os
class OpenIE:

    def IEopentest(self):
        driverLocation = 'D:\Shishu Raj Pandey\Software\Browser Drivers\EdgeDriver\MicrosoftWebDriver.exe'
        os.environ["webdriver.edge.driver"] = driverLocation
        driver = webdriver.Edge(driverLocation)
        driver.get("https://www.usabloggers.com")

ch=OpenIE()
ch.IEopentest();

