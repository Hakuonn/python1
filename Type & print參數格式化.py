# 註解 變數宣告

from typing import Type


a = 0
b = 1  # 整數變數的宣告
A = 3
x = y = z = 20
age, name = 2, "NKUSTIC"
Age, name = 19, 'Nkust_ic'

print(a, b)
print(x, y, z)
print(age, name)
print(Age, age)

# 資料型別 type
Num1 = 3  # 整數
Num2 = 4.5  # 浮點數
Num3 = True  # 布林 #布林值字母要大寫
Num4 = False  # 布林
str1 = "Nkust"  # 字串

print(type(a))
print(type(Num1))
print(type(Num2))
print(type(Num3))
print(type(Num4))
print(type(str1))
Num5 = 34 + True
print(Num5)
Num6 = 34 + False
print(Num6)

str2 = """
Alex
Ronney
Peko"""  # !長字串
print(str2)

name1 = "Alex's iphone"
print(name1)

name2 = 'Alex\'s iphone'
print(name2)

# 資料型別強制轉換
numtype1 = 23 + int("76")
print(numtype1)

帥哥 = 7
print(帥哥)

# 輸出
print("高科大")
print(100, "NKUST", 70)
print(str(100)+"NKUST"+str(70))
print(100, "NKUST", 70, sep="@", end="#")
print(200, "KMU", 80, sep="@")
print(100, "NKUST", 70, sep="\n", end="@")  # ! /n表示換行 /t表示按下tab鍵
print(200, "KMU", 80, sep="@")

# print 參數格式化
print("%s的成績是%d分" % ("班代", 90))  # ! %S字串 ； %d整數
print("%5s的成績是%3d分" % ("班代", 90))
print("%-5s的成績是%-4d分" % ("班代", 90))  # !負號靠左邊

print("我的BMI%f" % (18))  # ! %f浮點數
print("我的BMI%.2f" % (18))  # !代表取2位小數，四捨五入
print("我的BMI%6.2f" % (18))  # !代表有6位數字(3位整數,1位小數點,2位小數)

# print 參數格式化 [format]
print("{}成績是{}".format("班代", 90))  # !{}參數位址
print("{1}成績是{0}".format("班代", 90))  # !{索引}所以的數值從0開始
print("{0:5s}成績是{1:.2f}".format("班代", 90.765))  # !{索引值：格式化指定}
print("{}成績是{} {}".format("班代", 90, 70))

# (f)
name3 = "班代"
score = 90
print(f"{name3}的成績是{score}")

# HW
print("%-5s%2s%3s%3s%3s" % ("姓名", "座號", "國文", "數學", "英文"))
print("%-5s%2s%6s%5s%5s" % ("林大明", "1", "100", "87", "79"))
print("%-5s%2s%6s%5s%5s" % ("陳阿中", "2", "74", "88", "100"))
print("%-5s%2s%6s%5s%5s" % ("張小英", "11", "82", "65", "8"))

print("%-3s%5s%5s%5s" % ("年度", "所得稅", "營業稅", "證交稅"))
print("%-7s%6.2f%8.2f%8.2f" % (2017, 98.32, 90.20, 104.79))
print("%-7s%6.2f%8.2f%8.2f" % (2016, 83.00, 110.50, 182.45))
print("%-7s%6.2f%8.2f%8.2f" % (2015, 98.00, 79.32, 102.00))
