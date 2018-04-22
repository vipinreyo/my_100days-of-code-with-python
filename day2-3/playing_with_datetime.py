import datetime as datetime
import pytz

def main():
    # Creating a datetime object using strptime function
    input_date_string = '7/Aug/2017:15:10:01'
    input_date = datetime.datetime.strptime(input_date_string, '%d/%b/%Y:%H:%M:%S')
    print(input_date)

    # Displaying datetime with timezones (using pytz package) and strftime function
    event_date = input_date.replace(tzinfo=pytz.UTC)
    print(event_date.strftime('%m/%d/%Y %H:%M:%S %Z'))
    user_tz = pytz.timezone('Australia/Sydney')
    local_date = event_date.astimezone(user_tz)
    print(local_date.strftime('%m/%d/%Y %H:%M:%S %Z'))

    # Rounding the datetime to an hour
    local_date = local_date.replace(minute=0, second=0, microsecond=0)
    print(local_date.strftime('%m/%d/%Y %H:%M:%S %Z'))

    # Finding this week's and last week's Mondays
    today = datetime.datetime.now()
    monday = (today - datetime.timedelta(days=today.weekday())).replace(minute=0, second=0, microsecond=0)
    print(monday)
    last_week_monday = (monday - datetime.timedelta(days=7))
    print(last_week_monday)


if __name__ == '__main__':
    main()
