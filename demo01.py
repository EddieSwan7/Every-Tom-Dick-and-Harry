"""
print("hello world!") # 字符串
print(2333) # 整数
print(2.333) # 小数
print(True) # 布尔值 Trur or False
print(())  # 元组
print([])   # 数组
print({})   # 字典
锄禾日当午
汗滴禾下土
print("哈哈",2333)
print("哈哈"+"嘻嘻") #字符串的拼接
print("哈哈"*100)
print(((1+2)*100-9.9)/2) 
print(2<3)

# 变量 
#赋值
name = "张三" #把张三的这个值赋值给了名字叫a的这个变量
print(name)
"""
"""
a = input("请输入:")
b = input("请输入:")
print("input获取的内容: ",a+b)
"""
#数据格式的转换
# print(type("哈哈"))
# print(type(2333))
# print(type(2.333))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))

# a = str(2333)
# print(type(a))

# a = int("哈哈")
# print(type(a))

# a = float(input("请输入:"))
# b = float(input("请输入:"))
# print("input获取的内容: ",a+b)


# a = 'dsfsdfdsfsdgdfhfgjhfgdjjerhuwrhywhwghfdgsdhdfh   rfdgdfh'

# print(len(a))



"""
练习:通过代码获取两段内容，并且计算它们的长度的和。

"""

# a = input("请输入:")
# b = input("请输入:")
# # print("input获取的内容: ",a+b)
# # print(len(a+b))


# # a = input("请输入:")
# # b = input("请输入:")
# # print("两段字符串的长度:",len(a+b）)

# #元组,下标 从0开始编号
# a = (1,2,3,4,"哈哈","嘻嘻","哈哈","哈哈",True,False) 
# # 切片 批量取值
# # print(a[-5])
# # print(a[:4])  #左闭右开
# # print(a[4:8])
# # print(a[8:])
# # print(a[0:12])


# # print(a.index("嘻嘻"))
# # print(a.count("哈哈"))

# #二维元组
# # b = (a,"哈哈","嘻嘻")
# # print(b[1])
# # print(b[0][7])

# a = [1,2,3,4,"哈哈","嘻嘻","哈哈","哈哈",True,False]
# a.append("吴海华")
# print(a)



# print(a[4])
# #元组一定写好过后不可以修改，而数组是可以的修改的

# a.insert(7,"吴海华")
# print(a)
# b = a.pop(0)     #剪切
# c = a.pop(0)
# print(b+c)
# print(a)

# # a.clear()
# print(a)
# xx = ["AVA","WES"]
# # a.extend(xx)
# print(a+xx)

# b = a.remove(1)
# print(b)
# print(a)

# xx = [0,1,1,0,True,False]
# a = xx.count(0)
# print(a)

# #下标不要超出范围 = 越界
# xx = [a,0,1,2,3]
# xx[9]
"""
python的语法
所有的方法都是小括号结尾。比如，print（），input（），len（）
元组，数组，字段的取值都是用中括号，比如a[0]
元组，数组，字典的定义，分别是（），[],{}
"""


"""
字典的特点：
1.字典中的值没有顺序
2.字典的结构必须是键值对的结构。 key：value
3.子典的取值是通过Key去取value
"""
# a = {"z":"龙珠","name":"张三",0:"哈哈","age":25}
# 取值
# print(a["age"])
# # 新增
# a['high'] = "183cm"
# print(a)
# # 修改
# a['name'] = '李四'
# print(a)
 
# b = a.get("name")
# print(b)
# b = a.pop("name")
# print(b)
# a.update(name=1111)
# print(a)

# print("------------------")

# print(a.get("name11"))
# # print(a["name11"])

# #数组和字典的删除
# del a["name"]
# print(a)
# del a[0]
# print(a)

"""
练习：
获取用户输入的个人信息，并且存储到字典中。
个人信息包括了：name，age，sex
"""

a = {"姓名":"xxx","性别":"x","年龄":"xx","身高":"xx","体重":"xx"}
b = input("请输入姓名:")
c = input("请输入性别:")
d = input("请输入年龄:")
e = input("请输入身高:")
f = input("请输入体重:")
a.update(姓名=b)
a.update(性别=c)
a.update(年龄=d)
a.update(身高=e)
a.update(体重=f)
print(a)

















