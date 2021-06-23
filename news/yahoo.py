# Run with Python 3.9
# news/yahoo.py
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


'''
URLs that Yahoo news allows to crawl

Allow: /

Disallow: /comment/plugin/
Disallow: /comment/violation
Disallow: /profile/violation
Disallow: /polls/widgets/
Disallow: /articles/*/comments
Disallow: /articles/*/order


URL : https://news.yahoo.co.jp/


Search Yahoo news sites and get articles about COVID-19.

If you only want to know the title, run the file.
News titles are displayed in a list.

If you want to select the news and get the body, call SelectNews class.
By passing the number list of the news,
those body will be displayed.

Execution example:

    # A list of titles will be displayed as soon as they are instantiation
    >>> news = SelectNews()
    1: news title ...
    2: news title ...
           .
           .

    >>> news.select([1, 3])
    ***** news title *****
           new body
              .
              .
'''


class YahooNews:
    def __init__(self):
        self.response = requests.get(
            'https://news.yahoo.co.jp/search?p=コロナウイルス&ei=utf-8')
        self.title_dict = {}

    def __iter__(self):
        parse_result = BeautifulSoup(self.response.text, 'html.parser')

        for parse in parse_result.select('div.newsFeed_item_title'):
            # Get news title and url
            yield [
                parse.get_text(strip=True)]

    def get_titles(self):
        '''
        key: News number
        value: List news title and url
        '''
        self.title_dict = {
            index: titles for index, titles in enumerate(self.__iter__(), 1)}

    def display_titles(self):
        for index, title in self.title_dict.items():
            print(f'\n{index} : {title[0]}')


if __name__ == '__main__':
    yahoo = YahooNews()
    yahoo.get_titles()
    yahoo.display_titles()