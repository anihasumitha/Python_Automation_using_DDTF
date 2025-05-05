from selenium.webdriver.common.by import By

class LoginLocators:
    username_locator=(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input') #XPATH
    password_locator=(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input')#XPATH
    login_button_locator=(By.XPATH,'//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button') #XPATH

    dropdown_locator=(By.XPATH,'//p[@class="oxd-userdropdown-name"]')
    logout_button_locator=(By.XPATH,'//a[@class="oxd-userdropdown-link" and text()="Logout"]')



# from selenium.webdriver.common.by import By
#
# class LoginLocators:
#     # Use relative XPaths or CSS Selectors
#     username_locator = (By.XPATH, '//input[@type="text" and @placeholder="Username"]')  # XPath with attributes
#     password_locator = (By.XPATH, '//input[@type="password" and @placeholder="Password"]')
#     login_button_locator = (By.XPATH, '//button[text()="Login"]')  # XPath using button text
#     # Alternatively, use CSS selectors if possible
#     # username_locator = (By.CSS_SELECTOR, '#username')
#     # password_locator = (By.CSS_SELECTOR, '#password')
#     # login_button_locator = (By.CSS_SELECTOR, '#login-btn')
