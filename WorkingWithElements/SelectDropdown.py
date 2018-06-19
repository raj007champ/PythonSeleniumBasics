from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import time

class SelectDropdownClass():
     def selectdropdownDemo(self):
         driver=webdriver.Firefox()
         driver.get("https://learn.letskodeit.com/p/practice")
         selectDropdown=Select(driver.find_element(By.XPATH,"//select[@id='carselect']"))
         selectDropdown.select_by_index(0)
         time.sleep(3)
         selectDropdown.select_by_value('benz')
         time.sleep(3)
         selectDropdown.select_by_visible_text('Honda')

dropdown=SelectDropdownClass()
dropdown.selectdropdownDemo()