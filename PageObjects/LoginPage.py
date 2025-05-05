from PageObjects.BasePage import BasePage
from TestLocators.LoginLocators import LoginLocators
from TestData.LoginData import LoginData

class LoginPage(BasePage):

        def __init__(self,driver):
            super().__init__(driver)

        def login_to_homepage(self,username,password):
            self.enter_text(LoginLocators.username_locator,username)
            self.enter_text(LoginLocators.password_locator,password)
            self.click_element(LoginLocators.login_button_locator)
            print("Current webpage:", self.driver.current_url)

        def logout_of_homepage(self):
            self.click_element(LoginLocators.dropdown_locator)
            self.click_element(LoginLocators.logout_button_locator)
            print("Logged out of login page")
