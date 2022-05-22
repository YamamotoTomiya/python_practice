import random

def Create_DNA(N):
    L1=[]
    for i in range(N):
        a=["A","T","C","G"]
        b=random.choice(a)
        L1.append(b)
    return L1

def Slice_L1(L1,N1,N2):
    L2=L1[N1:N2]
    return L2

