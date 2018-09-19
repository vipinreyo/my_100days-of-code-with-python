# Selenium auotmation of bunnings.com.au
# Automates the Sign Up process

from selenium import webdriver
import time

url = "https://bunnings.com.au"
first_name = "Vipin"
last_name = "Reyaroth"
post_code = "1234"
email = "mymail@outlook.com"
pwd = 'Apple123'


def main():
    driver = webdriver.Chrome()
    driver.get(url)
    assert "not found" not in driver.page_source

    time.sleep(5)

    driver.find_element_by_xpath("//*[@href='/login']").click()

    time.sleep(3)

    driver.find_element_by_id('body_1_LoginForm_SignUp').click()

    time.sleep(3)

    driver.find_element_by_id('body_1_RegistrationDetailsCtrl_firstname').send_keys(first_name)
    driver.find_element_by_id('body_1_RegistrationDetailsCtrl_lastname').send_keys(last_name)
    driver.find_element_by_id('body_1_RegistrationDetailsCtrl_postcode').send_keys(post_code)
    driver.find_element_by_id('body_1_RegistrationDetailsCtrl_email').send_keys(email)
    driver.find_element_by_id('body_1_PasswordCtrl_password').send_keys(pwd)
    driver.find_element_by_id('body_1_PasswordCtrl_confirmpassword').send_keys(pwd)
    driver.find_element_by_id('body_1_tnc').click()
    driver.find_element_by_id('body_1_RegisterButton').click()

    time.sleep(5)

    assert email in driver.page_source
    driver.find_element_by_xpath("//*[@href='/logoff']").click()


if __name__ == '__main__':
    main()
