print("声明utf-8编码格式,utf-8格式是默认的,可忽略")

# python单行注释

# ** 计算乘方


# 切片操作:
#     切片中的越界索引将被自动处理
char = "stringTest"

print(char[0: 6])

print("stringTest length: ", len(char))

print("返回消除大小写的字符串副本:", char.casefold())

print(char.center(14, '-'))

print("子字符串在start和end之间非重叠出现的次数: ", char.count('t'))

print("返回原字符串编码为字节串对象的版本。 默认编码为 'utf-8': ", char.encode(encoding="utf-8"))

print("字符串格式化操作: {}".format(char))






