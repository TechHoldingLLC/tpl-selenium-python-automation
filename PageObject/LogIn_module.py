import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginIn ():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.login_link = (By.ID, "login2")
        self.username_field = (By.ID, "loginusername")
        self.password_field = (By.ID, "loginpassword")
        self.login_button = (By.XPATH, "//button[@onclick='logIn()']")
        
    def Login_page(self, username, password):
        self.wait.until(EC.element_to_be_clickable(self.login_link)).click()
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()