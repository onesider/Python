#URL 파싱..
from urllib import parse

result = parse.urlparse('https://www.python.org/doc/;parameter?q=example#hoge')

print('url')
print(result)
print(result.geturl())
print(result.scheme)
print(result[0:3])
print(result.hostname)

print('\nquery')
result2 = parse.urlparse('https://google.co.kr/search?q=python&oq=python&sourceid=chrome&ie=UTF-8')
print(result2.query)

#딕셔너리형태로 출력
print(parse.parse_qs(result2.query))

#하나의 키에 값이 두개 일때
print(parse.parse_qs('key=1&key=2'))

#파싱된 결과를 퓨플로 받고싶을때
print(parse.parse_qsl(result2.query))

#키값이 같을때 두개다 출력
print(parse.parse_qsl('key=1&key=2'))

#keep_blank_values 옵션 차이점
print("")
print(parse.parse_qs('key1=&key2=hong'))
print(parse.parse_qs('key1=&key2=hong', keep_blank_values=True))
