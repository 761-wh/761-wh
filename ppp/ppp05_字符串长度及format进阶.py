
# len()  字符串长度
s = "EOL while scanning string literal"
print(len(s))   # 空格也算长度

# 格式化小数长度（会四舍五入） :.2f
s1 = 3.1415926
print("{:.2f}".format(s1))

# 将小数按百分比的形式显示   :.2%
s3 = 0.23563
print("百分比为{:.2%}".format(s3))  #百分比为23.56%
print("百分比为{:.3%}".format(s3))  #百分比为23.563%
print("百分比为{:.3%}".format(0.23563))  #百分比为23.563%