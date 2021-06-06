# news/afp_bb.py
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

'''

Search AFP BB News sites and get articles about COVID-19.

If you only want to know the title, run the file.
News titles are displayed in a list.

If you want to select the news and get the body, call SelectNewsClass.
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



if __name__ == '__main__':
    afp = AFPBBNews()
    afp.get_titles()
    afp.display_titles()