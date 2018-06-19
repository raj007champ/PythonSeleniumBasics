from selenium import webdriver
import time
from selenium.webdriver.common.by import By

from selenium.webdriver.common.alert import Alert


class AlertHand:
    def AlertHandles(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")

        driver.find_element(By.ID,'name').send_keys('Hello')
        driver.find_element(By.ID,'alertbtn').click()
        alert= driver.switch_to.alert
        time.sleep(3)
        alert.accept()
        time.sleep(3)
        driver.find_element(By.ID, 'name').send_keys('Name')
        driver.find_element(By.ID, 'confirmbtn').click()
        alert = driver.switch_to.alert
        time.sleep(3)
        alert.dismiss()
        time.sleep(3)


alert=AlertHand()
alert.AlertHandles()