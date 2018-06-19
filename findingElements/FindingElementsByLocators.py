from selenium import webdriver
import os

class findingElements():

    def findElements(self):
        driverLocation = 'D:\Shishu Raj Pandey\Software\Browser Drivers\chromedriver\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver=webdriver.Chrome(driverLocation)
        driver.get('https://learn.letskodeit.com/p/practice')
        bmwbutton=driver.find_element_by_id("bmwradio")
        if bmwbutton is not None:
            print('BMW Found')
        driver.find_element_by_name("cars").click()

fe=findingElements()
fe.findElements()
