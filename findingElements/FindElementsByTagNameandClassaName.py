from selenium import webdriver
import os

class findingElementsbyClassNameTagName():

    def findElementsbytagandclass(self):
        driverLocation = 'D:\Shishu Raj Pandey\Software\Browser Drivers\chromedriver\chromedriver.exe'
        os.environ['webdriver.chrome.driver'] = driverLocation
        driver=webdriver.Chrome(driverLocation)
        driver.get('https://learn.letskodeit.com/p/practice')

        classNameElement=  driver.find_element_by_class_name("class1")
        tagNameElement= driver.find_element_by_tag_name('h1')

        if classNameElement is not None:
            print('Class Element found')
        if tagNameElement is not None:
            print('tagName element Found')

fe=findingElementsbyClassNameTagName()
fe.findElementsbytagandclass()
