"""
1、python关键词
import keyword
print(keyword.kwlist)

2、python 缩进
    tab 键

3、多行语句（斜杠换行）  \
a = 1
b = 2
c = 3
e = a + \
    b + \
    c
print(e)

4、python的引号
   ''
   ""
   """  """
5、python的注释
#注释

6、python的空格 和 空行 ————》美化作用
a = b + c

7、python输出函数与输入函数
   输出函数：print()
   输入函数：input()
   
a = input("请输入内容：")
print(a)

8、python的转义符：
     转义符，即 \ ＋特异功能的首字母
     \n   换行
     \t   制表符 代表的是4个空格
     \r   覆盖
     \b   删除
     \\   两个反斜杠表示一个\
     原字符   使转义字符不起作用，写在前面，用r或R
     
print("这里的引号\" \"要输出显示出来")
print("此处要\n换行")
print("aaa\tbbb")
print("左边\r覆盖左边")
print("会被删掉一个字字\b哪一个")
print("打印出一个反斜杠\\")
"""


"""
9、变量
    变量名的第一个字符不能是数字
    变量名区分大小写
    特殊关键字不能命名为变量名

#给变量赋值
a = 100
b = 200
c = 300
#给多个变量同时赋值
a,b,c = 100,200,300
#常量
BI = 3.141592653
"""