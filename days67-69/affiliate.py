import pyperclip
AFFLIATE_CODE = '&pybyte0123'


def main():
    url = pyperclip.paste()

    if 'amazon' not in url:
        print('Sorry, no update done to clipboard')
    else:
        print('Amazon affiliate url copied to clipboard')
        pyperclip.copy(url + AFFLIATE_CODE)
        print(url + url + AFFLIATE_CODE)


if __name__ == '__main__':
    main()
