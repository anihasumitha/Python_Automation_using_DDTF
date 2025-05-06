#TestScript for LoginPage

# Import necessary classes from project modules
from PageObjects.LoginPage import LoginPage
from TestData.LoginData import LoginData
from Utilities.excel_functions import ExcelFunctions

class TestLoginPage:
    def test_login(self,setup):
        driver=setup

        # Initialize ExcelFunctions with the test data file and sheet index
        excel=ExcelFunctions(LoginData.excel_file,LoginData.sheet_number)

        #Reading data from Excel sheet
        for row in range(2,excel.row_count()+1):
            username=excel.read_data(row,5)
            password=excel.read_data(row,6)

        #Pass this data to login script
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
