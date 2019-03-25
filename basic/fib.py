def fib(n):
    # 局部变量
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()


fib(10)

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, ":", v, end=' ')

print()

if __name__ == "__main__":
    import sys
    # 这样提供了一个便于测试模块的接口 666
    print("作为__main__被执行")
    print(sys.path)
    print()

    import math

    print(dir(math))

    with open('test.txt', 'r', encoding='utf-8') as f:
        print(f.tell())
        print(f.readline())
        print(f.tell())


