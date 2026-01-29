# 作者:李一安
# 2026年01月09日13时14分24秒


# 空列表
list1 = []
list2 = list()#用类来建立对象实例

print(list1)
print(list2)
print(type(list1),type(list2))

print("-"*50)

# 可容纳任何数据类型
list3 = [1,"2",3.14,[4,"5",6.12]]
print(list3)
print(list3[3][0])

print("-"*50)


# 增
# 列表对象的内部自带方法.append(对象)，于末位增加数据
list4=[]
print(list4)
list4.append("append_object")
print(list4)

print("-"*50)

# 列表对象的内部自带方法.insert(下标,对象)，于下标处插入数据
list5 = [0,1,2]
print(list5)
list5.insert(1,"insert_object")
print(list5)

print("-"*50)

# 列表对象的内部自带方法.extend(可迭代对象)，将可迭代对象中的内容依次取出，追加到列表尾部，如果是字符串，则会逐个字符追加。
list6 = [0,1,2]
print(list6)
list6.extend(list5)
print(list6)

print("-"*50)


# 删
# 按下标删
# 列表对象的内部自带方法.pop(下标)，删除指定下标的数据，并将被删除的数据作为此方法的返回值
list7=[0,1,2,3,4,"pop_object"]
print(list7)
ret = list7.pop(5)
print(list7)
print(ret)

print("-"*50)

# 按值删
# 列表对象的内部自带方法.remove(object)，删除容器中目标对象的第一次出现
list8 = [0,1,2,3,4,5,1]
print(list8)
list8.remove(1)
print(list8)

print("-"*50)

# 清空
# 列表对象的内部自带方法.clear()，清空容器内容
list9 = [0,1,2,3,4,5,6,7,8]
print(list9)
list9.clear()
print(list9)

print("-"*50)

# 可清空，可按下标删
# 本地函数del，可用于删除任意容器中指定下标对应的数据，但不会返回被删除的数据，也可用于删除整个容器
list10 = [0,1]
print(list10)
del list10[0]
print(list10)

del list10
# print(list10)# 输出空白

print("-"*50)

# 列表对象的内部自带方法.index(object)，获取目标对象第一次出现时的下标
list11 = [5,4,3,2,1,5]
print(list11)
index=list11.index(5)
print(index)

print("-"*50)

# 列表对象的内部自带方法.count(object)，统计目标对象出现次数并返回
list12=[0,1,2,3,4,5,5,5,[5,5,5]]
print(list12)
count=list12.count(5)
print(count)

print("-"*50)

# 列表对象的内部自带方法.reverse()，反转列表内容，不会排序，会改变原列表，不会返回新列表。
list13=[0,1,2,3,4,5,6,7,[5,4,3,2,1]]
print(list13)

list13.reverse()
print(list13)

print("-"*50)

# 列表对象的内部自带方法.sort(reverse=False)，默认从小到大排列列表内容，会改变原列表，不会返回新列表。
# 当修改默认值为True时，从大到小排列列表内容
# 硬性使用要求是容器中的数据类型都一样，若为字符串则比较Unicode编码
# sort不会深入到里层结构，即嵌套容器不会被排序，不只是此方法，列表所有的方法都不会深入到里层结构
list14=[9,5,2,1,6,4,3,7,8]
print(list14)

list14.sort()
print(list14)

list14.sort(reverse=True)
print(list14)


# 查和改使用下标访问实现。