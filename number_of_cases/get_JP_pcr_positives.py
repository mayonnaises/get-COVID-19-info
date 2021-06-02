# Run with Python 3.9
# -*- coding: utf-8 -*-

'''
Get the number of positive COVID-19
announced by the Japanese Ministry of Health, Labor and Welfare.


If you want to know the information comprehensively, please execute the file.

If you want to know the number of positives on a particular date:
    Execute get_specified_date function

If you want to know the number of positives a few days before the current date and time:
    Specify the number of days to be subtracted as an argument
    Execute get_minus_date function


Execution example:
>>> import get_pcr_positives as pcr
>>> pcr.get_specified_date(2021, 5, 1)
Number of positives 2021/5/1 : 5813 people
'''


import datetime
import requests


positives_data = {}


def get_date_and_count(data):
    '''
    Returns a list in ['date', 'number'] format.
    number : Number of positives
    '''
    info = data.split(',', 1)
    return info


def get_date_text(date):
    '''
    Convert a datetime object to a string in 'year/month/date' format.
    Remove the leading '0' in the string.
    Use lstrip func to support Windows.
    '''
    year = date.strftime('%Y')
    month = date.strftime('%m').lstrip('0')
    day = date.strftime('%d').lstrip('0')
    date = f'{year}/{month}/{day}'
    return date


def get_positives_data():
    '''Get the number of positive'''
    res = requests.get('https://www.mhlw.go.jp/content/pcr_positive_daily.csv')
    res_content = res.content.decode('utf-8')
    data_list = res_content.splitlines()


    # Convert to a python dictionary
    # The key is the date and the value is the number reported
    global positives_data
    positives_data = {info[0]: int(info[1]) for data in data_list[1:]
                      if (info := get_date_and_count(data))}


def get_today_data():
    '''Get the number of positives today'''
    str_now = get_date_text(datetime.datetime.now())

    if (count := positives_data.get(str_now)) is not None:
        print(f'\nNumber of positives in today({str_now}) : {count} people\n')
    else:
        print(f'\nThe number of positives today({str_now}) has not yet been announced. \n')


def get_yesterday_data():
    '''Get the number of positives yesterday'''
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    str_yesterday = get_date_text(yesterday)

    if (count := positives_data.get(str_yesterday)) is not None:
        print(f'Number of positives in yesterday({str_yesterday}) : {count} people\n')
    else:
        print(f'The number of positives yesterday({str_yesterday}) has not yet been announced.\n')


def get_two_days_ago():
    '''Get the number of positives 2 days ago'''
    two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)
    str_day = get_date_text(two_days_ago)

    if (count := positives_data.get(str_day)) is not None:
        print(f'Number of positives in two days age({str_day}) : {count} people\n')
    else:
        print(f'The number of positives two days ago({str_yesterday}) has not yet been announced.\n')


def get_week_average():
    '''
    Get the average number of positives over the last 7 days
    '''
    now = datetime.datetime.now()
    sum_week_positives = 0

    for day in range(7):
        back_day = get_date_text(now - datetime.timedelta(days=day))

        if (count := positives_data.get(back_day)) is not None:
            sum_week_positives += count

    week_average = sum_week_positives / 7

    print(f'Average number of positives over the last 7 days : {week_average:.1f} people\n')


def get_month_average():
    '''
    Get the average number of positives over the past month
    '''
    now = datetime.datetime.now()
    sum_month_positives = 0

    for day in range(30):
        back_day = get_date_text(now - datetime.timedelta(days=day))

        if (count := positives_data.get(back_day)) is not None:
            sum_month_positives += count

    month_average = sum_month_positives / 30

    print(f'Average number of positives over the past month : {month_average:.1f} people\n')


def get_sum_positives():
    '''
    Get the total number of positives so far
    and the ratio of the number of positives to the total population in Japan.
    '''
    sum_positives = sum(positives_data.values())

    # Assuming a total population of 125.5 million in Japan
    percentage =  (sum_positives / 125500000) * 100

    print(f'Total number of positives to date : {sum_positives} people (Percentage of the Japanese population : About {percentage:.3f}%)\n')


def get_specified_date(year: int, month: int, day: int):
    '''
    Get the number of positives on a specified day.
    Argument: Year, Month, Date
    Note: Arguments are numbers only, do not start with 0
    Description example: get_specified_date(2021, 5, 1)
    '''

    get_positives_data()

    date = f'{year}/{month}/{day}'

    if (count := positives_data.get(date)) is not None:
        print(f'Number of positives in {year}/{month}/{day} : {count} people')
    else:
        print(f'There is no data for the specified date ({year}/{month}/{day})')


def get_minus_date(day: int):
    '''
    Get the number of positives a few days before the current date and time.

    If you want to get the number of positives 3 days ago:
        get_minus_date(-3)
    Note: Arguments are only negative integers to prioritize visibility
    '''

    get_positives_data()

    if day > 0:
        print('Enter a negative integer for the argument.')
    else:
        # Convert to a positive integer
        day *= -1
        # Get date
        get_day = datetime.datetime.now() - datetime.timedelta(days=day)
        str_day = get_date_text(get_day)

        if (count := positives_data.get(str_day)) is not None:
            print(f'Number of positives in {str_day} : {count} people')
        else:
            print(f'There is no data for the specified date ({str_day})')


if __name__ == '__main__':
    get_positives_data()
    get_today_data()
    get_yesterday_data()
    get_two_days_ago()
    get_week_average()
    get_month_average()
    get_sum_positives()