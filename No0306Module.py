from operator import imod

import random
def Get_Max(a):
    b=a[0]
    c=0
    for i in range(len(a)):
        if b<=a[i]:
            b=a[i]
            c=i
    return b,c

def Get_Min(a):
    b=a[0]
    c=0
    for i in range(len(a)):
        if b>=a[i]:
            b=a[i]
            c=i
    return b,c

def Get_Initial_Real100(n1,d1):
    a=[0]*n1
    for i in range(n1):
        rand=random.uniform(0,d1)
        a[i]=rand
    return a

