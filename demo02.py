#判断 代码块 缩进代表


# if a == 1:
#     print("哈哈哈哈")


# if a > b:
#     print("a比b大") #前面四个空格
# else:
#     print("b更大")


# age = int(input("请输入你的年龄:"))
# if age > 60:
#     print("你应该退休了")
# elif age > 30:
#     print("家庭的责任很重")
# elif age > 20:
#     print("一定要好好规划你的未来！")
# else:
#     print("读书的时候，要认真！")

"""
if 30 >= age > 20:
    print("222222")
elif age > 30:
    print("333333")
elif age > 60:
    print("6666666")
else:
    print("xxxxxx")
"""
# == 判断是否相等
# = 赋值


# a = "你好"
# if a in ["你好", "不好"]:
#     print("OK")
# else:    
#     print("不OK")

# a = input("请输入：")
# if a == "":
#     print("不能为空！")
#     exit()    
# if a in "012345678":
#     a = int(a)
# else:
#     print("请输入正确的年龄:!")
#     exit()

# if a > 5:
#     print("大")
# else:
#     print("小")    

# a = 123456789
# if type(a) is int:
#     print("是数字！")
# elif type(a) is str:
#     print("是字符串")
# else:    
#     print("其他")

# if

# if else

# if elif else

# a = 1
# while a < 10:
#     print("哈哈哈哈")  死循环

# a = 1
# while a < 10:
#     print("哈哈哈哈",a)
#     a = a + 2

"""
练习：
现在有十个学生的成绩，需要录入到系统中。
这是个人分别是，刘一，陈二，张三，李四，王五，周六，吴七，郑八，朱九，亚索
并且名字和成绩需要对应上。
而且大于60的和小于60的需要分开存放
"""

# failingscoreslist = {} #定义了一个空字典，可以用来往里面存储小于60分的信息
# passingscoreslist = {} #定义了一个空字典，可以用来往里面存储大于等于60分的信息
# studentlist = ["刘一","陈二","张三","李四","王五","周六","吴七","郑八","朱九","亚索"] 
# a = 0 #定义了一个变量，用来控制数组的下标的变化，利于我们从学生表中挨个抽出我们要的学生姓名，方便接下来录入学生成绩
# while a < len(studentlist): #因为所有的人的信息的录入，都是要用input,所以需要循环语句，利用len判断了数组的长度可以挨个录入学生的成绩，总长度减1就是最大下标
#     scores = int(input("请输入"+studentlist[a]+"成绩:")) #录入信息，为了方便判断，所以转换了格式为数值，并且数值为动态变化，需要定义为scores方便下面的判断语句 if else
#     if scores < 60:     #判断分数                             #数值的动态变化通过input（"请输入+"张三"+的信息"）→ input("请输入"+"studentlist[a]+"的成绩:")
#         failingscoreslist[studentlist[a]] = scores #小于60分的信息全部通过上面的循环+判断语句筛选出来，通过字典的新增就完成了成绩不及格学生表的依次录入
#     else:
#         passingscoreslist[studentlist[a]] = scores 同上
#     a = a+1  #控制下标变化，每一次循环，都+1
# print("成绩不及格学生表:",failingscoreslist)
# print("成绩及格学生表:",passingscoreslist)


#遍历
# a = "你好，今天你吃了吗？"
a = ["刘一","陈二","张三","李四","王五","周六","吴七","郑八","朱九","亚索"]
for i in a:
    print(i)


b = list(range(0,100,10)) #自动生成了一个数列,步进/步长
print(b)

# for i in range(100):
#     print(i)

for i in range(10):
    print(i)















