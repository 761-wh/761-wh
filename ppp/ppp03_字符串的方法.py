"""
字符串 string
"""
s = 'zhongwen'
ss = "中文123abc"
sss = """
abc
123
中文
"""

"""
字符串索引 下标  --->由 0 开始，可以是负数

sa = "中文123abc"
print(sa[0])  #中
print(sa[1])  #文
print(sa[-1]) #c
print(sa[-2]) #b
"""

"""
字符串切片
切片[开始:结尾] 取左不取右
切片[开始:结尾:步长] 取左不取右

a = 'abcdefgh'
print(a[0:3])
print(a[:3])  #0 可以缺省
print(a[-3:-1])
print(a[0:8:2])  #aceg
print(a[::-1])  #反转整个字符串 hgfedcba
"""

"""
字符串的拼接 + 

a = '100' + "50"
print(a)   #10050

b = "制作不易"
c = "一键三连"
d = "感谢支持"
f = ','.join((b,c,d))
print(f)

"""

"""
 字符串的格式化 {}
 format()

s1 = "今天是{}年{}月{}日，星期{}"
s2 = s1.format("2023","8","7","一")
print(s2)
"""

"""
字符串的常用方法
find()  查找返回元素的位置,找不到返回-1
count()  统计指定的内容在字符串中出现的次数，找不到返回0
replace()  指定替换内容。参数1：要替换的内容；参数2：替换后的内容；参数3：替换的次数，从前往后替换（默认替换所有）
upper() 将小写转换成大写
lower() 将大写转换成小写
split()  指定分割点对字符串进行分割，得到一个列表。参数1：分割点；参数2：分割的次数（默认找到所有的分割点进行分割）
strip()  去掉字符串首尾的空格
"""
s1 = "ApythonAbcdeAfg"
print(s1.find("o"))   #4
print(s1.find("A",8,13))  #11
print(s1.count("A"))  #3
res = s1.replace("A","BB",2)
print(res)
res2 = s1.upper()
print(res2)   #APYTHONABCDEAFG
res3 = s1.lower()
print(res3)  #apythonabcdeafg

#split()  指定分割点对字符串进行分割，得到一个列表。参数1：分割点；参数2：分割的次数（默认找到所有的分割点进行分割）
s2 = "111ab222ab333ab444"
#将字符串s2用字符a 进行分割，得到一个列表
print(s2.split("a"))
print(s2.split("a",2))

#strip()  去掉字符串首尾的空格
s3 = "     abcdfergg       "
print(s3.strip())  #abcdfergg
s4 = "666abcdfergfd666"
print(s4.strip("6"))   #abcdfergfd
s5 = "python:666   ppp:777"
print(s5.replace(" ",''))  #python:666ppp:777   将中间的空格去掉，采用替换的方式

