from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ListElementsClass():
    def ListElementMethods(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://learn.letskodeit.com/p/practice")

        CarlistElements=driver.find_elements(By.XPATH,"//input[@type='radio' and @name='cars']")

        for x in CarlistElements:
            if not x.is_selected():
                time.sleep(3)
                x.click()


classSendKeys=ListElementsClass()
classSendKeys.ListElementMethods()