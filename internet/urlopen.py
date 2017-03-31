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

url = request.Request('http://httpbin.org/get', method='HEAD')
res = request.urlopen(url)
#method 값이 HEAD면 res.read()로 읽어올 값이 없음..
print(res.code)
