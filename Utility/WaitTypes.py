from selenium import webdriver
from selenium.common import exceptions
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import NoSuchElementException


class waitClass():
    def waitDemoMethod():


        driver=webdriver.Firefox()
        driver.maximize_window();
        driver.implicitly_wait(10)
        driver.get("Any Url")
        #wait=WebDriverWait(driver, 10, poll_frequency=1,ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
       # wait.until(expected_conditions.element_to_be_clickable(By.ID,"Any-ID"))

        wait=WebDriverWait(driver, 10, poll_frequency=10,ignored_exceptions=[NoSuchElementException, ElementNotVisibleException, Exception])
        wait.until(expected_conditions.element_to_be_clickable(By.ID,'Some Id'))