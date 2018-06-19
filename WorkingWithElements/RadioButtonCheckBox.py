from selenium import webdriver
from selenium.webdriver.common.by import By

'''
Use of is_enabled()
Use of is_displayed()
Use of is_selected()
'''

class RadioButtonCheckBoxClass():
    def rd_check(self):
        driver=webdriver.Firefox()
        driver.get("https://learn.letskodeit.com/p/practice")
        driver.implicitly_wait(10)
        bmw_radio=driver.find_element(By.ID,'bmwradio')
        benz_radio=driver.find_element(By.ID,'benzradio')
        bmw_check=driver.find_element(By.ID,'bmwcheck')
        benz_check=driver.find_element(By.ID,'benzcheck')

        print(bmw_radio.is_displayed())
        print(benz_radio.is_displayed())
        print(bmw_radio.click())
        print(benz_radio.click())
        print(bmw_radio.is_selected())
        print(benz_radio.is_selected())
        print(bmw_check.is_displayed())
        print(benz_check.is_displayed())
        print(bmw_check.is_selected())
        print(benz_check.is_enabled())


class1=RadioButtonCheckBoxClass()
class1.rd_check()