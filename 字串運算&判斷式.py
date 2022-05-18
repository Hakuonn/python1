
##範例
deposit = int(input("請輸入本金存款金額："))
times = 1.02**6
deposit *= times
print("6年後的存款為："+str(deposit))

##字串運算
s = "0123456789"
print(s*2)  ##複製字串
print(s[0])  ##取出字串
print(s[-1])  ##s[9]
print(s[-2])
##print(s[1:5]) #切割取出字串[開始:結束:間格]
print(s[1:5])  ##不包含終止值的索引值
print(s[:])
print(s[2:])
print(s[:2])

print(s[:-2])
print(s[-4:-2])
print(s[5:-2])

print(s[2:10:2])  ##print(s[開始值:終止值:間格])
print(s[::-1])
print(s[-1::-1])

##綜合運算
x1 = "3"
y1 = 3
a = x1*y1
print(a)

x2 = 6
y2 = 3
b = x2**y2
print(b)

x3 = 5
y3 = 2
c = x3/y3
print(c)

x4 = 7
y4 = 5
d = x4 < y4
print(d)

print("a的值為：""資料型態是：", type(a))
print("b的值為：""資料型態是：", type(b))
print("c的值為：""資料型態是：", type(c))
print(" d的值為：""資料型態是：", type(d))

# HW1
p = str(input("請輸入一個字串?"))
o = p[::-1]
if p == o:
    print("迴文判斷結果為""true")
else:
    print("迴文判斷結果為","flase")

##判斷式
"""
(a)單向判斷
if條件式：
    程式區塊
"""
# 範例1(成績的判斷)
score = int(input("請輸入您的分數："))
if score >= 60:  # if(score>=60):
    print("恭喜您及格了")

# 範例2(密碼判斷)
pw = input("請輸入密碼")
if(pw == "1234"):
    print("歡迎光臨")

# 範例3(判斷天氣)
rain = input("今天會下雨嗎?")
if(rain == "Y" or rain == "y" or rain == "會"):
    print("出門請帶雨具")


"""(b)雙向判斷
if條件式：
    程式區塊1
else
    程式區塊2
"""
# 範例1(成績的判斷)
score = int(input("請輸入您的分數："))
if score >= 60:  # if(score>=60):
    print("恭喜您及格了")
else:
    print("恭喜您不及格了")

# 範例2(密碼判斷)
pw = input("請輸入密碼")
if(pw == "1234"):
    print("歡迎光臨")
else:
    print("不歡迎光臨")

# 範例3(判斷天氣)
rain = input("今天會下雨嗎?")
if(rain == "Y" or rain == "y" or rain == "會"):
    print("出門請帶雨具")
else:
    print("出門請不要帶雨具")

# HW2
cash = int(input("請輸入購買金額?"))
if cash >= 9000:
    cash = cash*0.9
    print(cash)
else:
    print(cash)

i = int(input("請輸入一個整數?"))
u = i % 2
if u == 0:
    print(i, "為偶數")
else:
    print(i, "為奇數")


q = int(input("請輸入三角形邊長a長度為?"))
w = int(input("請輸入三角形邊長b長度為?"))
e = int(input("請輸入三角形邊長c長度為?"))
print("請輸入三角形邊長a長度為?", q)
print("請輸入三角形邊長b長度為?", w)
print("請輸入三角形邊長c長度為?", e)
if(q+w > e and w+e > q and q+e > w):
    print("可構成三角形")
else:
    print("無法構成三角形")
