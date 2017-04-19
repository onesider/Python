import re
from bs4 import BeautifulSoup
from urllib import request

html = BeautifulSoup(request.urlopen('https://www.python.org'))
#모든 a 요소를 얻음
url_list = html.find_all('a')
for url in url_list:
    print(url['href'])

#리미트를 걸수 있음
docs_list = html.find_all(href=re.compile('^http(s)?://docs'),limit=2)
#for doc in docs_list:
#    print(doc['href'])
