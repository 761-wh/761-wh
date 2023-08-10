"""
列表的操作方法：
    insert方法——向列表中插入元素。参数1：插入的位置；参数2：插入的内容

    clear() 用于将列表清空

"""
list_1 = [1,2,3,4,5]
list_1.insert(2,'aaa')
print(list_1)   #[1, 2, 'aaa', 3, 4, 5]

list_1.insert(5,[10,20,30])
print(list_1)   #[1, 2, 'aaa', 3, 4, [10, 20, 30], 5]


#clear()  清空列表
list_1.clear()
print(list_1)    #[]