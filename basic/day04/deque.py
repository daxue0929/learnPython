from collections import deque

"""
    若要实现一个队列，可使用 collections.deque，它被设计成可以快速地从两端添加或弹出元素
"""

queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
print(queue.popleft())
print(queue.pop())




