import re
CONTENT_HTML = 'content_html.htm'


def read_and_parse_file(file_name):
    pat = re.compile('\d+:\d+')
    with open(file_name, 'r') as html:
        return pat.findall(html.read())


def calculate_course_time(parsed_data):
    mins = 0
    seconds = 0

    for data in parsed_data:
        min, sec = data.split(':')

        mins += int(min)
        seconds += int(sec)

    return (mins/60) + (seconds/3600)


def main():
    total_course_hr = calculate_course_time(read_and_parse_file(CONTENT_HTML))
    print(f'Total course time is {round(total_course_hr, 2)}hrs')


if __name__ == '__main__':
    main()
