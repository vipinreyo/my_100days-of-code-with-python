import pyperclip


def get_text_from_clipboard():
    return pyperclip.paste()


def replace_text_and_copy_to_clipboard(clip_text):
    print(clip_text)
    text = input('Enter text to search: ')
    replace_text = input('Enter text to replace: ')
    clip_text = clip_text.replace(text, replace_text)
    pyperclip.copy(clip_text)


def main():
    clip_text = get_text_from_clipboard()

    if not clip_text:
        print('No data in clipboard.')
    else:
        replace_text_and_copy_to_clipboard(clip_text)
        updated_clip_text = get_text_from_clipboard()
        print(updated_clip_text)


if __name__ == '__main__':
    main()
