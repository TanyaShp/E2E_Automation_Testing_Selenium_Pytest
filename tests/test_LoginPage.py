# test_LoginPage.py
import pytest
from pages.LoginPage import LoginPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from config import INDEX_URL

class TestLogin:

    # setup for the TestLogin class
    @pytest.fixture(autouse=True)
    def object_setup(self, setup):
        # instantiate LoginPage
        self.login_page = LoginPage(setup)

    # test successful login scenario
    def test_login_success(self):
        self.login_page.go_to_login()
        self.login_page.set_username("test_user")  # valid username
        self.login_page.set_password("test")  # valid password
        self.login_page.click_login_button()

        # welcome-message is only visible after a successful login:
        WebDriverWait(self.login_page.driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "welcome-message"))
    )
        
        # assert the current URL is correct, confirming successful login
        assert self.login_page.driver.current_url == INDEX_URL, "The login was not successful"

    # test login failure scenario
    def test_login_fail(self):
        self.login_page.go_to_login()
        self.login_page.set_username("wrong_user")  # invalid username
        self.login_page.set_password("wrong_password")  # invalid password
        self.login_page.click_login_button()

        # assert the flash message is correct when login fails
        assert self.login_page.get_flash_message() == "Username does not exist.", "The flash message is incorrect"

