import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PageObject.signup_module import SignupPage
import time

@pytest.mark.order(1)
def test_signup_link(driver):
    signuplink = SignupPage(driver)
    signuplink.driver.find_element(*signuplink.signup_link).click()
    time.sleep(3)
  

@pytest.mark.skip
def test_signup_success(driver):

    signuppage = SignupPage(driver)
    signuppage.sign_up("MeghanaSolanki1.9", "Test@1234")
    alert = driver.switch_to.alert
    alert.accept()  # Close the alert
    response = alert.text
    assert response == "Sign up successful."


@pytest.mark.order(4)
def test_signup_existing_user(driver):

    signuppage = SignupPage(driver)
    signuppage.sign_up("MeghanaSolanki", "Test@1234")
    response = test_signup_success(driver)  # Call helper function
    assert response == "This user already exist."


@pytest.mark.order(2)
def test_signup_without_username(driver):
   
    signuppage = SignupPage(driver)
    signuppage.sign_up("", "ValidPass123")
    response = test_signup_success(driver)  # Call helper function
    assert response == "Please fill out Username and Password."

@pytest.mark.order(5)
def test_signup_without_password(driver):

    signuppage = SignupPage(driver)
    signuppage.sign_up("NewUser567", "")
    response = test_signup_success(driver)  # Call helper function
    assert response == "Please fill out Username and Password."


@pytest.mark.order(3)
def test_signup_special_characters(driver):

    signuppage = SignupPage(driver)
    signuppage.sign_up("User@#$$$$&*(12)", "SecurePass123")
    response = test_signup_success(driver)  # Call helper function
    assert response == "Sign up successful." 


