# Run with Python 3.9
# news/afp_bb.py
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

'''
URL : https://www.afpbb.com/

Search AFP BB News sites and get articles about COVID-19.


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


class AFPBBNews:

    def __init__(self):
        self.response = requests.get(
            'https://www.afpbb.com/subcategory/theme-corona')
        self.title_dict = {}

    def __iter__(self):
        parse_result = BeautifulSoup(self.response.text, 'html.parser')

        for parse in parse_result.select('a.block.move'):
            # Get news title and url
            yield [
                parse.find('h3').get_text(strip=True), parse['href']]

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


class SelectNews(AFPBBNews):

    def __init__(self):
        # News site domain
        self.domain = 'https://www.afpbb.com/'

        super().__init__()
        self.get_titles()
        self.display_titles()

    def get_news_body(self, news_info):
        '''Get the body of the news'''
        response = requests.get(self.domain + news_info[1])
        parse = BeautifulSoup(response.text, 'html.parser')
        news_body = parse.select_one(
            'div.article-body').get_text()
        return news_body

    def select(self, numbers: list):
        '''
        Please give a list of news numbers for which you want to know the body.
        '''
        border = '*' * 12

        if isinstance(numbers, list):
            for number in numbers:

                # [news title, news url]
                if (news_info := self.title_dict.get(number)) is not None:
                    news_body = self.get_news_body(news_info)

                    print(f'\n\n{border} {news_info[0]} {border}\n{news_body}')
                else:
                    print(f'\n\nNo.{number} news does not exist.\n'
                          f'Please enter the correct number.')

        else:
            raise TypeError(f'select() argument must be a list')



if __name__ == '__main__':
    afp = AFPBBNews()
    afp.get_titles()
    afp.display_titles()