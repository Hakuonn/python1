import random
def lotto():
    a=int(input("a"))
    b=int(input("b"))
    c=[]
    for i in b:
        d=random.randrange(0,a)
        c.append(d)
    print(c)