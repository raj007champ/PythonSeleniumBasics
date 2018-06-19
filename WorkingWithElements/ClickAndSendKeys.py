from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():
    def ClickAAndSendActions(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.find_element(By.XPATH,'//a[@href="/sign_in"]').click()
        driver.find_element_by_id("user_email").send_keys('test')
        time.sleep(5)
        driver.find_element_by_id('user_password').send_keys('test')
        driver.find_element(By.XPATH,"//input[@value='Log In']").click()

classSendKeys=ClickAndSendKeys()
classSendKeys.ClickAAndSendActions()
