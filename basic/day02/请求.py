import urllib.request


response = urllib.request.urlopen('http://www.baidu.com')

# print(response.read().decode('utf-8'))

print(type(response))   # <class 'http.client.HTTPResponse'>

print('-----------------------------------')
print(response.getheader('Server'))
print('-----------------------------------')
print(response.getheaders())

