# pages/SignupPage.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from config import SIGNUP_URL

class SignupPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = SIGNUP_URL
        self.username_input = (By.ID, "name")
        self.password_input = (By.ID, "password")
        self.signup_button = (By.XPATH, '//input[@type="submit"]')
        self.flash_message = (By.CLASS_NAME, "flash")  # Replace with the actual class name

    def go_to_signup(self):
        self.driver.get(self.url)

    def set_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_signup_button(self):
        self.driver.find_element(*self.signup_button).click()

    def get_flash_message(self):
        try:
            flash_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
            return flash_message.text
        except NoSuchElementException:
            return None
