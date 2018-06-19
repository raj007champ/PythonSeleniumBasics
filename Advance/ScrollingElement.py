from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class ScrollingElement():
    def scrolling(self):
        driver=webdriver.Firefox()
        #Using javascript to open a URL
        #driver.execute_script("window.location='https://learn.letskodeit.com/p/practice'")
        driver.get('https://learn.letskodeit.com/p/practice')

        element = driver.execute_script("return document.getElementById('name');")
        element.send_keys('hey')
        driver.execute_script("window.scrollBy(0,5000);")
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,-1000);")
        element=driver.find_element(By.XPATH,"//*[@id='mousehover']")
        driver.execute_script('arguments[0].scrollIntoView(true);',element)


js=ScrollingElement()
js.scrolling()