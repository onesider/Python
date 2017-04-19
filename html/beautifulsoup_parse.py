#pip install beautifulsoup4

from bs4 import BeautifulSoup
from urllib import request
from lxml import html
html = BeautifulSoup(request.urlopen('https://www.python.org'))
#title 요소
print(html.title)
#title 요소의 text
print(html.title.text)
#h1 요소
print(html.h1)
#h1 요소
print(html.find('h1'))
#h1 요소중 이미지 값만 추출
print(html.h1.img)
#h1 요소의 img 요소의 속성값
print(html.h1.img.attrs)
#h1 > img > src
print(html.h1.img['src'])
#id=back-to-top-1
print(html.find(id='back-to-top-1'))
#속성 이름과 값을 사전으로 검색
print(html.find('li',attrs={'class':'shop-meta'}))
