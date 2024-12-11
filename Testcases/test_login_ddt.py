import time
import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities import excelUtils
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGeneration


class Test_002_DDT_login:  # Data-driven testing using Excel
    baseUrl = readConfig.getUrl()
    path = "TestData/LoginData.xlsx"
    logger = LogGeneration.log_gen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******************** Test_002_DDT_login ***************************")
        self.logger.info("******************** Verifying Login Test *************************")
        self.driver = setup
        self.driver.get(self.baseUrl)
        self.lp = LoginPage(self.driver)

        # Get the number of rows in Excel
        self.rows = excelUtils.getRowCount(self.path, "Sheet1")
        self.logger.info(f"Number of rows in Excel: {self.rows}")

        list_status = []

        for r in range(2, self.rows + 1):
            self.username = excelUtils.readData(self.path, "Sheet1", r, 1)
            self.password = excelUtils.readData(self.path, "Sheet1", r, 2)
            self.exp = excelUtils.readData(self.path, "Sheet1", r, 3)

            self.logger.info(f"Testing with Username: {self.username}, Password: {self.password}, Expected: {self.exp}")

            # Perform login steps
            self.lp.EnterUsername(self.username)
            self.lp.EnterPwd(self.password)
            self.lp.clickLoginbtn()
            time.sleep(5)  # Wait for navigation

            # Validate current URL
            act_url = self.driver.current_url
            exp_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

            if act_url == exp_url:
                if self.exp == "Pass":
                    self.logger.info("****** Test Passed ******")
                    list_status.append("Pass")
                else:
                    self.logger.info("****** Test Failed (Unexpected Pass) ******")
                    list_status.append("Fail")
                self.lp.clickProfile()
                self.lp.clickLogotbtn()
            else:
                if self.exp == "Pass":
                    self.logger.info("****** Test Failed (Unexpected Fail) ******")
                    list_status.append("Fail")
                else:
                    self.logger.info("****** Test Passed ******")
                    list_status.append("Pass")

        # Final assertion
        if "Fail" not in list_status:
            self.logger.info("*********** Login DDT Test Passed ****************")
            assert True
        else:
            self.logger.info("*********** Login DDT Test Failed ****************")
            assert False

        self.driver.close()
        self.logger.info("************** End of Login Test *********************")
