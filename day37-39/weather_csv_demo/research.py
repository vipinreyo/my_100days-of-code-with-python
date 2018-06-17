import os
import csv
import collections
import pprint
from typing import List

data = []
Record = collections.namedtuple('Record', 'date, actual_min_temp, actual_max_temp, actual_precipitation')


def init():
    filename = os.path.join(os.path.dirname(__file__), 'data', 'seattle.csv')

    if not data:
        with open(filename) as fin:
            reader = csv.DictReader(fin)

            data.clear()
            for row in reader:
                data.append(parse(row))


def get_hot_days() -> List[Record]:
    return sorted(data, key=lambda x: x.actual_max_temp, reverse=True)


def get_cold_days() -> List[Record]:
    return sorted(data, key=lambda x: x.actual_min_temp)


def get_wettest_days() -> List[Record]:
    return sorted(data, key=lambda x: x.actual_precipitation, reverse=True)


def parse(row):
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['actual_precipitation'] = float(row['actual_precipitation'])

    record = Record(
                date=row.get('date'),
                actual_min_temp=row.get('actual_min_temp'),
                actual_max_temp=row.get('actual_max_temp'),
                actual_precipitation=row.get('actual_precipitation')
                )
    return record
