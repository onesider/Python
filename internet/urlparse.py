#URL 파싱..
from urllib import parse

result = parse.urlparse('https://www.python.org/doc/;parameter?q=example#hoge')

print('url')
print(result)
print(result.geturl())
print(result.scheme)
print(result[0:3])
print(result.hostname)
