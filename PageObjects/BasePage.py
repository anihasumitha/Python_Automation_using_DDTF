#Creating a basepage containing driver initialization and other basic functions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    #Method to enter text
    def enter_text(self,locator,text):
        self.wait.until(EC.presence_of_element_located(locator)).send_keys(text)

    #Method to click elements
    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()





