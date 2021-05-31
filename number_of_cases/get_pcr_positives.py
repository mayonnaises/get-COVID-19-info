# -*- coding: utf-8 -*-
'''
Python 3.8

厚生労働省が発表している
新型コロナウイルスの国内陽性者数を取得

網羅的な陽性者数情報を知りたい場合はファイルを実行

特定の日付の陽性者数を知りたい場合は
    get_specified_date 関数を実行

現在日時から特定の日数分前の陽性者数を知りたい場合は
    get_minus_date 関数を実行

実行例:
>>> import get_pcr_positives as pcr
>>> pcr.get_specified_date(2021, 5, 1)
2021年5月1日 の陽性者数 : 5813人
'''


import datetime
import requests


positives_data = {}


def get_date_and_count(data):
    '''['日付', '数'] のリストを返す'''
    info = data.split(',', 1)
    return info


def get_date_text(date):
    '''
    日付の情報を 年/月/日 の文字列に変換して返す
    その際、先頭の0を削除
    Windowsにも対応させるため lstrip を使用
    '''
    year = date.strftime('%Y')
    month = date.strftime('%m').lstrip('0')
    day = date.strftime('%d').lstrip('0')
    date = f'{year}/{month}/{day}'
    return date


def get_positives_data():
    ''' 陽性者数の取得'''
    res = requests.get('https://www.mhlw.go.jp/content/pcr_positive_daily.csv')
    res_content = res.content.decode('utf-8')
    data_list = res_content.splitlines()


    # キーが日付、値が報告された数の辞書に変換
    global positives_data
    positives_data = {info[0]: int(info[1]) for data in data_list[1:]
                      if (info := get_date_and_count(data))}


def get_today_data():
    '''今日の陽性者数'''
    str_now = get_date_text(datetime.datetime.now())

    if (count := positives_data.get(str_now)) is not None:
        print(f'\n今日({str_now}) の陽性者数 : {count}人\n')
    else:
        print(f'\n今日({str_now}) の陽性者数はまだ発表されていません\n')


def get_yesterday_data():
    '''昨日の陽性者数'''
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    str_yesterday = get_date_text(yesterday)

    if (count := positives_data.get(str_yesterday)) is not None:
        print(f'昨日({str_yesterday}) の陽性者数 : {count}人\n')
    else:
        print(f'昨日({str_yesterday}) の陽性者数はまだ発表されていません\n')


def get_two_days_ago():
    '''一昨日の陽性者数'''
    two_days_ago = datetime.datetime.now() - datetime.timedelta(days=2)
    str_day = get_date_text(two_days_ago)

    if (count := positives_data.get(str_day)) is not None:
        print(f'一昨日({str_day}) の陽性者数 : {count}人\n')
    else:
        print(f'一昨日({str_day}) の陽性者数はまだ発表されていません\n')


def get_week_average():
    '''過去７日間の平均陽性者数'''
    now = datetime.datetime.now()
    sum_week_positives = 0

    for day in range(7):
        back_day = get_date_text(now - datetime.timedelta(days=day))

        if (count := positives_data.get(back_day)) is not None:
            sum_week_positives += count

    week_average = sum_week_positives / 7

    print(f'過去７日間の平均陽性者数 : {week_average:.1f}人\n')


def get_month_average():
    '''過去１か月間の平均陽性者数'''
    now = datetime.datetime.now()
    sum_month_positives = 0

    for day in range(30):
        back_day = get_date_text(now - datetime.timedelta(days=day))

        if (count := positives_data.get(back_day)) is not None:
            sum_month_positives += count

    month_average = sum_month_positives / 30

    print(f'過去１か月間の平均陽性者数 : {month_average:.1f}人\n')


def get_sum_positives():
    '''これまでの合計養成者数と
    国内総人口に対する陽性者数の割合'''
    sum_positives = sum(positives_data.values())

    # 国内総人口を1億2550万人と仮定
    percentage =  (sum_positives / 125500000) * 100

    print(f'今日までの合計陽性者数 : {sum_positives}人 (国内人口に対する割合 : 約{percentage:.3f}%)\n')


def get_specified_date(year: int, month: int, day: int):
    '''
    指定された日の陽性者数を取得
    年、月、日 を引数に記述
    注意点: 引数は全て数字で、先頭に0はつけない
    記述例: get_specified_date(2021, 5, 1)
    '''

    get_positives_data()

    date = f'{year}/{month}/{day}'

    if (count := positives_data.get(date)) is not None:
        print(f'{year}年{month}月{day}日 の陽性者数 : {count}人')
    else:
        print(f'指定された日({year}/{month}/{day}) のデータはありません')


def get_minus_date(day: int):
    '''
    引数で指定された日数前の陽性者数を取得

    ３日前のデータを取得したい場合:
        get_minus_date(-3)
    注意点: 引数は負の整数のみ
    '''

    get_positives_data()

    if day > 0:
        print('引数には負の整数を入力してください')
    else:
        # 正の整数に変換
        day *= -1
        # 指定された日数分戻った日付を取得
        get_day = datetime.datetime.now() - datetime.timedelta(days=day)
        str_day = get_date_text(get_day)

        if (count := positives_data.get(str_day)) is not None:
            print(f'{str_day} の陽性者数 : {count}人')
        else:
            print(f'指定された日({str_day}) のデータはありません')


if __name__ == '__main__':
    get_positives_data()
    get_today_data()
    get_yesterday_data()
    get_two_days_ago()
    get_week_average()
    get_month_average()
    get_sum_positives()