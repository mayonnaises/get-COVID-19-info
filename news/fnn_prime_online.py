# news/fnn_prime_online.py
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

'''
2021/6

URLs that FNN Prime Online allows to crawl

Allow: /
'''


class FNNPrimeOnline:
    def __init__(self):
        self.response = requests.get(
            'https://www.fnn.jp/search?fulltext=コロナ')
        self.title_dict = {}

    def __iter__(self):
        parse_result = BeautifulSoup(self.response.text, 'html.parser')
        for parse in parse_result.select('a.m-article-item__link'):
            yield [
                parse.find('h2').get_text(strip=True), parse['href']]

    def get_titles(self):
        self.title_dict = {
            index: titles for index, titles in enumerate(self.__iter__(), 1)}

    def display_titles(self):
        for index, title in self.title_dict.items():
            print(f'\n{index} : {title[0]}')


class SelectNews(FNNPrimeOnline):

    def __init__(self):
        super().__init__()
        self.get_titles()
        self.display_titles()

    def select(self, *args: list):
        pass



if __name__ == '__main__':
    # fnn = FNNPrimeOnline()
    # fnn.get_titles()
    # fnn.display_titles()


    select = SelectNews()
    # select.display()