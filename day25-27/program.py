import api


def main():
    keyword = input('Please enter keyword: ')
    try:
        for r in api.find_movie_by_title(keyword):
            print(r.title)
    except ValueError as ve:
        print(ve)
    except TypeError as te:
        print(f'Empty result. {te}')
    except StopIteration as se:
        print(f'Cannot iterate through the collections. {se}')
    except Exception as e:
        print(f'{e}')


if __name__ == '__main__':
    main()
