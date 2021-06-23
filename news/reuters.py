# Run with Python 3.9
# news/reuters.py
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


'''
URL : https://jp.reuters.com/

Search REUTERS news sites and get articles about COVID-19.


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
