import time

import pytest
from PageObjects.AddingEmpPage import adding_Employee
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGeneration

class Test_002_AddEmp:
    baseurl= readConfig.getUrl()
    username=readConfig.getUsername()
    password=readConfig.getPassword()
    firstname= readConfig.getFirstname()
    middlename= readConfig.getMiddlename()
    lastname= readConfig.getLastname()
    empid= readConfig.getEmpId()

    logger=LogGeneration.log_gen2()

    @pytest.mark.sanity
    def test_addEmp(self,setup):
        self.logger.info("******************* Test_002_AddEmp **********************")
        self.logger.info("****************** test_addEmp test started *******************")
        self.driver=setup
        self.lp=LoginPage(self.driver)
        self.driver.get(self.baseurl)
        self.lp.EnterUsername(self.username)
        self.lp.EnterPwd(self.password)
        self.lp.clickLoginbtn()
        time.sleep(2)
        self.aEmp = adding_Employee(self.driver)
        self.aEmp.click_Pim_lnk()
        self.aEmp.click_AddEmp_lnk()
        self.aEmp.set_First_name(self.firstname)
        self.aEmp.set_Middle_name(self.middlename)
        self.aEmp.set_Last_name(self.lastname)
        self.aEmp.set_Emp_Id(self.empid)
        self.aEmp.click_save_btn()
        time.sleep(8)

        act_title=self.driver.title
        exp_title="OrangeHRM"

        self.logger.info("****************Verifying Title**************************")
        if act_title==exp_title:
            assert True
            self.driver.close()
            self.logger.info("**************addEmp test passed**************************")
        else:
            self.driver.save_screenshot(".\\ScreenShots\\test_addEmp.png")
            self.driver.close()
            self.logger.error("****************addEmp test failed**************************")
            assert False
        self.logger.info("******************test_addEmp test completed***************************")






