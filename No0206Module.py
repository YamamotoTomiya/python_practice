import random

def Create_DNA(N):
    L1=[]
    for i in range(N):
        a=["A","T","C","G"]
        b=random.choice(a)
        L1.append(b)
    return L1

