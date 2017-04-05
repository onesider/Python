import base64

s = 'Python은 좋다'
print(s.encode())

#바이트 형태 데이터가 들어가야지 스트링이 들어가면 오류남...
print(base64.b64encode(s.encode()))
