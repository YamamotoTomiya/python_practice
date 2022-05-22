import random

def Get_Initial():
    a=[]
    for i in range(10):
        b=random.randint(0,10)
        a.append(b)
    return a

def Count(n1,a):
    count=0
    for i in range(len(a)):
        if n1==a[i]:
            count+=1
    return count