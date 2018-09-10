# Just dabbling with Selenium
# This program will open the python.org page and search 'pycon'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
ele = driver.find_element_by_name('q')
ele.clear()
ele.send_keys('pycon')
ele.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
