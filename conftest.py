import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from config import INDEX_URL

@pytest.fixture(scope="class")
def setup(request):
    print("Initiating chrome driver")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(INDEX_URL)  
    driver.implicitly_wait(6)
    request.cls.driver = driver
    yield driver
    driver.quit()
