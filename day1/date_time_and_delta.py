
from datetime import datetime
from datetime import date
from datetime import timedelta


def main():
    today = datetime.today()
    print(today, type(today))

    todaydate = date.today()
    print(todaydate, type(todaydate))

    christmas = date(2018, 12, 25)

    if christmas is not todaydate:
        print("Sorry, there are still " + str((christmas - todaydate).days) + " days till Christmas!")
    else:
        print("It's Christmas today :)")

    delta = timedelta(days=4, hours=5)
    print("{} days and {} seconds ".format(delta.days, delta.seconds))

    eta = timedelta(hours=6)
    print(today)
    print(today + eta)


if __name__ == '__main__':
    main()
