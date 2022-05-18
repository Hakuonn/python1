"""
tuple元組
list串列
dict字典
set集合
"""

"""
tuple()
"""


from functools import partial
from typing import List
t1 = ()
print(t1)

t2 = 1, 2, 3
print(t2[0])

# t2[0]=3 #!無法更改元素數值

t3 = (1, 2, 3)
a, b, c = t3

a = 10
b = 20
a, b = b, a  # *資料交換

list1 = [1, 2, 3, 4]
t4 = tuple(list1)

t5 = (1, 2, 3, 4)
t6 = (t5, 5, 6)
print(t5)
print(t6)

print(t6[0])
print(t6[0][0])
print(t6[0][2])
print(t6[1])
print(len(t5))
print(len(t6))

t7 = ("z",)  # !資料只有一個時，後面要加,
t7_1 = ("z")  # !不加逗號會變str

"""
list[]
"""
list2 = [1, 2, 3, 4, 5]
list3 = ["蘋果", "草莓", "香蕉"]
print(list3[0])
print(list3[-1])
print(len(list3))
list4 = [1, 2, 3, "香蕉", "蘋果"]

list4_1 = []

list5 = [["Alex", "1234"], ["peko", "abcd"]]
print(list5[0][0])
print(list5[1][0])

"""
使用for 變數 in 串列讀取
"""
list6 = ["班代", "副班代", "學藝"]
for s in list6:
    print(s, end=" ")

# *不同型別的元素
items = [12, "apple", True]
i = 1
for item in items:
    print(item)

# 範例 成績對應

subjects = ["國文", "英文", "數學"]
scores = [90, 100, 88]
for i in range(len(scores)):
    print("%s的成績:%d分" % (subjects[i], scores[i]))

index1 = subjects.index("英文")  # !index 尋找在第幾位
print(index1)

subjects_1 = ["國文", "英文", "數學", "英文"]
count1 = subjects_1.count("英文")  # !count 統計字符串裡某個字符出現的次數

scores_1 = [90, 100, 88]
scores_1[0] = 100
print(scores_1)

# *增加串列元素
sopelist = ["牛奶", "咖啡豆", "西瓜", "鳳梨"]
# 1.append 加在最後一個
sopelist.append("加麵包")
# 2.insert 加在指定位置
sopelist.insert(3, "加蘋果")
sopelist.insert(20, "加蘋果")  # !功能會變跟append一樣

# *索引值為負
list7 = [1, 2, 3, 4]
list7.insert(-1, "love")
list7.insert(19, "IC")

# 範例 建立成績表
scores = []
total = inscore = 0
while(inscore != -1):
    inscore = int(input("請輸入學生成績:"))
    if (inscore != -1):
        scores.append(inscore)
print("共有%d位學生" % (len(scores)))
for score in scores:
    total += score
average = total/(len(scores))
print("本班總成績為:%d分,平均成績為:%5.2f" % (total, average))

# *刪除串列元素
# 1.remove() //串列名稱.remvove()
sopelist = ["牛奶", "咖啡豆", "西瓜", "鳳梨"]
sopelist.remove("咖啡豆")
# 2.pop()
sopelist.pop(-1)
# 3.del
del sopelist[0]
print(sopelist)

del sopelist[0:4:2]

# 範例 刪除不要的元素(顏色)
colors = ["紅", "橙", "黃", "綠", "藍"]
while True:
    print("顏色有:", colors)
    color = input("請刪除要刪除的顏色(Enter結束)")
    if (color == ""):
        break
    n = colors.count(color)
    if (n > 0):
        colors.remove(color)
    else:
        print(color, "不在串列中")

# *排序
# ? sort()由小排到大
list8 = [3, 8, 1, 9]
list8.sort()
print(list8)

# ? reverse() 反轉
list8.reverse()
print(list8)

# ? 由大到小
# 1.
list8.sort()
list8.reverse()
# 2.
list9 = sorted(list8, reverse=True)
print(list9)
print(list8)

# *其他常見字串處理方法
# ? 1. split分割字串
s1 = "國立高雄第一科大,國立高雄海洋科大,國立高應大"
list1 = s1.split("高雄")
print(list1)

# ? 2. join 連結字串
s2 = "AA".join(list1)
print(s2)

# ? 3. replace 取代
s3 = s1.replace("國立", "私立", 2)  # !replace(被取代,取代,option)
print(s3)

# ? 4. find 尋找
print(s1.find("海洋"))
print(s1.find("海洋洋"))

# ? 5. startswith 開始字串
str1 = "mailto:nkust@yahoo.com.tw"
print(str1.startswith("mailto"))
print(str1.startswith("mailtoto"))

# ? endswith 結尾字串
print(str1.endswith(".tw"))
print(str1.endswith(".cn"))

# 範例(判斷檔案名稱)
filename = input("請輸入圖片名稱")
if filename.endswith(".jpg") or filename.endswith(".JPG"):
    print("圖片格式為JPG")
else:
    print("圖片格式不是JPG")

# * tuple與list互相轉換
tuple1 = (1, 2, 3, 4)
list1 = list(tuple1)
list1.append(8)

list2 = [1, 2, 3, 4, 5]
tuple2 = tuple(list2)
tuple2.append(8)  # !轉成tuple後無法修改
"""
字典 dict
語法1:
字典名稱 = {key1:value1,key2:value2...}
"""
dict1 = {}
dict2 = {"高科大": "NKUST", "高應大": "KMU"}
print(dict2)

"""
語法2:
字典名稱 = dict([[key1,value1],[key2,value2]...])
"""
dict3 = dict([["高科大", "NKUST"], ["高應大", "KMU"]])

"""
語法3:
字典名稱 = dict(key1=value1,key2=value2...)
"""
"""
#!不能用數字當key
因為字典以key為主
以記憶體來說，字典是隨機性的
"""
dict4 = dict(高科大="NKUST", 高應大="KMU")

dict5 = {"侯先生": 900, "張小姐": 800, "林小弟": 30, "王小妹": 30}
print(dict5["侯先生"])
# print(dict5["李小姐"])
# print(dict5[0])
#!get //key不存在時不會產生錯誤，回傳None
print(dict5.get("李小姐"))
print(dict5.get("李小姐", "不再字典裡"))

# 範例 天氣
dict6 = {"春": "暖", "夏": "熱", "秋": "涼", "冬": "冷"}
name = input("輸入季節(春夏秋冬):")
feeling = dict6.get(name)
if feeling == None:
    print("沒有"+name+"季節")
else:
    print(name+"人體感覺為:"+dict6[name])

# *修改字典 如果沒有key就新增
dict5["侯先生"] = 650
dict5["侯先"] = 110

# *刪除字典
# ? 1. del 字典名稱[key] ; 指定特定元素
del dict5["侯先生"]

# ? 2.字典名稱.clear()
#!字典還存在
dict5.clear()

# ? 3. del 字典名稱
#!字典直接消失
del dict5

# *合併字典 update
lang1 = {"您好": "Hello"}
lang2 = {"早安": "Good Morning"}
lang1.update(lang2)

# *複製
# ? 指向同一個字典物件(lang3和lang4值都會改變)
lang3 = {"您好": "Hello"}
lang4 = lang3
lang4["您好"] = "HI"

# ? copy()指向不同字典物件
lang5 = {"您好": "Hello"}
lang6 = lang5.copy()
lang6["您好"] = "HI"

# *key & value
dict7 = {"春": "暖", "夏": "熱", "秋": "涼", "冬": "冷"}
keys1 = dict7.keys()
print(keys1)
print(keys1[0])  # !error

keys2 = list(keys1)
print(keys2[0])

value1 = dict7.values()
print(value1)

value2 = list(value1)
print(value2[2])

# *item()
lang7 = {"早安": "GOOD MORNING", "您好": "HELLO"}
lang8 = lang7.items()
for ch, en in lang7.items():
    print("中文為", ch, "英文為", en)

# *set集合 // {}或set 創建一個無序不重複元素集，可進行關係測試，刪除重複數據，還可以計算交集、差集、並集等。
s = {1, 2, 3, 4}
s = set(("a", 1, "b", 2))
s = set(["apple", 1, "banana", 2])
s = set({"早安": "Good Morning", "您好": "Hello"})

# * add and remove
s = set("NKUST")
s.add("z")
s.remove("N")

# *set運算
a = set("NKUST")
b = set("KMU")
print(a | b)  # !聯集
print(a & b)  # !交集
print(a-b)  # !差集
print(a ^ b)  # !互斥或

# *集合的比較
s1 = set("NKUST")
s2 = set("NKUSTs")
print(s1 < s2)  # !真子集合
print(s1 <= s2)  # !子集合
print(s1 >= s2)  # !超集合
print(s1 > s2)  # !真超集合

# HW1
city = ["台北", "新北", "桃園", "台中", "台南", "高雄"]
inCity = input("輸入要查詢的六都名稱")
if inCity in city:
    print("六都中有「%s」城市!" % (inCity))
else:
    print("六都中沒有「%s」城市!" % (inCity))


pm25 = {"台北市": 13, "新北市": 8, "桃園市": 8, "台中市": 6, "台南市": 14, "高雄市": 24}
inCityPM = input("輸入要查詢的六都名稱:")
ppmm = pm25.get(inCityPM)
if ppmm == None:
    print("六都沒有"+inCityPM)
else:
    print(inCityPM, "今天的PM2.5值為:", pm25[inCityPM])


# HW2
cnYear = {"鼠": "親切和藹", "牛": "保守努力", "虎": "熱情大膽", "兔": "溫柔慈善"}
listcnYear = list(cnYear.items())
animal = input("請輸入生肖:")
for i in range(4):
    if animal == listcnYear[i][0]:
        print("生肖屬", animal, "的性格特徵為", listcnYear[i][1])

# HW3
students = set(['John', 'Mary', 'Tina', 'Fiona',
               'Claire', 'Eva', 'Ben', 'Bill', 'Bert'])
english = set(['John', 'Mary', 'Fiona', 'Claire', 'Ben', 'Bill'])
math = set(['Mary', 'Fiona', 'Claire', 'Eva', 'Ben'])
print("英文與數學都及格"+str(english & math))
print("數學不及格"+str(students ^ math))
print("英文及格且數學不及格"+str((english) & (students ^ math)))
