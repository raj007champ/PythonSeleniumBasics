import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class AutoCompleteClass():
    def autoComplete(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://www.southwest.com/")
        #driver.find_element(By.ID,'air-city-departure').click()
        driver.find_element(By.ID,'air-city-departure').send_keys('new')
        time.sleep(3)
        driver.find_element(By.XPATH,"//ul[@id='air-city-departure-menu']//li[contains(text(),'EWR')]").click()

auto=AutoCompleteClass()
auto.autoComplete()