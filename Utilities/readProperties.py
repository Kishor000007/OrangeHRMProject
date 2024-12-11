import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class readConfig():
    @staticmethod
    def getUrl():
        url=config.get("Common info","baseurl")
        return url

    @staticmethod
    def getUsername():
        username=config.get("Common info","username")
        return username

    @staticmethod
    def getPassword():
        password=config.get("Common info","password")
        return password

    @staticmethod
    def getFirstname():
        firstname=config.get("AddEmp info","firstname")
        return firstname

    @staticmethod
    def getMiddlename():
        middlename=config.get("AddEmp info","middlename")
        return middlename

    @staticmethod
    def getLastname():
        lastname = config.get("AddEmp info", "lastname")
        return lastname

    @staticmethod
    def getEmpId():
        EmpId = config.get("AddEmp info", "empId")
        return EmpId