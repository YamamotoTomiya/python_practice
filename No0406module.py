import random
def Get_List(n1:int) ->list[float]:
    a=[]
    for i in range(n1):
        a.append(random.random)
    return a

def Moving_Average(a:list[float],n1:int) ->list[float]:
    
    b=[]
    for i in range(len(a)):
        sum=0
        for j in range(i+n1):
            sum+=a[i]
        ave=sum/j
        b.append(ave)
    return b

