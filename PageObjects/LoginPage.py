from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPage:
    textbox_username_xpath="//input[@placeholder='Username']"
    textbox_pwd_xpath="//input[@placeholder='Password']"
    btn_login_xpath="//button[normalize-space()='Login']"
    btn_profile_xpath="//span[@class='oxd-userdropdown-tab']/.."
    lnk_logout_xpath="//a[text()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def EnterUsername(self,username):
        self.driver.find_element(By.XPATH,self.textbox_username_xpath).send_keys(username)

    def EnterPwd(self,pwd):
        self.driver.find_element(By.XPATH,self.textbox_pwd_xpath).send_keys(pwd)

    def clickLoginbtn(self):
        self.driver.find_element(By.XPATH,self.btn_login_xpath).click()

    def clickProfile(self):
        self.driver.find_element(By.XPATH,self.btn_profile_xpath).click()

    def clickLogotbtn(self):
        self.driver.find_element(By.XPATH,self.lnk_logout_xpath).click()


