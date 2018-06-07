import api
import webbrowser
import sys

def print_header():
    print('******* SEARCH TALK PYTHON *******')


def main():
    print_header()

    search_term = input('What keywords to search for? ')
    results = api.search_talk_python_podcast(search_term)
    print(f'There are {len(results)} matching episodes:')

    for result in results:
        print(f'Episode {result.id}: {result.title}')

    choice = input('Do you want to listen to the episode? Please enter the id or type Q to exit: ')
    if choice == 'Q':
        sys.exit('Exiting.....')
    else:
        for r in results:
            if r.id == int(choice):
                full_url = f'https://talkpython.fm{r.url}'
                webbrowser.open(full_url, new=2)
                break


if __name__ == '__main__':
    main()
