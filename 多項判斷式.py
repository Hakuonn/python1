"""
(c)多向式
if 條件1:
    程式區塊1
elif 條件2:
    程式區塊2
elif 條件3:
    程式區塊3
    .
    .
    .
else:
    程式區塊N
"""

# 範例1(成績等第)
score = int(input("請輸入您的分數:"))
if score >= 90:
    print("甲等")
elif score >= 80:
    print("乙等")
elif score >= 70:
    print("丙等")
elif score >= 60:
    print("丁等")
else:
    print("您的成績未通過!")
# 範例2
age = int(input("請輸入您的年齡:"))
if age < 6:
    print("可以看普通級")
elif age < 12:
    print("可以看普通級及保護級")
elif age < 18:
    print("可以看限制級以外的電影")
else:
    print("您已經成年，您可以觀看所有等級的電影")


# HW1
u = int(input("請輸入物品重量?"))
if u <= 5:
    print("所需郵資為50元")
elif u <= 10:
    print("所需郵資為70元")
elif u <= 15:
    print("所需郵資為90元")
elif u <= 20:
    print("所需郵資為110元")
else:
    print("超過20公斤無法寄送")

# HW2
kg = int(input("請輸入體重(KG)?"))
m = float(input("請輸入身高(M)?"))
print("請輸入體重(KG)?", kg)
print("請輸入身高(M)?", m)
bmi = kg/(m**2)
if bmi < 18:
    print("bmi為", bmi, "體重過輕")
elif bmi < 24 and bmi >= 18:
    print("bmi為", bmi, "體重正常")
elif bmi < 27 and bmi >= 24:
    print("bmi為", bmi, "體重過重")
else:
    print("bmi為", bmi, "體重肥胖")

# HW3
money = int(input("請輸入購買金額："))
if money >= 100000:
    money *= 0.8
    print(money, "元")
elif money >= 50000:
    money *= 0.85
    print(money, "元")
elif money >= 30000:
    money *= 0.9
    print(money, "元")
elif money >= 10000:
    money *= 0.95
    print(money, "元")
else:
    print(money, "元")

# HW4
a = int(input("請輸入a的值"))
b = int(input("請輸入b的值"))
c = int(input("請輸入c的值"))
print("a=", a)
print("b=", b)
print("c=", c)
if a > b and a > c:
    print("最大值為", a)
elif b > a and b > c:
    print("最大值為", b)
else:
    print("最大值為", c)

# HW5
month = int(input("請輸入月份"))
if month <= 3 and month > 0:
    print("春")
elif month <= 6 and month >= 4:
    print("夏")
elif month <= 9 and month >= 7:
    print("秋")
elif month <= 12 and month >= 10:
    print("冬")
else:
    print(month, "月份不在範圍內")

# HW6
rt = int(input("請輸入今年收入淨額"))
if rt > 2000000:
    rt *= 0.3
    print("付稅金額:", rt, "元")
elif rt >= 1000000 and rt < 2000000:
    rt *= 0.21
    print("付稅金額:", rt, "元")
elif rt >= 600000 and rt < 1000000:
    rt *= 0.13
    print("付稅金額:", rt, "元")
elif rt >= 300000 and rt < 600000:
    rt *= 0.06
    print("付稅金額:", rt, "元")
elif rt < 300000:
    print("免稅")

# HW7
x = int(input("請輸入x值"))
y = int(input("請輸入y值"))
if x > 0 and y > 0:
    print("(", x, ",", y, ")", "在第一象限")
elif x < 0 and y > 0:
    print("(", x, ",", y, ")", "在第二象限")
elif x < 0 and y < 0:
    print("(", x, ",", y, ")", "在第三象限")
elif x < 0 and y < 0:
    print("(", x, ",", y, ")", "在第四象限")
elif x == 0 and y == 0:
    print("(", x, ",", y, ")", "在原點")
elif x < 0 or x > 0 and y == 0:
    print("(", x, ",", y, ")", "在X軸上")
elif x == 0 and y > 0 or y < 0:
    print("(", x, ",", y, ")", "在Y軸上")

# HW8
x = float(input("請輸入體溫？"))
if x >= 39:
    print("體溫很燒")
elif x >= 38 and x < 39:
    print("體溫有點燒")
elif x >= 36 and x < 38:
    print("體溫正常")
elif x < 36:
    print("體溫過低")

# HW9
year = int(input("請輸入年份？"))
if year % 400 == 0:
    print(year, "是閏年")
elif year % 100 == 0 and year % 400 != 0:
    print(year, "不是閏年")
elif year % 4 == 0 and year % 100 != 0:
    print(year, "是閏年")
elif year % 4 != 0:
    print(year, "不是閏年")
