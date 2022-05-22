def Get_List(a,n1,n2):
    
    if len(a)>=n1+n2:
        b=a[n1-1:n1+n2-1]
    else:
        b=a[n1:]
    return b