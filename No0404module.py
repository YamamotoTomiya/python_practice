def Get_Product(a:list[float],b:list[float]) ->float:
    c=0
    if len(a)==len(b):
     for i in range(len(a)):
        c+=a[i]*b[i]
     return c
    else:
        print("error:be the same in length")