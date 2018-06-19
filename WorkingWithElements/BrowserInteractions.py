from selenium import webdriver

class BrowserInteractions():

    def browserInteractionMethod(self):
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get('https://learn.letskodeit.com/p/practice')
        current_url=driver.current_url
        print(current_url)
        page_source=driver.page_source
        title=driver.title

        driver.back()
        print(title)
        driver.forward()
        driver.refresh()
        driver.get(driver.current_url)
       # driver.close()
        driver.quit()

class1=BrowserInteractions()
class1.browserInteractionMethod()

