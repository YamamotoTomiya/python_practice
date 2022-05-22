import random
def Get_ATCG():
    a=["A","T","C","G"]
    return random.choice(a)

def Get_ATCG_List(n1:int):
    a=[]
    for i in range(n1):
        a.append(Get_ATCG())
    return a

def Print_List(a:list):
    print(a)

