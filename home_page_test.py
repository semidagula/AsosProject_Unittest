import unittest

from selenium import webdriver
import time

from unittest_proiectFinal import Locators


class TestHomePage(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.asos.com/')
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test1_homepage_loads(self):
        # Test if the homepage loads successfully
        self.assertEqual(self.driver.title, 'ASOS | Online Shopping for the Latest Clothes & Fashion')

    def test2_accept_cookies(self):
        # Check if the cookies banner is displayed
        cookies_banner = self.driver.find_element(*Locators.COOCKIES_BANNER)
        self.assertTrue(cookies_banner.is_displayed())

        # Accept the cookies
        accept_button = self.driver.find_element(*Locators.ACCEPT_COOCKIES)
        accept_button.click()

        # Verify that the cookies banner is no longer displayed
        self.assertFalse(cookies_banner.is_displayed())

    def test10_facebook_link(self):
        self.driver.find_element(*Locators.FACEBOOK_LINK).click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        expected_facebook_url = "https://www.facebook.com/ASOS/"
        current_url = self.driver.current_url
        self.assertEqual(current_url, expected_facebook_url)
