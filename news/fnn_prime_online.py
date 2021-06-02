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

    def get_title_list(self):
        parse_result = BeautifulSoup(self.response.text, 'html.parser')

        for parse in parse_result.select('a.m-article-item__link'):
            print(parse.find('h2').get_text(strip=True))
            print(parse['href'])


if __name__ == '__main__':
    fnn = FNNPrimeOnline()
    fnn.get_title_list()