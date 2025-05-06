#LoginPage contains all the login functions of OrangeHRM website

#BasePage and Login Locators are imported
from PageObjects.BasePage import BasePage
from TestLocators.LoginLocators import LoginLocators
from TestData.LoginData import LoginData

# LoginPage class inherits from BasePage and handles login/logout actions
class LoginPage(BasePage):

    # Constructor to initialize the driver using the parent class
    def __init__(self,driver):
        super().__init__(driver)

        # Method to perform login using provided username and password
    def login_to_homepage(self,username,password):
        self.enter_text(LoginLocators.username_locator,username)
        self.enter_text(LoginLocators.password_locator,password)
        self.click_element(LoginLocators.login_button_locator)
        print("Current webpage:", self.driver.current_url)

        # Method to perform logout from the homepage
    def logout_of_homepage(self):
        self.click_element(LoginLocators.dropdown_locator)
        self.click_element(LoginLocators.logout_button_locator)
        print("Logged out of login page")
