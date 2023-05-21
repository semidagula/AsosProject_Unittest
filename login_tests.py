import unittest
from selenium import webdriver
import time

from unittest_proiectFinal import Locators


class TestLoginPage(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.asos.com/')
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test5_login(self):
        accept_button = self.driver.find_element(*Locators.ACCEPT_COOCKIES)
        accept_button.click()
        # Test the login functionality
        self.driver.find_element(*Locators.SIGN_IN).click()
        time.sleep(2)
        self.driver.find_element(*Locators.SIGN_IN_ACC).click()
        time.sleep(2)
        email = self.driver.find_element(*Locators.EMAIL)
        email.send_keys("sem.gula@gmail.com")
        email.submit()

        password_input = self.driver.find_element(*Locators.PASSWORD)
        password_input.send_keys("Supersecret")
        password_input.submit()



    def test6_invalid_login(self):
        accept_button = self.driver.find_element(*Locators.ACCEPT_COOCKIES)
        accept_button.click()
        # Test the login functionality
        self.driver.find_element(*Locators.SIGN_IN).click()
        time.sleep(5)
        self.driver.find_element(*Locators.MY_ACCOUNT).click()
        time.sleep(5)
        email = self.driver.find_element(*Locators.EMAIL)
        email.send_keys("sem.gula@gmail.com")
        email.submit()

        password_input = self.driver.find_element(*Locators.PASSWORD)
        password_input.send_keys()
        password_input.submit()
        time.sleep(2)
        error_message = self.driver.find_element(*Locators.MSG_ERROR).text
        expected_error_message = "Hey, we need a password here"
        assert error_message == expected_error_message
