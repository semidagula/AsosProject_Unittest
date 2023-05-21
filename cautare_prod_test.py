import time
from selenium import webdriver

import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from unittest_proiectFinal import Locators



class TestCautareProduse(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.asos.com/')
        self.driver.maximize_window()
        time.sleep(2)

    def tearDown(self) -> None:
        self.driver.quit()

    def test3_search_functionality(self):
        # Test the search functionality
        search_box = self.driver.find_element(*Locators.SEARCH)
        search_box.send_keys("dress")
        search_box.submit()
        wait = WebDriverWait(self.driver, 60)
        lista = wait.until(EC.visibility_of_all_elements_located(Locators.LISTA_DRESSES))

        assert len(lista) > 10, "Numarul de elemente din lista este mai mare decat 10"

    def test4_invalid_search_functionality(self):
        self.driver.find_element(*Locators.SEARCH).send_keys("excavator")
        self.driver.find_element(*Locators.BTN).click()
        expected_result = "NOTHING MATCHES YOUR SEARCH But don't give up – check the spelling or try less specific search terms.."
        actual_result = self.driver.find_element(*Locators.MSG_ERROR)
        self.assertTrue(expected_result, actual_result)
