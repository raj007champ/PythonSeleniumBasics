import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class ExpediaCalendar():
    def expediaCalendar(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(5)
        driver.get("https://www.expedia.com/")
        driver.find_element(By.ID,'tab-flight-tab-hp').click()
      # driver.find_element(By.ID,'flight-origin-hp-flight').send_keys("")
        driver.find_element(By.ID,'flight-departing-hp-flight').click()
        driver.find_element(By.XPATH,"//td[@class='datepicker-day-number notranslate'][1]//button[text()='24']").click()
        time.sleep(3)
        driver.find_element(By.ID,'flight-returning-hp-flight').click()
        driver.find_element(By.XPATH,"//td[@class='datepicker-day-number notranslate']//button[@data-month='5' and @data-day='30']").click()

cal=ExpediaCalendar()
cal.expediaCalendar()