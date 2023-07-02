# tests/test_SignupPage.py
import pytest
import requests
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from pages.SignupPage import SignupPage
from config import INDEX_URL, DEL_USR_URL

# use the setup fixture for these test cases
@pytest.mark.usefixtures("setup")
class TestSignup:

    # setup for the TestSignup class
    @pytest.fixture(autouse=True)
    def object_setup(self, setup):
        # instantiate SignupPage
        self.signup_page = SignupPage(setup)
        # track if a new user was created
        self.new_user_created = False

        # tear down after tests run
        yield  
        if self.new_user_created:
            delete_user_url = DEL_USR_URL + self.new_user_username
            requests.delete(delete_user_url)

    # test successful signup scenario
    def test_signup_success(self):
        username = "new_user"
        password = "new_password"
        self.signup_page.go_to_signup()
        self.signup_page.set_username(username)  # unique username
        self.signup_page.set_password(password)  # password
        self.signup_page.click_signup_button()

        # wait for an element that is only visible after a successful login:
        WebDriverWait(self.signup_page.driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "welcome-message"))
    )
        # flag new user creation and store username        
        self.new_user_created = True
        self.new_user_username = username
        
        # assert URL is correct to confirm successful signup
        assert self.signup_page.driver.current_url == INDEX_URL, "The signup was not successful"

    # test signup scenario with an existing username
    def test_signup_existing_username(self):
        self.signup_page.go_to_signup()
        self.signup_page.set_username("test_user")  # existing username
        self.signup_page.set_password("test")  # any password
        self.signup_page.click_signup_button()

        # assert flash message is correct when user already exists
        assert self.signup_page.get_flash_message() == "A user already exists with that username.", "The flash message is incorrect"


