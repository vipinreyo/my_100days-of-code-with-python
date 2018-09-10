# This example code will automate the login to packt.com and go to 'My ebooks page'
# It also provides an option to search a book of a particular format and print the title and the download link

import os
import re
from dotenv import load_dotenv, find_dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

load_dotenv(find_dotenv())

user = os.getenv('PACKT_USER')
pwd = os.getenv('PACKT_PWD')

DOWNLOAD_URL = "https://www.packtpub.com/ebook_download/{nid}/{ebook_format}"
EBOOK_FORMATS = ['pdf', 'epub', 'mobi']


def get_books(books, name, ebook_format):

    name = name.lower()
    ebook_format = ebook_format.lower()

    if ebook_format not in EBOOK_FORMATS:
        raise ValueError(f'Incorrect ebook format. Available formats are {EBOOK_FORMATS}')

    for nid, title in books.items():
        if re.search(name, title.lower()):
            url = DOWNLOAD_URL.format(nid=nid, ebook_format=ebook_format.lower())
            print(title, url)


def main():
    login = "https://www.packtpub.com/login"
    driver = webdriver.Chrome()
    driver.get(login)

    driver.find_element_by_id('edit-name').send_keys(user)
    driver.find_element_by_id('edit-pass').send_keys(pwd + Keys.RETURN)
    driver.implicitly_wait(3)

    driver.find_element_by_link_text('My eBooks').click()
    elements = driver.find_elements_by_class_name('product-line')

    books = {ele.get_attribute('nid'): ele.get_attribute('title') for ele in elements}
    driver.close()

    get_books(books, 'Python*', 'pdf')


if __name__ == '__main__':
    main()
