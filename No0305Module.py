import random

def Get_List(a,n1):
    b=[]
    for i in range(len(a)):
        if a[i]>=n1:
            b.append(i)
    return b

def Get_Initial(n1):
    a=[]
    for i in range(n1):
        b=random.randint(0,10)
        a.append(b)
    return a
