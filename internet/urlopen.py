from urllib import request

res = request.urlopen('http://httpbin.org/get')
#print(res.code)
#print(res.read().decode(),'\n')

res = request.urlopen('http://httpbin.org/get?key1=value1')
#print(res.code)
#print(res.read().decode())

#Header Setting
headers = {'Amcept':'applicaiton/json'}

#Headers를 사용할려면 request.Request 객체에 포함시킨 후 urlopen을 수행해야함.
url = request.Request('http://httpbin.org/get', headers=headers)
res = request.urlopen(url)
#print(res.read().decode())

#HEAD
#url = request.Request('http://httpbin.org/get', method='HEAD')
url = request.Request('http://gw.withsecurity.co.kr', method='HEAD')
res = request.urlopen(url)
#method 값이 HEAD면 res.read()로 읽어올 값이 없음..
#원래는 있어야하지만 httpbin에서는 반응을 하지 않는듯..
print(res.code)
str1 = res.read()
print(str1.decode('utf-8'))
#print(res.read())
