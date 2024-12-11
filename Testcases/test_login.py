import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGeneration

class Test_001_login:
    baseUrl = readConfig.getUrl()
    username = readConfig.getUsername()
    password = readConfig.getPassword()

    logger=LogGeneration.log_gen()

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info("*********************Test_001_login*********************")
        self.logger.info("*********************Verifying Home Page title***********************************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        act_title=self.driver.title
        if act_title=="OrangeHRM":
            assert True
            self.driver.close()
            self.logger.info("********************Home page title is passed***************************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\" + "test_homepagetitle.png")
            self.driver.close()
            self.logger.error("********************Home page title is failed***************************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********************Verifying Login Test***************************")
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lp=LoginPage(self.driver)
        #We have to use self keyword bcoz username,pwd,baseUrl are class variables
        self.lp.EnterUsername(self.username)
        self.lp.EnterPwd(self.password)
        self.lp.clickLoginbtn()
        time.sleep(5)
        act_url=self.driver.current_url
        exp_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
        if act_url==exp_url:
            assert True
            self.driver.close()
            self.logger.info("********************Login test is passed***************************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********************Login test is failed***************************")
            assert False







