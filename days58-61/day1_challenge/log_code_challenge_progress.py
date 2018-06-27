import requests
from datetime import date, timedelta
import sys
import os
from bs4 import BeautifulSoup

TALKPYTHON_URL = 'https://training.talkpython.fm/courses/explore_100days_in_python/100-days-of-code-in-python'
LOG_PROGRESS_FILE = 'log.md'


def get_course_outline():
    response = requests.get(TALKPYTHON_URL)
    response.raise_for_status()

    dom = BeautifulSoup(response.text, 'html.parser')
    chapter_divs = dom.find_all('div', class_ = 'chapter-title')

    outline = []
    day_count = 1
    for div in chapter_divs[1:]:
        a = div.find('a')
        title = a['title'].replace('Watch chapter', '')
        outline.append('{} Day {} (Lectures). '.format(title, day_count))
        outline.append('{} Day {} (Practice).'.format(title, day_count + 1))
        outline.append('{} Day {} (More coding).'.format(title, day_count + 2))
        day_count += 3

    return outline


def write_course_progress(outline, current_progress_day):
    progress_file = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), LOG_PROGRESS_FILE)
    with open(progress_file, 'w') as log:
        log.write('# Progress log\n')
        log.write('| {:<5} | {:<5} | {:<5} |\n'.format('Days', 'Completed on', 'Title'))
        log.write('| {:<5} | {:<5} | {:<5} |'.format('-'*5, '-'*5, '-'*5))
        log.write('\n')

        completed_date = date(2018, 4, 20)
        for idx, course in enumerate(outline[: current_progress_day], 1):
            log.write('| {:<5} | {:<5} | {:<5} |\n'.format(idx, completed_date.strftime('%b %d, %Y'), course))
            completed_date += timedelta(days=1)


def main():
    try:
        current_progress_day = int(input('Enter the day to log the progress [1 - 100]:'))

        if current_progress_day not in range(1, 101):
            raise ValueError
    except ValueError:
        print('Not a valid day. Please enter a day [1 - 100].')
        sys.exit(1)

    outline = get_course_outline()
    write_course_progress(outline, current_progress_day)


if __name__ == '__main__':
    main()
