import research


def main():
    # init
    research.init()

    # print the 5 hottest days
    print('5 Hottest days')
    hot_days = research.get_hot_days()
    for day in hot_days[:5]:
        print(f'{day.actual_max_temp}F on {day.date}')

    # print the 5 coolest dates
    print()
    print('5 Coldest days')
    cold_days = research.get_cold_days()
    for day in cold_days[:5]:
        print(f'{day.actual_min_temp}F on {day.date}')

    # print the wettest dates
    print()
    print('5 Wettest days')
    wet_days = research.get_wettest_days()
    for day in wet_days[:5]:
        print(f'{day.actual_precipitation} inches on {day.date}')


if __name__ == '__main__':
    main()
