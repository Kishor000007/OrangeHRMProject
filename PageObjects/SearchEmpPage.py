from selenium import webdriver
from selenium.webdriver.common.by import By

class search_Emp:
    lnk_pim_xpath = "//span[text()='PIM']/../.."
    textbox_empname_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input"
    textbox_empid_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input"
    btn_search_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def clickpimlnk(self):
        self.driver.find_element(By.XPATH,self.lnk_pim_xpath).click()

    def EnterEmpname(self,empname):
        self.driver.find_element(By.XPATH,self.textbox_empname_xpath).send_keys(empname)

    def EnterEmpid(self,empid):
        self.driver.find_element(By.XPATH,self.textbox_empid_xpath).send_keys(empid)

    def clickSearchbtn(self):
        self.driver.find_element(By.XPATH,self.btn_search_xpath).click()
