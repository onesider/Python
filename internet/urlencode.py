from urllib import parse

#사전으로 넘어가면 순서를 보장할수 없음.
print(parse.urlencode({'key1':1, 'key2':2, 'key3':'파이선'}))
print(parse.urlencode([('key1',1), ('key2',2), ('key3','파이선')]))

#key2의 값이 시퀀스인 자료구조
query={'key1':'hong', 'key2':['fuga','piyo']}
print('')
#doseq는 기본적으로 False ['faga','piyo'] 는 문자열로 인식
print(parse.urlencode(query))

#하나의 키에 여러개의 값이 존재하는걸로 해석함..doseq
print(parse.urlencode(query,doseq=True))
