"""As explained by Bob in the plotly talkpythin course, this is my attempt to replicate the Pybites graphs without
looking at exercise video"""

import feedparser
from datetime import datetime
from collections import Counter
import plotly
import plotly.graph_objs as go
import re


def get_year_and_month_of_entries(entry_date_string):
    date_str = entry_date_string.split('+')[0].strip()
    entry_date = datetime.strptime(date_str, "%a, %d %b %Y %H:%M:%S")
    return f'{entry_date.year}-{entry_date.month}'


def get_category(link):
    known = dict(codechallenge='challenge',
                 twitter='news',
                 special='special',
                 guest='guest')
    category = re.sub(r'.*\.es/([a-z]+).*', r'\1', link)
    default = 'article'
    return known.get(category) or default


def transpose_list_of_tuples(data):
    if isinstance(data, dict):
        data = data.items()

    return list(zip(*data))


def main():
    blog = feedparser.parse('http://projects.bobbelderbos.com/pcc/dates/all.rss.xml')
    entries = blog['entries']

    pub_dates = [get_year_and_month_of_entries(entry.published) for entry in entries]
    posts_per_month = Counter(pub_dates)
    dates_as_x_axis, entry_count_as_y_axis = transpose_list_of_tuples(posts_per_month)
    data = [go.Bar(x=dates_as_x_axis, y=entry_count_as_y_axis)]
    plotly.offline.plot(data)

    categories = [get_category(entry.link) for entry in entries]
    categories_cnt = Counter(categories)
    labels, values = transpose_list_of_tuples(categories_cnt)
    pie = go.Pie(labels=labels, values=values)
    plotly.offline.plot([pie])

    tags = [tag.term.lower() for entry in entries for tag in entry.tags]
    tags_cnt = Counter(tags)
    top_tags = tags_cnt.most_common(20)
    labels, values = transpose_list_of_tuples(top_tags)
    tags = go.Pie(labels=labels, values=values)
    plotly.offline.plot([tags])


if __name__ == '__main__':
    main()
