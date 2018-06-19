from itertools import chain

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class findElementsDemo:

    def findELemetsMethod(self):

        chromedriverpath="D:\Shishu Raj Pandey\Software\Browser Drivers\chromedriver\chromedriver.exe"
        os.environ['webdriver.chrome.driver']=chromedriverpath
        driver=webdriver.Chrome(chromedriverpath)

        driver.get("https://learn.letskodeit.com/p/practice")
        id_elements= driver.find_elements_by_id('carselect')
        tag_elements=driver.find_elements_by_tag_name('a')
        class_elements=driver.find_elements(By.CLASS_NAME,'class1')

        print(len(id_elements))
        print(len(tag_elements))
        print(len(class_elements))


findByElements=findElementsDemo()
findByElements.findELemetsMethod()