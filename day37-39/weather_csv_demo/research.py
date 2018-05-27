import os
import csv
import collections
import pprint
from typing import List

data = []
Record = collections.namedtuple('Record', 'date,actual_mean_temp,actual_min_temp,'
                                          'actual_max_temp,average_min_temp,average_max_temp,'
                                          'record_min_temp,record_max_temp,record_min_temp_year,record_max_temp_year,'
                                          'actual_precipitation,average_precipitation,record_precipitation')


def init():
    filename = os.path.join(os.path.dirname(__file__), 'data', 'seattle.csv')

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
    row['actual_mean_temp'] = int(row['actual_mean_temp'])
    row['actual_min_temp'] = int(row['actual_min_temp'])
    row['actual_max_temp'] = int(row['actual_max_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['average_min_temp'] = int(row['average_min_temp'])
    row['record_min_temp'] = int(row['record_min_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_max_temp'] = int(row['record_max_temp'])
    row['record_min_temp_year'] = int(row['record_min_temp_year'])
    row['record_max_temp_year'] = int(row['record_max_temp_year'])
    row['actual_precipitation'] = float(row['actual_precipitation'])
    row['average_precipitation'] = float(row['average_precipitation'])
    row['record_precipitation'] = float(row['record_precipitation'])

    record = Record(**row)
    return record
