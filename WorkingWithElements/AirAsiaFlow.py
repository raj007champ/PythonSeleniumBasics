from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class AirAsiaFlowClass():

    def BookFlight(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://www.airasia.com")
      #  // *[ @ id = "select2-cb_origins-container-inner"] / span[2]
        driver.find_element(By.XPATH,"/html/body/form/div[3]/main/div[1]/div[2]/div/div/div/div[1]/div[1]/label/span").send_keys("Pune")
       # driver.find_element(By.XPATH,"//*[contains[text(),'select2-cb_origins-container-inner']").click()

book=AirAsiaFlowClass()
book.BookFlight()