#coding:utf-8

import requests

'''
s = requests.Session()
url = 'https://httpbin.org/cookies/set/sessioncookie/123456789'
s.get(url)

url_cookie = 'https://httpbin.org/cookies'
r = s.get(url_cookie)
print(r.text)
'''





from requests import Request, Session
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = req.prepare()

# do something with prepped.body
prepped.body = 'No, I want exactly this as the body.'

# do something with prepped.headers
del prepped.headers['Content-Type']

resp = s.send(prepped,
    stream=stream,
    verify=verify,
    proxies=proxies,
    cert=cert,
    timeout=timeout
)

print(resp.status_code)






