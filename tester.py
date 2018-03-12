#-*-coding:utf8-*-
#第五章 条件、循环和其他语句

# # 使用逗号输出,逗号当连接符用
# print("age:", 42)

# # 文本和变量同时输出，又不希望格式化字符串时可以使用此方法
# name = "zhangchi"
# salutation = "Mr."
# greeting = "Hello"
# print(greeting, salutation, name)

# # 在结尾加上逗号，会和下一个print输出到同一行(只在脚本中起作用）
# print("Hello,"),
# print("World!")

# # 把某件事作为另一件事导入，方法
# import somemodule
# from somemodule import somefunction
# from somemodule import somefunction, anotherfunction#如果两个模块中都用同名时需要使用第一种方法导入
# from somemodule import *

# # 导入的方法可以用as进行重命名
# import math as foobar#把math命名为foobar
# print(foobar.sqrt(4))
# from math import sqrt as foobar
# print(foobar(64))

# # 多个赋值操作同时进行
# x, y, z = 1, 2, 3
# print(x, y, z)
# # 交换两个变量
# x, y = y, x
# print(x,y)

# #序列解包
# values = 1, 2, 3
# print(values)
# x, y, z = values
# print(x)

# #随机删除并返回字典中
# scoundrel = {
#     "name" : "Robin",
#     "girlfriend" : "Marion",
#     "key" : "value"
# }
# key, value = scoundrel.popitem()
# print(key)
# print(value)
# print(scoundrel)

# #python 3中新特性：ab复制
# *c, a, b = 1, 2, 3, 4, 5
# print(c)
# a, b, *c = 1, 2, 3, 4, 5
# print(c)

# #链式赋值
# x = y = 1
# print(x, y)

# #增量赋值
# x = 2
# x = x + 1
# print(x)
# x *= 2
# print(x)
# fnord = "foo"
# fnord += "bar"
# fnord *= 2
# print(fnord)

#######################下面插入本地电脑中的内容

#布尔运算符
# number = int(input("Enter a number between 1 and 10"))
# if number <= 10:
#     if number >=1:
#         print("Great!")
#     else:
#         print("Wrong!")
# else:
#     print("Wrong!")
# #方法二
# if 1 <= number <= 10:
#     print("0-1")
# else:
#     print("error")

# #简单if语句书写方式
# b = int(input("输入数字"))
# a if b < 10 else c#如果b<10则返回a，否则返回c

# #断言 在调试过程中使用较多 可以用于判断条件是否为真
# age = 10
# assert 0 < age < 100
# age = 101
# assert 0 < age < 100, 'The age must be realistic'#条件后可以增加字符串，用于解释断言

# #while循环 当条件为真的情况时重复执行一段代码 可以使用
# #打印1-100的数字
# x = 1
# while x <= 100:
#     print(x)
#     x += 1

# #判断name中填写数据，否则返回重新填写
# name = ""
# # while not name or name.isspace():#isspace() 方法检测字符串是否只由空白字符组成。
# while not name.strip():#strip函数用于移除字符串首尾指定字符，默认为空格
#     name = str(input("Please enter your name"))
# print("Hello, %s!" % name)

# #for循环 要为一个集合的每个元素都执行相同代码时使用
# numbers = range(10)
# for number in numbers:
#     print(number)

