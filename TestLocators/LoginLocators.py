#Test Locators for LoginPage

from selenium.webdriver.common.by import By

class LoginLocators:
    username_locator=(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input') #XPATH
    password_locator=(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')#XPATH
    login_button_locator=(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button') #XPATH
    dropdown_locator=(By.XPATH,'//p[@class="oxd-userdropdown-name"]')
    logout_button_locator=(By.XPATH,'//a[@class="oxd-userdropdown-link" and text()="Logout"]')


