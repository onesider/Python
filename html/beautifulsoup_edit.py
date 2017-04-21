from bs4 import BeautifulSoup
from urllib import request

html = BeautifulSoup(request.urlopen('https://www.python.org'))
#h1 요소
print(html.h1)

#요소 추가
#html.h1.insert(0,'ham')
#print(html.h1)

#요소 추가 인덱스는 태그를 기준으로 카운트하는 듯함.
#html.h1.insert(3,'egg')
#print(html.h1)

#img 태그대신 span태그를 삽입
#new_tag = html.new_tag('span')
#new_tag.string = 'ham egg'
#html.h1.img.replace_with(new_tag)
#print(html.h1)

#span태그 요소내용을 삭제
#html.h1.span.clear()
#print(html.h1)

#span태그 자체를 삭제
#html.h1.span.decompose()
#print(html.h1)

#앵커 태그를 삭제 함..
html.h1.a.extract()
print(html.h1)

#래핑..div 태그로 html객체를 감싸버림..
wrapper_tag = html.new_tag('div')
wrapper_tag.attrs['class'] = 'wapper'
print(html.h1.wrap(wrapper_tag))
