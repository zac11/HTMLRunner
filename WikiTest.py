__author__ = 'rahul'

import unittest
from selenium import webdriver

class MyWikiTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
    def test_Wiki(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('http://en.wikipedia.org')

        driver.find_element_by_id('searchInput').clear()
        driver.find_element_by_id('searchInput').send_keys('Sachin Tendulkar')
        driver.find_element_by_id('searchButton').click()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
