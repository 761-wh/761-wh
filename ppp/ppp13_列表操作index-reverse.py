"""
列表操作方法：
    index()
         返回所匹配的元素的索引。参数1：待查找的对象；参数2：查找的起始范围；参数3：查找的结束范围

    reverse()
         用于将列表反向排列

"""
list_1 = ['apple','china',1,2,'china',3,'python']
r = list_1.index('apple')
print(r)  #0

r2 = list_1.index('china',2,5)
print(r2)  #4

#反向
list_1.reverse()
print(list_1)  #['python', 3, 'china', 2, 1, 'china', 'apple']