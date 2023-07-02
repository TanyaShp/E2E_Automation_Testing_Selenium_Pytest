import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import INDEX_URL

# this function is a fixture
# setup is called once per test class
@pytest.fixture(scope="class")
def setup(request):
    print("Initiating chrome driver")
    # instantiate a Chrome webdriver using the ChromeDriverManager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     # navigate to the base URL as defined in the config file
    driver.get(INDEX_URL)  
    # wait for up to 6 seconds for elements to be available
    driver.implicitly_wait(6)
    # attach the webdriver instance to the test class
    request.cls.driver = driver
    # yield control back to the test method
    yield driver
    # close the webdriver session
    driver.quit()
