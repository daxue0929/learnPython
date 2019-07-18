import os
import urllib.request
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')

response = urllib.request.urlopen('http://www.baidu.com')

# window 则用'nt'表示，对于Linux/Unix用户，它是'posix'
print(os.name)

# 得到当前工作工作目录
print(os.getcwd())

# 指定目录下的所有文件和目录名
print(os.listdir('C:'))

os.system("type nul>layout.scss")
os.system("type nul>a")

try:
    f = open('a.txt', 'w')
    str = response.read().decode('utf-8')
    f.write(str)
finally:
    if f:
        f.close()


