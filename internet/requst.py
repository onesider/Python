import requests

#get,head,post,patch,put,delete,option 메소드 지원...
r_get = requests.get('http://httpbin.org/get')
r_options = requests.post('http://gw.withsecurity.co.kr')
print(r_options)
print(r_options.text)

r_get2 = requests.get('http://httpbin.org/get', params='example')
print(r_get2.url)

r_get3 = requests.get('http://httpbin.org/get', params={'key':'value', 'key2':'value2'})
print(r_get3.url)
