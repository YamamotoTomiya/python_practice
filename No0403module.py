def Add_V(a:list[float],b:list[float]) ->list[float]:
    c=[]
    if len(a)==len(b):
        for i in range(len(a)):
            c.append(a[i]+b[i])
        return c
    else:
        print("error:be the same in length")

def Substitue_V(a:list[float],b:list[float]) ->list[float]:
    c=[]