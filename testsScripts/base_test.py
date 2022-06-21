from pageFactory.home_page import HomePage
from testsScripts.test_data import TestData
from selenium import webdriver
import unittest


class BaseTest(unittest.TestCase):
    """
    Base class for each test
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.castorama.pl/")
        # Create HomePage class instance
        self.home_page = HomePage(self.driver)
        # Create TestData class instance
        self.test_data = TestData()

    def tearDown(self):
        self.driver.quit()