import time

from selenium import webdriver
from selenium.webdriver.common.by import By

class ScreenShots():
    def takeScreenshot(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://www.southwest.com/")
        driver.find_element(By.ID,'air-city-departure').send_keys('new')
        time.sleep(3)
        driver.find_element(By.XPATH,"//ul[@id='air-city-departure-menu']//li[contains(text(),'EWR')]").click()

        try:
            driver.save_screenshot("C:\\Users\\msys\\Desktop\\Python Programs\\ScreenShots\\test.png")
        except :
            print('There is an error')

auto=ScreenShots()
auto.takeScreenshot()