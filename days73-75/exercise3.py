# Just dabbling with Selenium
# Unit test to check if https://python/org is open and search for 'python' is successful

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://python.org")
        e = driver.find_element_by_name('q')
        e.clear()
        e.send_keys('pycon')
        e.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
