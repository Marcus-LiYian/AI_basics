# 作者:李一安
# 2026年02月10日19时56分01秒

'''
1、字符串同元组一样，只读。
2、字符串无法自我嵌套，也就是字符串容器中的每个对象都必须是单个字符，因此字符串仅能使用一维[]来访问字符。
3、
'''


# 字符串对象内部方法
# 目标字符的下标=字符串.index(目标字符)
str1 = "abcdefg"
result = str1.index("e")
print(result)


# 容纳分割后的子字符串的列表=字符串.split(用于分割的字符)
str2 = "abc@def@ghi"
list2 = str2.split("@")
print(list2)


# 替换后字符串=替换前字符串.replace("目标字符串片段","替换用字符串片段")
# replace方法：将字符串中的某个字符串片段全部替换成目标字符串，这个字符串片段可以是单个字符
str3 = "wwwwwwwaaaaaa"
str4 = str3.replace("w","W")
print(str4)


# count方法：统计指定字符在字符串中出现的次数。
# num = 字符串.count(目标字符)
str5 = "aaaaaaaa"
num = str5.count("a")
print(num)