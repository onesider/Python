#pip install requests
#해당 모듈을 설치해야만 사용이 가능함.

import requests

#get,head,post,patch,put,delete,option 메소드 지원...
r_get = requests.get('http://httpbin.org/get')
r_options = requests.post('http://gw.withsecurity.co.kr')
#print(r_options)
#print(r_options.text)

r_get2 = requests.get('http://httpbin.org/get', params='example')
#print(r_get2.url)

r_get3 = requests.get('http://httpbin.org/get', params={'key':'value', 'key2':'value2'})
#print(r_get3.url)

#Header Setting
headers = {'Accept':'application/json'}
r_get4 = requests.get('http://httpbin.org/get', headers=headers)

#print(r_get4.text)
#print(r_get4)
#응답값들...
#text로 출력하면 보기좋게 출력됨..좋네..
#request, url, cookie, headers, status_code, ok, text, inter_lines(), json()
print(r_get4.request)
#print(r_get4.headers)
#print(r_get4.status_code)
#print(r_get4.ok)
#print(r_get4.text)

payload = {'id':'onesider'}
r_post = requests.post('http://httpbin.org/get', data=payload)
print(r_post.request)
print(r_post.request.body)
