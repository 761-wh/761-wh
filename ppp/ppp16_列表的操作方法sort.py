"""
列表的操作方法
    sort()
        用于将列表进行排序，同类型的数据才能一起排序
        默认是升序排列
        ASCII码，常见的大小规则：0~9<A~Z<a~z

"""
list_1 = ['he','llo','wh','hh','aa','我','cc','zz','kk','1',"88"]
list_1.sort()   #['1', '88', 'aa', 'cc', 'he', 'hh', 'kk', 'llo', 'wh', 'zz', '我']
print(list_1)

list_2 = [3,2,5,4,7,6,8,2,3,1]
list_2.sort()   #[1, 2, 2, 3, 3, 4, 5, 6, 7, 8]
print(list_2)

#降序排列
list_3 = [3,2,5,4,7,6,8,2,3,1]
list_3.sort(reverse=True)  #[8, 7, 6, 5, 4, 3, 3, 2, 2, 1]
print(list_3)
