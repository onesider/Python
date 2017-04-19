from bs4 import BeautifulSoup
from urllib import request

html = BeautifulSoup(request.urlopen('https://www.python.org'))
print(html.h1)

#prettify를 사용하면 인덴트를 깔끔하게 처리해줌..
print(html.h1.prettify())
print(html.h1.a.prettify(formatter='html'))
