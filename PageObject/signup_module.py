
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:
    def __init__(self, driver):
        # Define locators
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.signup_link = (By.ID, "signin2")
        self.username_field = (By.ID, "sign-username")
        self.password_field = (By.ID, "sign-password")
        self.signup_button = (By.XPATH, "//button[normalize-space()='Sign up']")

    def sign_up(self,username,password):

        self.wait.until(EC.element_to_be_clickable(self.signup_link)).click()
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)
        self.wait.until(EC.element_to_be_clickable(self.signup_button)).click()
