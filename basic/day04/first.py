"""
    关于列表的操作示例
        extend(iterable)    使用可迭代对象中的所有元素来扩展列表
        append(x)           在列表的末尾添加一个元素
        insert(i, x)        在给定的位置插入一个元素
        remove(x)           从列表右侧移除第一个元素 Remove the first item from the list whose value is x. It is an error if there is no such item.
        list.pop([i])       删除列表中给定位置的元素并返回它。如果没有给定位置，a.pop() 将会删除并返回列表中的最后一个元素。
        clear()             移除列表中的所有元素。等价于`` del a[:] ``

        index(x[, start[, end]]) Return zero-based index in the list of the first item whose value is x. Raises a ValueError if there is no such item.
            可选参数 start 和 end 是切片符号，用于将搜索限制为列表的特定子序列。返回的索引是相对于整个序列的开始计算的，而不是 start 参数

        count(x)            返回元素 x 在列表中出现的次数
        copy()              返回列表的一个浅拷贝，等价于 a[:]


"""
exampleList = ["a", "b", "c", "d", "e"]

test = ["1", "2"]

exampleList.extend(test)

print(exampleList)

exampleList.remove("a")

print(exampleList)


