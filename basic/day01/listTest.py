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

"""
元组的差异:
    函数: 
        trule(seq)  将列表转化为元祖
    
        
"""

direct = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

del direct['d']  # 删除单一某一个字典元素
print(direct)
del direct  # 删除整个字典
"""
字典:
    1) 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住
    2) 键必须不可变，所以可以用数字，字符串或元组充当，所以用列表就不行
内置函数:
    cmp(dict1, dict2)   比较两个字典元素
    len(dict)           计算字典元素的个数
    str(dict)           输出字典元素可打印的字符串表示
    type(variable)      返回输入的变来那个类型,如果变量是字典就返回字典类型
内置方法:
    dict.clear()        删除字典内所有元素
    dict.copy()         返回一个字典的浅复制
    dict.fromkeys(seq[, val])       创建一个新字典，以序列 seq 中元素做字典的键，val 为字典所有键对应的初始值
    dict.get(key, default=None)     返回指定键的值，如果值不在字典中返回default值
    dict.has_key(key)   如果键在字典dict里返回true，否则返回false
    dict.items()        以列表返回可遍历的(键, 值) 元组数组
    
    dict.keys()         以列表返回一个字典所有的键
    dict.values()       以列表返回字典中的所有值
    dict.setdefault(key, default=None)      和get()类似, 但如果键不存在于字典中，将会添加键并将值设为default
    dict.update(dict2)  把字典dict2的键/值对更新到dict里
    pop(key[,default])  删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。
    popitem()           随机返回并删除字典中的一对键和值。
    
"""

