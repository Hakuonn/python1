"""
while loop
用於執行次數不固定的迴圈
語法:
while 條件式:
    程式區塊
"""
# 範例1 計算1+2+3+...+10之和
total = n = 0
while(n < 10):
    n += 1
    total += n
print(total)

# 範例2(n!)
total = i = 1
n = int(input("請輸入正整數n的值:"))
while (i <= n):
    total *= i
    i += 1
print("%d!=%d" % (n, total))

# 範例2 for loop
total = 1
n = int(input("請輸入正整數n的值:"))
for i in range(1, n+1):
    total *= i
print(total)

# 判斷三角形
while True:
    a = float(input("輸入三角形最短邊長:"))
    b = float(input("輸入三角形最長邊長:"))
    c = float(input("輸入三角形第三邊長:"))
    if a+b > c and b+c > a and a+c > b:
        if a == b == c:
            print("正三角形")
        else:
            if b**2 == a**2+c**2:
                if b == c:
                    print("等腰直角三角形")
                else:
                    print("直角三角形")
            elif b**2 > a**2+c**2:
                if a == c:
                    print("等腰鈍角三角形")
                else:
                    print("鈍角三角形")
            elif b**2 < a**2+c**2:
                if a == c:
                    print("等腰銳角三角形")
                else:
                    print("銳角三角形")
            elif b == c:
                print("等腰三角形")
    else:
        print("不是三角形")
    q = input()
    if q == "q":
        print("bye")
        break
    else:
        pass

# 測試帳密
user = "test"
key = "0000"
logIn = input("輸入帳號:")
keyIn = input("輸入密碼:")
if logIn == user and keyIn == key:
    print("帳號與密碼正確")
else:
    print("登入失敗")

# 因數&質數
a = int(input("輸入一個正整數:"))
b = []
for i in range(1, a+1):
    if a % i == 0:
        b.append(i)
        continue
    else:
        pass
if len(b) == 2:
    print("%d是質數" % (a))
else:
    print("%d不是質數" % (a))
    print(b)

# * N!超過M的最小N值
M = int(input("請輸入M?"))
t = 1
i = 1
while M > t:
    i += 1
    t *= i
print("%d階乘為%d大於%d" % (i, t, M))

# 偶數總和和奇數總和、3及7倍數總和&比較大小
x = int(input("輸入一個正整數:"))
oven = 0
odd = 0
three = 0
seven = 0
for i in range(1, x+1, 1):
    if i % 2 == 0:
        oven += i
        continue
    elif i % 2 != 0:
        odd += i
        continue
for i in range(1, x+1, 1):
    if i % 3 == 0:
        three += i
        continue
    elif i % 7 == 0:
        seven += i
        continue
print("偶數總和為:", oven)
print("奇數總和為:", odd)
print("3及7的倍數總和為:", three+seven)
ts = three+seven
if oven > odd > ts:
    print(oven, ">", odd, ">", ts)
elif odd > ts > oven:
    print(odd, ">", ts, ">", oven)
elif ts > oven > odd:
    print(ts, ">", oven, ">", odd)
elif odd > oven > ts:
    print(odd, ">", oven, ">", ts)
elif ts > odd > oven:
    print(ts, ">", odd, ">", oven)
elif oven > ts > odd:
    print(oven, ">", ts, ">", odd)
if oven >= odd > ts:
    print(oven, ">=", odd, ">", ts)
elif odd >= ts > oven:
    print(odd, ">=", ts, ">", oven)
elif ts >= oven > odd:
    print(ts, ">=", oven, ">", odd)
elif odd >= oven > ts:
    print(odd, ">=", oven, ">", ts)
elif ts >= odd > oven:
    print(ts, ">=", odd, ">", oven)
elif oven >= ts > odd:
    print(oven, ">=", ts, ">", odd)
if oven > odd >= ts:
    print(oven, ">", odd, ">=", ts)
elif odd > ts >= oven:
    print(odd, ">", ts, ">=", oven)
elif ts > oven >= odd:
    print(ts, ">", oven, ">=", odd)
elif odd > oven >= ts:
    print(odd, ">", oven, ">=", ts)
elif ts > odd >= oven:
    print(ts, ">", odd, ">=", oven)
elif oven > ts >= odd:
    print(oven, ">", ts, ">=", odd)
elif oven == odd == ts:
    print(oven, "=", odd, "=", ts)
