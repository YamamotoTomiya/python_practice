import random

def Create_DNA(N):
    L1=[]
    for i in range(N):
        a=["A","T","C","G"]
        b=random.choice(a)
        L1.append(b)
    return L1

def Count_L1(L1,S):
    
    N=0
    for i in range(len(L1)):
        if L1[i]==S:
            N+=1
        else:
            N+=0
    return N

