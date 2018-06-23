import datetime

from blog_client import BlogClient


def main():
    val = 'RUN'

    while val:
        print('What would you like to do?')
        selection = input('Please enter read[r] or write[w] to continue: ')

        if selection == 'r':
            read_posts()

        if selection == 'w':
            write_posts()


def read_posts():
    svc = BlogClient()
    response = svc.all_entries()

    posts = response.json()

    for idx, p in enumerate(posts, 1):
        print(f"{idx}. {p.get('view_count')} views for {p.get('title')}")

    print()

    selected = int(input('Which number to view? '))
    selected_id = posts[selected - 1].get('id')

    response = svc.entry_by_id(selected_id)

    selected_post = response.json()

    print('Details of the selected post: {}'.format(selected_id))
    print('Title: {}'.format(selected_post.get('title')))
    print('Written: {}'.format(selected_post.get('published')))
    print('Content: {}'.format(selected_post.get('content')))
    print()
    print()


def write_posts():
    svc = BlogClient()

    title = input('Title: ')
    views = int(input('View count: '))
    content = input('Content: ')

    resp = svc.add_new_entry(title, content, views)

    print()
    print('Create the new post successfully: {}'.format(resp.json().get('id')))
    print()


if __name__ == '__main__':
    main()
