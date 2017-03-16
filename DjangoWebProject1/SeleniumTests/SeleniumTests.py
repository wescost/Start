from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest

class SeleniumTests(unittest.TestCase):
    """description of class"""

    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://www.ukr.net")

    def test1(self):
        driver=self.driver

    def tearDown(self):
        self.driver.quit()   

if __name__ == '__main__':
    unittest.main()
