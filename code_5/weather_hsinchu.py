
# -*- coding: utf-8 -*-

from __future__ import print_function
from io import open

import requests
from lxml import html
# from lxml.html import soupparser
# from bs4 import BeautifulSoup

url = 'http://www.cwb.gov.tw/V7/forecast/taiwan/Hsinchu_City.htm'

r = requests.get(url)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)
r.encoding = 'utf-8'
print(type(r.text), len(r.text))
# print(r.text)

# root = soupparser.fromstring(r.text) # parse
root = html.fromstring(r.text) # parse
# print(type(root))
print('-' * 20)


# 'body/div/div/div/div/div/div/h3'   class="CenterTitle"
el_issued = root.find('body/div/div/div/div/div/div/h3/span')
print(el_issued.text)
print('-' * 20)


el_table = root.find('body/div/div/div/div/div/div/table')
for el_ths in el_table.findall('thead/tr/th'):
    print('{:　<9s}'.format(el_ths.text.strip()), end='')
print()

for el_trs in el_table.findall('tbody/tr'):
    th = el_trs.find('th')
    print('{:　<9s}'.format(th.text.split()[0]), end='')
    for td in el_trs.findall('td'):
        if td.find('img') is not None and td.find('img').get('title'):
            print('{:　<9s}'.format(td.find('img').get('title').strip()), end='')
        else:
            print('{:　<9s}'.format(td.text.strip()), end='')
    print()
print()
    
    
####

# def count_eng(s):
    # return sum(1 for c in s if ord(c) <= 127)

# el_table = root.find('body/div/div/div/div/div/div/table')
# for el_ths in el_table.findall('thead/tr/th'):
    # s = el_ths.text.strip()
    # count = count_eng(s)
    # print('{:　<{cnt}s}'.format(s, cnt=7+count), end='')
# print()

# for el_trs in el_table.findall('tbody/tr'):
    # th = el_trs.find('th')
    # print('{:　<9s}'.format(th.text.split()[0]), end='')
    # for td in el_trs.findall('td'):
        # if td.find('img') is not None and td.find('img').get('title'):
            # print('{:　<9s}'.format(td.find('img').get('title').strip()), end='')
        # else:
            # print('{:　<9s}'.format(td.text.strip()), end='')
    # print()
# print()

    