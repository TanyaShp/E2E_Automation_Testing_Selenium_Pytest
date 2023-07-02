# tests/test_SignupPage.py
import pytest
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.SignupPage import SignupPage
from config import INDEX_URL, DEL_USR_URL


@pytest.mark.usefixtures("setup")
class TestSignup:

    @pytest.fixture(autouse=True)
    def object_setup(self, setup):
        self.signup_page = SignupPage(setup)
        self.new_user_created = False
        yield  
        if self.new_user_created:
            delete_user_url = DEL_USR_URL + self.new_user_username
            requests.delete(delete_user_url)

    def test_signup_success(self):
        username = "new_user"
        password = "new_password"
        self.signup_page.go_to_signup()
        self.signup_page.set_username(username)  # replace with a unique username
        self.signup_page.set_password(password)  # replace with a secure password
        self.signup_page.click_signup_button()
        # Add your assertions here to verify successful signup

        # Wait for an element that is only visible after a successful login:
        WebDriverWait(self.signup_page.driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "welcome-message"))
    )
                
        self.new_user_created = True
        self.new_user_username = username
        # Here you should add assertions to verify successful login
        # This could be checking the URL of the page after login
        assert self.signup_page.driver.current_url == INDEX_URL, "The signup was not successful"

    def test_signup_existing_username(self):
        self.signup_page.go_to_signup()
        self.signup_page.set_username("test_user")  # replace with an existing username
        self.signup_page.set_password("test")  # replace with any password
        self.signup_page.click_signup_button()
        assert self.signup_page.get_flash_message() == "A user already exists with that username.", "The flash message is incorrect"

    # TestSignup class
    def teardown_method(self, method):
        if self.new_user_created:
            delete_user_url = DEL_USR_URL + self.new_user_username
            requests.delete(delete_user_url)



