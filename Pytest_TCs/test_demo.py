import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Chrome auto-handled by Selenium Manager
    driver.maximize_window()
    yield driver  # Provide the driver to test cases
    driver.quit()  # Close the browser after test execution

def perform_signup(driver, username, password):
    """Function to perform the signup action"""
    driver.find_element(By.ID, "signin2").click()  # Click on Sign up button
    time.sleep(2)  # Wait for modal to appear

    driver.find_element(By.ID, "sign-username").send_keys(username)  # Enter username
    driver.find_element(By.ID, "sign-password").send_keys(password)  # Enter password
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()  # Click Sign up button
    time.sleep(2)  # Wait for alert

    alert = driver.switch_to.alert
    response_message = alert.text
    alert.accept()  # Close the alert

    return response_message

@pytest.mark.order(1)
def test_signup_success(browser: WebDriver):
    browser.get("https://www.demoblaze.com/index.html")  # Launch website
    username = "MeghanaSolanki1.5"
    password = "Test@1234"

    response = perform_signup(browser, username, password)  # Call helper function
    assert response == "Sign up successful."  # Validate success message

@pytest.mark.order(2)
def test_signup_without_UN(browser: WebDriver):
    browser.get("https://www.demoblaze.com/index.html")
    username = ""
    password = "Test@1234"

    response = perform_signup(browser, username, password)
    assert response == "Please fill out Username and Password."

@pytest.mark.order(3)
def test_signup_without_PW(browser: WebDriver):
    browser.get("https://www.demoblaze.com/index.html")
    username = "MeghanaSolanki"
    password = ""

    response = perform_signup(browser, username, password)
    assert response == "Please fill out Username and Password."

@pytest.mark.order(4)
def test_signup_duplicate(browser: WebDriver):
    browser.get("https://www.demoblaze.com/index.html")
    username = "MeghanaSolanki"  # Reusing the same username
    password = "Test@1234"

    response = perform_signup(browser, username, password)
    assert response == "This user already exist."

