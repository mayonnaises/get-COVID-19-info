# Run with Python 3.9
# news/cnn.py
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

class BBCNews:

    def __init__(self):
        self.response = requests.get(
            'https://www.bbc.com/japanese/52137815')
        self.title_dict = {}

    def __iter__(self):
        parse_result = BeautifulSoup(self.response.text, 'html.parser')

        for parse in parse_result.select('h3.evnt13t1'):
            # Get news title and url
            link = parse.find('a')
            yield [
                link.get_text(strip=True), link['href']]

    def get_titles(self):
        '''
        key: News number
        value: List news title and url
        '''
        self.title_dict = {
            index: titles for index, titles in enumerate(self.__iter__(), 1)}
        print(self.title_dict)

    def display_titles(self):
        for index, title in self.title_dict.items():
            print(f'\n{index} : {title[0]}')


if __name__ == '__main__':
    bbc = BBCNews()
    bbc.get_titles()
    bbc.display_titles()
