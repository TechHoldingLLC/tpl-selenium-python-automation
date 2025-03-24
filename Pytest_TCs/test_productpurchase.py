import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import userlogin
from PageObject.Product_Purchase import Purchase_mobile
import time
from PageObject.LogIn_module import LoginIn

def test_addtocart(userlogin):
    mobiledevice = Purchase_mobile
