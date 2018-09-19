# This is a trial to auotmate the 'claim my ebook' feature of Packt using Selenkum.
# But this won't work unless user attempts the captcha. But atleast a good try :)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv, find_dotenv
import time
import os

load_dotenv(find_dotenv())

url = "https://www.packtpub.com/packt/offers/free-learning"
user = os.getenv('PACKT_USER')
pwd = os.getenv('PACKT_PWD')


def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)

    time.sleep(3)
    driver.find_element_by_xpath("//*[@class='login-popup']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='email']").clear()
    driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='email']").send_keys(user)
    driver.implicitly_wait(2)
    driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='password']").clear()
    driver.find_element_by_xpath("//div[@id='account-bar-form']//input[@id='password']").send_keys(pwd + Keys.RETURN)
    time.sleep(20)
    driver.find_element_by_id('free-learning-claim').click()
    input('Hello')


if __name__ == '__main__':
    main()
