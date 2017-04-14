import http.client
conn = http.client.HTTPSConnection("onesider.synology.me", 5001)
conn.request("GET", "/")
r1 = conn.getresponse()
print(r1.status, r1.reason)
print(r1.read())
