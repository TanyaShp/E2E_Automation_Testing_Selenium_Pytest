from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from config import LOGIN_URL

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_login(self):
        self.driver.get(LOGIN_URL) 

    def set_username(self, username):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "name"))).send_keys(username)

    def set_password(self, password):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "password"))).send_keys(password)

    def click_login_button(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn"))).click()

    def get_flash_message(self):
        try:
            flash_message = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "alert")))
            return flash_message.text
        except NoSuchElementException:
            return None