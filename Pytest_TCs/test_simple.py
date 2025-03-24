import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from conftest import driver,userlogin

'''def test_login(driver):
    driver.find_element(By.ID, "signin2").click()
    time.sleep(2)  # Wait for modal to appear

    driver.find_element(By.ID, "sign-username").send_keys("Meghana1")  # Enter username
    driver.find_element(By.ID, "sign-password").send_keys("Solanki1")  # Enter password
    driver.find_element(By.XPATH, "//button[text()='Sign up']").click()  # Click Sign up button
    time.sleep(2)  # Wait for alert

    alert = driver.switch_to.alert
    alert.accept() 
    time.sleep(2)'''

def test_addtocart (driver):
    driver.find_element(By.XPATH, "(//a[normalize-space()='Laptops'])[1]").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[normalize-space()='Sony vaio i5']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[normalize-space()='Add to cart']").click()
    time.sleep(3)
    alert = driver.switch_to.alert
    alert.accept() 
    time.sleep(2)
