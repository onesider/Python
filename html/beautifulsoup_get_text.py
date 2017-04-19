from bs4 import BeautifulSoup
from urllib import request

html = BeautifulSoup(request.urlopen('https://www.python.org'))
tag = html.find('div',attrs={'id':'nojs'})
print(tag)

#태그를 제거하고 출력
print(tag.get_text(strip=True))

#separator : 태그로잘려있던 위치에 지정한 문자열삽입
#strip : True를 지정하면 빈행을 제외
print(tag.get_text(separator='-- '))
