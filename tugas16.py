import unittest
#import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
        webdriver.Chrome(ChromeDriverManager().install())
        webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.url ="https://www.saucedemo.com/"
    def test_a_success_login(self):
        driver = self.browser #buka web browser
        driver.get("self.url") # buka situs
        driver.find_element(By.ID,"user-name").send_keys("standard_user") # isi email
        driver.find_element(By.ID,"password").send_keys("secret_sauce") # isi password
        driver.find_element(By.ID, "login-button").click()

        # validasi
        response_data = driver.find_element(By.CLASS_NAME,"title").text
        self.assertIn('PRODUCTS', response_data)
    
    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()