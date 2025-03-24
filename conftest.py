import pytest
from selenium import webdriver
from PageObject.LogIn_module import LoginIn
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()  # Chrome auto-handled by Selenium Manager
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/index.html")  # Launch website
    yield driver
    driver.quit()  # Close the browser after test execution


@pytest.fixture
def userlogin():
    driver = webdriver.Chrome()  # Chrome auto-handled by Selenium Manager
    driver.maximize_window()
    driver.get("https://www.demoblaze.com/index.html")  # Launch website
    login_page = LoginIn(driver)
    login_page.Login_page("MeghanaSolanki", "Test@1234")
    
    # Wait for login to complete
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "nameofuser"))
    )
    
    # Assertion to confirm successful login
    assert driver.find_element(By.ID, "nameofuser").is_displayed(), "Login failed"
    yield driver
    driver.quit()  # Close the browser after test execution