#-*-coding:utf8-*-

a = [1,2,3]
b = [4,5,6]
print(len(a))#函数计算元组元素个数
a[2:] = b#a的第2个值赋值为b中的元素
print("a的第二个值等于列表b中的元素:",a)

# a = [1,2,2,1,1]
# print(a.index(2))

# a = [1,2,3,4,5]
# a.insert(0,0)
# a.insert(len(a), 6)
# print (a)

# a = [1,2,1,2]
# print(a.pop())
#
# a.pop(0)
# print(a)
# a = [1,2,1,2]
# a.remove(1)
# print(a)
#
# a = [9,2,5,1,8,3,4,6,7]
# a.sort()
# print(a)


# format = "Hello, %a, %a, enough for ya?"
# values = ("world", "hot")
# print (format % values)

# a = [0,1,2,3,4,5,6,7,8,9]
# for i in a:
#     print(i)
#     i += 1
# print(a)
#
#
# b = ["abc", "bcd", "cde"]
# for j in b:
#     print(j)
#     if len(j) > 6:
#         b.insert(0,b)

# i = 5
# i = 6
# f()
# def f(arg=i):
#     print(arg)

# def f(a,L=[]):
#     L.append(a)
#     pr0
#
# print(f(a=1))
# print(f(a=1))
# print(f(a=1))

# print('123的十六进制是: %r' % 123)

# print('%-10f' % 3.1415926582563)
# print('%-10.2f' % 3.1415926)

# a = "zhangchizuiniubi"
# print(a.find("zui"))
# print(a[9:])

# a = "1" "2" "3" "4" "5" "6"
# b = "+"
# print(b.join(a))

# a = "ZHangChi"
# print(a.lower())

# a = "1+2+3+4+5+6"
# print(a.split("+"))

# x = {41:"abc"}
# x[42] = "foobar"
# print (x)
# del x[41]
# print (x)
# print(41 in x)
# print(42 in x)

# people = {
#     "zhangchi":{"phone":12345678, "gender":"M"},
#     "fengxu":{"phone":22345678, "gender":"M"}
# }
#
# a = input("请输入要查询人的姓名：")
# print(a in people)
# if a in people:
#     print(a + " in people dict")
#     b = input("是否需要查询电话号码")
#     if b == "y" or b == "Y":
#         print (people[a])
#     elif b == "n" or b == "N":
#         print ("感谢您使用！")
#     else:
#         print ("请输入Y或N查询")
# else:
#     print ("未找到您输入的人员")

# phonebook = {
#     "zhangchi":"123",
#     "chenfei":"456",
#     "wangtao":"789"
# }
# print ("zhangchi's phonenum is %(zhangchi)s ." % phonebook)

# d = {}
# z = d
# d['name'] = 'Jack'
# d['age'] = 24
# print (d)
# print (z)
# d.clear()
# print (d)
# print (z)

# from copy import deepcopy
# d = {}
# d['name'] = ['jack']
# c = d.copy()
# dc = deepcopy(d)
# d['name'].append(['Clive'])
# print(c)
# print(dc)
# print(d)

# d = {'name1' : 'zhangchi',
#      'name2' : 'wangtao',
#      'name3' : 'zhaochen'
#      }
# print(d.get('name'))

# labels = {'phone' : 'phoneNumber',
#           'adr' : 'address'
#      }
# name = input("name:")
# request = input('phone number or address?')
# key = request
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'
# person = people.get(name, {})
# label = labels.get(key, key)
# result = person.get(key, 'not available')
# print ("%s's %s is %s") % (name,label,result)

# print (1,2,3)
# print ("Age",42)

# a = 1, 2, 3
# print(a)
# x, y, z = a
# print (a)

# name = 'zhangchi'
# if name.endswith('zhangchi'):
#     print ('hello', name)
# else:
#     print (name, 'is not found')

# x = y = [1,2,3]
# z = [1,2,3]
# print (z is y)
# print (z == y)

# if not condition:
#     crash program

# assert 2-2==2*2, "fail"

# names = ['zhangchi', 'anne', 'beth']
# ages = [12, 45, 32]
# for i in range(len(names)):
#     print(names[i], 'is', ages[i], 'years old')

# #替换x字符
# strings = ['index', 'string', 'xc']
# for string in strings:
#     if 'x' in string:
#         index = strings.index(string)
#         strings[index] = '[secsored]'
#         print (string)
# print (strings)

# print (sorted([4,9,3,6,8,2,0,3,-1]))
# print (sorted('qwertyuiopasdfghjklzxcvbnm'))
# print (list(reversed('adsfghjkl')))

# word = ""
# while 0:
#     word = input('please enter a word:')
#     print ('The name is', word)

# j = []
# for i in range(10):
#     if i % 3 == 0:
#         j.append(i ** 2)
# print (j)
# print ([x*x for x in range(10) if x % 3 == 0])

# print(eval('2*3'))

# print (fibs(10))

# import turtle
# t = turtle.Pen()
# for x in range(100):
#     t.forward(x)
#     t.right(90)
#
# def fibs(num):
#     result = [0,1]
#     for i in range(num-2):
#         result.append(result[-2] + resule[-1])
#         return result
# fibs(20)

# x = 1
# a = vars()
# print(a['x'])

# def foo():x = 42
# x = 1
# print(x)

# def add(x,y):
#     x = x ** 0.5
#     y = y ** 0.5
#     z = x + y
#     return(x,"+",y,"=",z)
# print(add(4,16))
# #函数调用
# import math
# def add1(x,y,f):
#     return f(x) + f(y)
# print(add1(4,16,math.sqrt))

# a = 0
# for i in range(10):
#     print ("--" * 10, i)
#     if (i % 2) == 1:
#         i += i
#         print (i)
# print("=" * 10, i)

