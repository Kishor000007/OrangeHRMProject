import time

import pytest
from selenium import webdriver

from PageObjects.LoginPage import LoginPage
from PageObjects.SearchEmpPage import search_Emp
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGeneration

class Test_003_searchEmp:
    url=readConfig.getUrl()
    username=readConfig.getUsername()
    pwd=readConfig.getPassword()
    firstname=readConfig.getFirstname()
    middlename=readConfig.getMiddlename()
    lastname=readConfig.getLastname()
    empid=readConfig.getEmpId()
    logger=LogGeneration.log_gen2()

    @pytest.mark.regression
    def test_search_emp(self,setup):
        self.driver=setup
        self.driver.get(self.url)
        self.lp=LoginPage(self.driver)
        self.lp.EnterUsername(self.username)
        self.lp.EnterPwd(self.pwd)
        self.lp.clickLoginbtn()
        time.sleep(5)
        self.sEmp=search_Emp(self.driver)
        self.sEmp.clickpimlnk()
        self.sEmp.EnterEmpname(self.firstname)
        self.sEmp.EnterEmpid(self.empid)
        self.sEmp.clickSearchbtn()
        time.sleep(5)
