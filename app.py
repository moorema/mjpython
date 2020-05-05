# mingling = ""
# started = False
# while   True:
#     mingling = input("> ").lower()
#     if mingling == "start":
#         if started:
#             print("汽车已经发动了!!!")
#         else:
#             started = True
#             print("汽车发动!")
#     elif mingling == "stop":
#         if  not started:
#             print("汽车已经暂停了!!!")
#         else:
#             started = False
#             print("汽车暂停")
#     elif mingling == "help":
#         print("请帮助我,help!")
#     elif mingling == "quit":
#         break
#     else:
#         print("命令输入错误")
#



# jaige = [10,20,30]
# qian = 0
# for zongjg in jaige:
#     qian += zongjg
#
# print(f"总价格是:  {qian}" )




# numbers = [5,2,5,2,2]
# xcishu = 0
# for i in numbers:
#     xcishu = i
#     print(xcishu * "x")



# numbers = [5,2,5,2,2]
# for i in numbers:
#     c = i
#     for a in c:
#         print("x")


#---------------集合排序--------------------------
# numbers = [1,56,78745,35,54654,13325,14351,581451,555,4444444,6,222]
# max = numbers[0]
# for num in numbers:
#     if num > max:
#         max = num
# print(f'最大DE数字是: {m
#---------------集合排序--------------------------


# num = input("Phone: ")
# number = list(map(int,str(num)))
# one = []
# for i in number:
#     if i == 1:
#         one.append("one")
#     elif i == 2:
#         one.append("two")
#     elif i == 3:
#         one.append("three")
#     elif i == 4:
#         one.append("four")
#     elif i == 5:
#         one.append("five")
#     elif i == 6:
#         one.append("six")
#     elif i == 7:
#         one.append("serve")
#     elif i == 8:
#         one.append("ehiter")
#     elif i == 9:
#         one.append("nigne")
#     elif i == 0:
#         one.append("zoer")
# print(one)

#---------------字典--------------------------
# phone = input("Phone= ")
# zidian = {
#     "1":"One",
#     "2":"Two",
#     "3":"Three",
#     "4":"Four"
# }
# jh = ""
# for ch in phone:
#     jh += zidian.get(ch,"!") + " "
# print(jh)
#---------------字典--------------------------

# def digital_to_chinese(digital):
#     str_digital = str(digital)
#     chinese = {'1': '壹', '2': '贰', '3': '叁', '4': '肆', '5': '伍', '6': '陆', '7': '柒', '8': '捌', '9': '玖', '0': '零'}
#     chinese2 = ['拾', '佰', '仟', '万', '厘', '分', '角']
#     jiao = ''
#     bs = str_digital.split('.')
#     yuan = bs[0]
#     if len(bs) > 1:
#         jiao = bs[1]
#     r_yuan = [i for i in reversed(yuan)]
#     count = 0
#     for i in range(len(yuan)):
#         if i == 0:
#             r_yuan[i] += '圆'
#             continue
#         r_yuan[i] += chinese2[count]
#         count += 1
#         if count == 4:
#             count = 0
#             chinese2[3] = '亿'
#
#     s_jiao = [i for i in jiao][:3]  # 去掉小于厘之后的
#
#     j_count = -1
#     for i in range(len(s_jiao)):
#         s_jiao[i] += chinese2[j_count]
#         j_count -= 1
#     last = [i for i in reversed(r_yuan)] + s_jiao
#     last_str = ''.join(last)
#     print(str_digital)
#     print(last_str)
#     for i in range(len(last_str)):
#         digital = last_str[i]
#         if digital in chinese:
#             last_str = last_str.replace(digital, chinese[digital])
#     print(last_str)
#     return last_str
# if __name__ == '__main__':
#     jine = input("输入小写金额: ")
#     digital_to_chinese(jine)
#

# def emoji_converter(message):
#     words = message.split(' ')
#     emojis = {
#         ":)": "😁",
#         ":(": "😂"
#     }
#     output = ""
#     for i in words:
#         output += emojis.get(i, i) + " "
#     return output
#
# message = input(">")
# print(emoji_converter(message))
# #
# try:
#     age = int(input('age= '))
#     print(age)
# except ValueError:
#     print("Invalid value")
#




# class Point():
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")

#
# point1 = Point()
# point1.x = 10
# point1.y = 20
# print(point1.x)
#
# point2 = Point()
# point2.x = 100
# print(point2.x)

# point1 = Point(10,20)
# point1.x = 100
# print(point1.x)
#
#
# class Person:
#     def __init__(self,name):
#         self.name =name
#     def talk(self):
#         print(f"HI, I am {self.name}")
#
# john = Person("John Smith")
# # print(john.name)
# john.talk()
#
# bob = Person("Bob tom")
# bob.talk()


# class Person:
#     def __init__(self,name):
#         self.mingzi = name
#     def talk(self):
#         print(f"HI I am {self.mingzi}")
#
# majie = Person("zhang san")
# majie.talk()
#
# mazhichen = Person("马梓宸")
# mazhichen.talk()


#----------------继承----------------------
# class Dongwu():
#     def walk(self):
#         print("walk")
#     def run(self):
#         print("running")
#
# class Dog(Dongwu):
#     pass
#
#
# class Cat(Dongwu):
#     pass
#
# gou = Dog()
# gou.run()
# gou.walk()
# mao = Cat()
# mao.walk()
# mao.run()
#----------------继承----------------------

# from utils import  find_max
# numbers = [ 109,2,89,7854,54100065,131]
# # print(find_max(numbers))
# maxnum = find_max(numbers)
# print(maxnum)
#--------------包管理调用方法一----------------------
# import ecommerce.shipping
# ecommerce.shipping.calc_shipping()
#--------------包管理调用方法一----------------------
#--------------包管理调用方法二一----------------------
# from ecommerce.shipping import calc_shipping
# calc_shipping()
#--------------包管理调用方法二一----------------------
#
# import random
# # for i in range(3):
# #     print(random.randint(10,20))
# #
# #
# # members = ['john','Mary','Bob','Mosh']
# # leader = random.choice(members)
# # print(leader)
#
#
# class Dice:
#     def roll(self):
#         first = random.randint(1, 6)
#         second = random.randint(1, 6)
#         return first, second
#
#
# dice = Dice()
# print(dice.roll())
#---------------路径模块使用，历遍打印所有文件------------------------
# from pathlib import Path
#
#
# path = Path()
# for file in path.glob('*'):
#     print(file)
#---------------路径模块使用，历遍打印所有文件------------------------

