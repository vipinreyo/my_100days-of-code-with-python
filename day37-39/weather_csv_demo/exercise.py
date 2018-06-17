import research
import cProfile
profiler = cProfile.Profile()
profiler.disable()


def main():
    profiler.enable()
    # init
    research.init()
    hot_days = research.get_hot_days()
    cold_days = research.get_cold_days()
    wet_days = research.get_wettest_days()
    profiler.disable()

    # print the 5 hottest days
    print('5 Hottest days')
    for day in hot_days[:5]:
        print(f'{day.actual_max_temp}F on {day.date}')

    # print the 5 coolest dates
    print()
    print('5 Coldest days')
    for day in cold_days[:5]:
        print(f'{day.actual_min_temp}F on {day.date}')

    # print the wettest dates
    print()
    print('5 Wettest days')
    for day in wet_days[:5]:
        print(f'{day.actual_precipitation} inches on {day.date}')


if __name__ == '__main__':
    for _ in range(1, 100):
        main()

    profiler.print_stats(sort='cumtime')