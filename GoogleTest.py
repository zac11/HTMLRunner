__author__ = 'rahul'

import unittest
from selenium import webdriver


class MyGoogleTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_GoogleTest(self):
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.youtube.com/')

        driver.find_element_by_id('masthead-search-term').clear()
        driver.find_element_by_id('masthead-search-term').send_keys('Metallica')
        driver.find_element_by_id('search-btn').click()



if __name__ == '__main__':
    unittest.main()
