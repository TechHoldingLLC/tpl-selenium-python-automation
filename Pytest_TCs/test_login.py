import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObject.LogIn_module import LoginIn


def test_login_link(driver):  # Pass driver fixture
    """Verify the login link is clickable."""
    login_page = LoginIn(driver)  # Pass driver instance
    login_page.driver.find_element(*login_page.login_link).click()
    assert driver.find_element(*login_page.username_field), "Login modal did not open"

def test_login_successfully(driver):
    """Verify login with valid credentials."""
    login_page = LoginIn(driver)
    login_page.Login_page("MeghanaSolanki", "Test@1234")
    
    # Wait for login to complete
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )
    
    # Assertion to confirm successful login
    assert driver.find_element(By.ID, "nameofuser").is_displayed(), "Login failed"

def test_login_fail(driver):
    """Verify login fails with incorrect credentials."""
    login_page = LoginIn(driver)
    login_page.Login_page("MeghanaSolanki", "testttt@12")
    
    # Add an assertion for failed login (adjust based on website behavior)
    assert driver.find_element(By.ID, "logInModal").is_displayed(), "Login did not fail as expected"
