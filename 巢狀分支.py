
## 巢狀分支
# 範例1
score = float(input("請施入一個學生成績："))
if score < 0 or score > 100:
    print("輸入分數範圍有誤")
else:
    if 90 <= score:
        print("A")
    else:
        if 80 <= score:
            print("B")
        else:
            if 70 <= score:
                print("C")
            else:
                if 60 <= score:
                    print("D")
                else:
                    print("E")

# 範例2(BMI國軍標準)

gender = input("請輸入性別(m/f)")
height = float(input("請請輸入身高(m)："))
weight = float(input("請輸入體重(kg)："))
bmi = weight/height**2
print("BMI為{:.2f}:".format(bmi))  
if gender == "f":
    if bmi >= 26:
        print("不合格")
    else:
        print("合格")
else:
    if bmi >= 30:
        print("不合格")
    else:
        print("合格")
    
# HW1
score1 = float(input("輸入一個期中考分數(0~100)："))
score2 = float(input("輸入一個期末考分數(0~100)："))
score3 = (score1*0.4+score2*0.6)
print("總分為：%.2f" % (score3))
if 90 <= score3 <= 100:
    print("A")
else:
    if 80 <= score3 < 90:
        print("B")
    else:
        if 70 <= score3 < 80:
            print("C")
        else:
            if 60 <= score3 < 70:
                print("D")
            else:
                if 0 < score3 < 60:
                    print("E")
                else:
                    print("超出範圍")

# HW2
x = float(input("輸入x座標點："))
y = float(input("輸入y座標點："))
if x > 0 and y > 0:
    print("第一象限")
else:
    if x < 0 and y > 0:
        print("第二象限")
    else:
        if x < 0 and y < 0:
            print("第三象限")
        else:
            if x > 0 and y < 0:
                print("第四象限")
            else:
                if x == 0 and y > 0 or y < 0:
                    print("Y軸上")
                else:
                    if y == 0 and x > 0 or x < 0:
                        print("X軸上")
                    else:
                        if x == 0 and y == 0:
                            print("原點上")

# HW3
A = input("請輸入車輛種類(B或C)：")
KM = float(input("請輸入超速公里數(浮點數)"))
if A == "B":
    if KM < 20:
        print("罰金 1,200")
    else:
        if KM < 40:
            print("罰金 1,400")
        else:
            if KM < 60:
                print("罰金 1,600")
            else:
                if KM < 80:
                    print("罰金 8,000")
                else:
                    if KM < 100:
                        print("罰金 12,000")
                    else:
                        if KM >= 120:
                            print("罰金罰金 24,000")
else:
    if KM < 20:
        print("罰金 1,600")
    else:
        if KM < 40:
            print("罰金 1,800")
        else:
            if KM < 60:
                print("罰金 2,000")
            else:
                if KM < 80:
                    print("罰金 8,000")
                else:
                    if KM < 100:
                        print("罰金 12,000")
                    else:
                        if KM >= 120:
                            print("罰金罰金 24,000")
