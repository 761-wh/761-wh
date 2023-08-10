"""
列表操作方法
    copy()
        用于创建列表的副本
"""

a = ['hello','关注','python',1,2,3,4]
b = a.copy()
del a[0]
print(a)  #['关注', 'python', 1, 2, 3, 4]
print(b)  #['hello', '关注', 'python', 1, 2, 3, 4]