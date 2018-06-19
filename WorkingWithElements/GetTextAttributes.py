from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class GetTextAttributeClass():

    def GetAttributesMethod(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://learn.letskodeit.com/p/practice")
        getText=driver.find_element(By.XPATH,'//*[@id="product"]/tbody/tr[2]/td[2]').text
        print(getText)

        getAttribute=driver.find_element(By.XPATH,"//*[@id='product']").get_attribute('name')
        print("Get Atribute text is " + getAttribute)

book=GetTextAttributeClass()
book.GetAttributesMethod()