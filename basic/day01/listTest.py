list = ['a', 'b', 'c', 'd', 'e', 'f', 'h']

"""
列表包含下列函数:
    cmp(list1, list2)   比较两个列表的元素
    len(list)           列表元素的个数
    max(list)           返回列表元素的最大值
    min(list)
    list(seq)           将元组转化为列表
列表包含下列方法:
    list.append(obj)    在列表末尾添加新的对象
    list.count(obj)     统计某个元素在列表中出现的个数
    
    list.extend(seq)    在列表末尾一次性追加另一个序列的多个值(用新列表扩展原来的列表)
    list.index(obj)     从列表中找出某个值第一个匹配项的索引位置
    list.insert(index, obj) 将对象插入列表
    list.pop([index=-1])    移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
    list.remove(obj)    移除列表中某个值的第一个匹配项
    list.reverse()         反向列表中元素
    list.sort(cmp=None, key=None, reverse=False)       对原列表进行排序  
    
"""

print(list.pop(-2))
print(list)

list.remove('a')

print(list)
