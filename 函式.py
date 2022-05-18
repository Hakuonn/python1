#自訂函式
"""
語法:
def 函式名稱([參數1,參數2],...):
    程式區塊
    [return 回傳值1,回傳值2,...]
"""

#無回傳值
def SayHello():
    print("歡迎光臨")

SayHello()
SayHello()


#有回傳值
def min(a,b):
    if a > b:
        return b
    elif a < b:
        return a

print(min(2,4))
print(min(4,1))

#範例
def Area(width,height):
    area=width*height
    print(area)

print(Area(5,4))

def Area(width,height=12):
    area=width*height
    return area

print(Area(5))

#SyntaxError: non-default argument follows default argument
def Area(width=12,height): #!不能放最後
    area=width*height
    return area

print(Area(5))



#*全域 & 區域變數

def scope():
    var1=1
    print(var1,var2)

var1 =10
var2 =20
scope()
print(var1,var2)


def scope():
    global var1
    var1=1
    var2=2
    print(var1,var2)

var1=10
var2=20
scope()
print(var1,var2)



g=5
def f1():
    print(g)

f1()


g=5
def f1():
    g=10
    print(g)
    #g=10 UnboundLocalError
f1()







#*import 模組
#1.
import random
random.randint(參數)

#2.
from random import *
randint(參數)

#3.
import random as r
r.randint(參數)

import random as r
for i in range(5):
    print(r.randint(0,10),end=" ")


import random as r
for i in range(5):
    print(r.randrange(0,12,2),end=" ")

import random as r
print(r.sample("abbcdefg",5),end=" ")


import guess
computer=guess.figure_guess()
print(computer)

import guess as gs
computer=gs.figure_guess()
print(computer)

import sys
for path in sys.path:
    print(path)


#檔案處理

content="""Hello
高科大
IC
"""

f=open("file2.txt",'w',encoding='utf-8')
f.write(content)
f.close()


f=open("file2.txt",'r',encoding='utf-8')
for i in f:
    print(i,end="")
f.close()

f=open("file2.txt",'a',encoding='utf-8')
f.write(content)
f.close()

with open('file2.txt','r',encoding='utf-8') as f:
    content=f.readlines()
    print(content)


import exlotto
exlotto.lotto()