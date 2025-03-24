import selenium
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Purchase_mobile():
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.laptop = (By.XPATH, "(//a[normalize-space()='Laptops'])[1]")
        self.sony = (By.XPATH, "//a[normalize-space()='Sony vaio i5']")
        self.Addtocart = (By.XPATH, "//a[normalize-space()='Add to cart']")

    def mobiledevice(self):
        self.wait.until(EC.element_to_be_clickable)(self.laptop).click()
        self.wait.until(EC.element_to_be_clickable)(self.sony).click()
        self.wait.until(EC.element_to_be_clickable)(self.Addtocart).click()
 