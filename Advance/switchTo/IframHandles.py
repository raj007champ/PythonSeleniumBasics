from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class Iframe():
    def IframeHandles(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        #driver.find_element(By.ID,'')
        #driver.switch_to.frame("courses-iframe") #switching frame by Id
        driver.switch_to.frame("iframe-name")  #switching frame by name
        #driver.switch_to.frame('0')    #switching frame by frame number
        time.sleep(3)
        driver.find_element(By.ID,'search-courses').send_keys('Python')
        e=driver.find_element(By.XPATH,"//div[contains(text(),'Learn Python')]").text
        print(e)
        driver.switch_to.default_content()


frame=Iframe()
frame.IframeHandles()