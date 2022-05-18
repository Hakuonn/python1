#輸入成績：inpiut命令
##由input()所接收的值是字串狀態
score1=input("輸入程式設計成績：")
score2=int(input("請輸入微積分成績："))
print(type(score1))
print(score1)
print(score1+10)


print("程式設計分數是："+(score1))
print("微積分分數是："+str(score2))

scoreA=input("請輸入國文成績：")
scoreB=input("請輸入英文成績：")
scoreC=input("請輸入數學成績：")
total=scoreA+scoreB+scoreC
print(total)
print("您的總分數是："+total)

##利用int() str()
scoreA=int(input("請輸入國文成績："))
scoreB=int(input("請輸入英文成績："))
scoreC=int(input("請輸入數學成績："))
total=scoreA+scoreB+scoreC
print(total)
print("您的總分數是："+str(total))

