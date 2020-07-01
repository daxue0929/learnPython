squares = [1, 4, 9, 16, 25]

print("当前列表是: ", squares)

# 注意:
#   所有的切片操作都返回一个新列表, 这个新列表包含所需要的元素。就是说，如下的切片会返回列表的一个新的(浅)拷贝:
print('类似字符串列表也支持切片操作,返回一个子列表: ', squares[0: 2])

squares.append(36)
print("在列表末尾添加新元素: ", squares)


# i = int(input("请输入一个正整数:"))
i = squares[0]

if i < 10:
    print("这是一个一位数: ", i)
elif i == 10:
    print("这是一个最小的两位数")
else:
    print("这不是一个一位数: ", i)

for s in squares:
    print(s)

print("--------------------------分割线--------------------------")

# range(start, end, step) 开始 结束 步进
# range() 所返回的对象在许多方面表现得像一个列表，但实际上却并不是。此对象会在你迭代它时基于所希望的序列返回连续的项，但它没有真正生成列表，这样就能节省空间
for i in range(0, 20, 5):
    print(i)


def initlog(*args):
    pass    # Remember to implement this!


# 关键字 def 引入一个函数 定义。它必须后跟函数名称和带括号的形式参数列表。构成函数体的语句从下一行开始，并且必须缩进。
# 函数体的第一个语句可以（可选的）是字符串文字；这个字符串文字是函数的文档字符串或 docstring
# 即使没有 return 语句的函数也会返回一个值，尽管它是一个相当无聊的值。这个值称为 None （它是内置名称）。一般来说解释器不会打印出单独的返回值 None

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 1, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


fib(100)

print("--------------------------分割线--------------------------")

# in 关键字。它可以测试一个序列是否包含某个值


def f(a, value=None):
    """第二次调用不共享默认值写法"""
    if value is None:
        value = []
    value.append(a)
    return value



