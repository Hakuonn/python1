"""
迴圈
range()整數串列
語法:range(終止值)
range(起始值,終止值,間隔值)
"""
list1 = range(5)
print(list(list1))

list2 = range(3, 8)
print(list(list2))

list3 = range(3, 8, 2)  # !元素每次增2
print(list(list3))

list4 = range(8, 3, -1)  # !間隔值是負值
print(list(list4))

list5 = range(-2, 4)  # !起始值是負值
print(list(list5))


"""
for迴圈
用於執行固定次數
語法:
for變數in串列:
        程式區塊
"""
# 範例1 顯示串列元素
list6 = ["蘋果", "橘子", "香蕉"]
for s in list6:
    print(s)

# 範例2 1+2+3+...+10之和(for range)
sum = 0
for i in range(1, 11):
    sum += i
print(sum)

"""
sum=0
for i in range(1,11):
    sum+=i
    print(sum) #!這樣會加10次
"""

# HW1
a = int(input("請輸入正整數"))
for b in range(1, a+1, 1):
    print(b)
# HW2
c = int(input("請輸入正整數"))
sum = 0
for i in range(1, c+1):
    sum += i
print(sum)

del(sum)
# HW3
q = int(input("請輸入開始值?"))
w = int(input("請輸入終止值?"))
e = int(input("請輸入增減值?"))
sum = 0
for r in range(q, w, e):
    sum += r
    print("i為", r, "加總結果為", sum)


# 巢狀for迴圈
for i in range(1, 6):  # !外部迴圈 執行5次
    print("外部第", i, "次迴圈,內部執行", i, "次迴圈:", end="")
    for j in range(1, i+1):  # !內部迴圈
        print("#", end="")
    print()  # !換行

# 範例3 9x9乘法表
for i in range(1, 10):
    for j in range(1, 10):
        product = i*j
        print("%dx%d=%2d " % (i, j, product), end="")
    print()

# HW4
a = int(input("請輸入正整數"))
for i in range(1, a+1):
    for j in range(1, 1+i):
        print(j, end="")
    print()

# HW5
b = int(input("請輸入正整數"))
for k in range(b, 0, -1):
    for l in range(k, 0, -1):
        print("*", end="")
    print()

# break & continue
# break範例
for i in range(1, 11):
    if(i == 4):
        break
    print(i, end=",")
print()
# continue範例
for i in range(1, 11):
    if(i == 4):
        continue
    print(i, end=",")
print()

# in運算子
a = (1, 2, 3, 4)
if 8 in a:
    print("數字1在tuple a 中")
else:
    print("數字1不在tuple a 中")

b = list("fsdfhusdfhsudoihfsuhf")
if "f" in b:
    print("f在串列b裡")
else:
    print("f不在串列b裡")

lang1 = {"早安": "Good mornrng", "謝謝": "Thank you"}  # !字典{"key":"value"}
if "謝謝" in lang1:
    print("謝謝的英文是", lang1["謝謝"])
else:
    print("查不到'謝謝'的英文")

c = set("tiger")
if "t" in c:
    print("t在此集合中")
else:
    print("t不在此集合中")

# HW6
a = int(input("請輸入正整數:"))
for i in range(1, a+1):
    if i % 5 == 0:
        continue
    print(i, end=" ")
print()

# *聖誕樹
h = 5
s = 1
for i in range(h):
    print((" "*(h-i))+("*"*s))
    s += 2
