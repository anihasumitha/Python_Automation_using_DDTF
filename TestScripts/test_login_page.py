from PageObjects.LoginPage import LoginPage
from TestData.LoginData import LoginData
from Utilities.excel_functions import ExcelFunctions

class TestLoginPage:
    def test_login(self,setup):
        driver=setup


        excel=ExcelFunctions(LoginData.excel_file,LoginData.sheet_number)


        #reading data from Excel sheet
        for row in range(2,excel.row_count()+1):
            username=excel.read_data(row,5)
            password=excel.read_data(row,6)

        #pass this data to login script
            driver.get(LoginData.login_url)
            login = LoginPage(driver)
            login.login_to_homepage(username,password)

        #Write test results in Excel file

            if "dashboard" in driver.current_url:
                print("Test Case:Passed")
                excel.write_data(row,7,"Test Passed")
                login.logout_of_homepage()
                driver.get(LoginData.login_url)

            else:
                print("Test Case:Failed")
                excel.write_data(row,7,"Test Failed")
                driver.get(LoginData.login_url)

    #
    # def test_is_logged_in(self):
    #     assert LoginPage.is_logged_in() is True
    #     print("Successfully Logged in")
    #     print("Test Case: Passed")