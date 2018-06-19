from selenium import webdriver
import time

from selenium.webdriver.common.by import By


class windowHandlesClass():
    def handlemethod(self):
        driver=webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.get("https://learn.letskodeit.com/p/practice")
        parent_handle=driver.current_window_handle
        print(parent_handle)
        driver.find_element(By.ID,'openwindow').click()
        handles=driver.window_handles

        for handle in handles:
            print(handle)
            if handle==parent_handle:
                pass
            else:
                driver.switch_to.window(handle)
                time.sleep(3)
                driver.find_element(By.ID,'search-courses').send_keys("Python")
                time.sleep(3)
                driver.close()
                driver.switch_to.window(parent_handle)
            print(driver.current_window_handle)

hd=windowHandlesClass()
hd.handlemethod()
