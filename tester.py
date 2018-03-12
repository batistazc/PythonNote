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

#