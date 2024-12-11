from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class adding_Employee:
    lnk_pim_xpath = "//span[text()='PIM']/../.."
    lnk_addEmployee_xpath="//a[text()='Add Employee']"
    textbox_firstname_name="firstName"
    textbox_middlename_name="middleName"
    textbox_lastname_name = "lastName"
    textbox_emoployeeid_xpath="//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    btn_save_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def click_Pim_lnk(self):
        self.driver.find_element(By.XPATH,self.lnk_pim_xpath).click()

    def click_AddEmp_lnk(self):
        self.driver.find_element(By.XPATH,self.lnk_addEmployee_xpath).click()

    def set_First_name(self,firstname):
        self.driver.find_element(By.NAME,self.textbox_firstname_name).send_keys(firstname)

    def set_Middle_name(self,middlename):
        self.driver.find_element(By.NAME,self.textbox_middlename_name).send_keys(middlename)

    def set_Last_name(self,lastname):
        self.driver.find_element(By.NAME,self.textbox_lastname_name).send_keys(lastname)

    def set_Emp_Id(self,empid):
        self.driver.find_element(By.XPATH,self.textbox_emoployeeid_xpath).clear()
        self.driver.find_element(By.XPATH,self.textbox_emoployeeid_xpath).send_keys(empid)

    def click_save_btn(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()



