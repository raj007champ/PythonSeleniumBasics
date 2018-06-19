from selenium import webdriver
import os

class findingElementsbyCssXpath():

    def findElementsbyCssxpaths(self):
        driverLocation = 'D:\Shishu Raj Pandey\Software\Browser Drivers\chromedriver\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver=webdriver.Chrome(driverLocation)
        driver.get('https://learn.letskodeit.com/p/practice')

        driver.find_element_by_xpath("//button[@id='openwindow']").click()
        driver.find_element_by_css_selector("a[id='opentab']").click()

fe=findingElementsbyCssXpath()
fe.findElementsbyCssxpaths()
