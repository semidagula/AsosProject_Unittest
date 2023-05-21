import time
import unittest

from selenium import webdriver
import time
from unittest_proiectFinal import Locators


class TestAddToCart(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.asos.com/')
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test7_add_to_cart(self):
        self.driver.find_element(*Locators.ACCEPT_COOCKIES).click()
        self.driver.find_element(*Locators.SEARCH).send_keys("bag")
        time.sleep(3)
        self.driver.find_element(*Locators.BTN).click()
        time.sleep(2)
        self.driver.find_element(*Locators.VALENTINO_BAG).click()

        self.driver.find_element(*Locators.ADD_TO_BAG).click()

    def test8_remove_from_cart(self):
        time.sleep(5)
        self.driver.find_element(*Locators.ACCEPT_COOCKIES).click()
        self.driver.find_element(*Locators.SEARCH).send_keys("bag")

        self.driver.find_element(*Locators.BTN).click()
        time.sleep(3)
        self.driver.find_element(*Locators.VALENTINO_BAG).click()
        time.sleep(3)
        self.driver.find_element(*Locators.ADD_TO_BAG).click()
        time.sleep(2)
        self.driver.find_element(*Locators.cart).click()
        time.sleep(3)
        self.driver.find_element(*Locators.REMOVE_CART).click()
        time.sleep(3)
        expected_result = "COȘUL DE CUMPĂRĂTURI ESTE GOL"
        actual_result = self.driver.find_element(*Locators.MSG_ERROR).text
        self.assertEqual(actual_result, expected_result)

    def test9_view_wishlist(self):
        # Test viewing the wishlist
        self.driver.find_element(*Locators.SAVED_LIST).click()
        expected_url = "https://www.asos.com/saved-lists/?nlid=nav%20header"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_url)
