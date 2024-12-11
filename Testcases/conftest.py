from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=="chrome":
        driver=webdriver.Chrome()
        print("chrome browser is launching")
    elif browser=="edge":
        driver=webdriver.Edge()
        print("edge browser is launching")
    else:
        driver=webdriver.Firefox()
        print("firefox browser is launching")
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver

#This will get value of CLI/hooks
def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
import pytest

# Add custom metadata to the HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    if hasattr(config, '_metadata'):  # Check if _metadata exists
        config._metadata['Project Name'] = 'nop Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Kishor'

# Modify or delete unwanted metadata
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)




