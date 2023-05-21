import unittest

import HtmlTestRunner

from unittest_proiectFinal.add_to_cart_test import TestAddToCart
from unittest_proiectFinal.cautare_prod_test import TestCautareProduse
from unittest_proiectFinal.home_page_test import TestHomePage
from unittest_proiectFinal.login_tests import TestLoginPage


class MyTestSuites(unittest.TestCase):

    # se ruleaza testele si se vor crea rapoarte
    def test_suite(self):
        smoketest = unittest.TestSuite()
        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestLoginPage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestCautareProduse),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestHomePage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestAddToCart)

        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Report', report_name='smoke Test', combine_reports=True
        )
        runner.run(smoketest)
