from selenium import webdriver
import os

class findingElementsbyLinkPartiaXLink():

    def findElementsbylinks(self):
        driverLocation = 'D:\Shishu Raj Pandey\Software\Browser Drivers\chromedriver\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver=webdriver.Chrome(driverLocation)
        driver.get('https://learn.letskodeit.com/p/practice')

        loginLink=  driver.find_element_by_link_text('Login')
        practiceLink= driver.find_element_by_partial_link_text('Pract')

        if loginLink is not None:
            print('Login Link found')
        if practiceLink is not None:
            print('Practice link Found')

fe=findingElementsbyLinkPartiaXLink()
fe.findElementsbylinks()
