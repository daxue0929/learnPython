print("你好，世界")


# 默认情况下python被视为UTF-8编码

if 3 < 10:
    print("判断正确")


# for item in [1,3,4,5,6]:
#     print(item)

# for i in range(8):
#     print(i, end=' ')

# print(range(10))  #这是一个对象，并不是一个列表，可迭代

# try:
#     pass
# except ValueError:
#     pass
# except OSError:
#     pass
# finally:
#     pass

def fun(arguments):
    pass

class ClassName:
    pass

class FirstClass:

    className = '这是一个类变量' #实例之间共享的变量

    # 类初始化函数
    def __init__(self):
        self.name = '王雪迪'
        self.age = '23'

c = FirstClass()

print(c.name + " " + c.age)


