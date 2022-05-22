from cmath import sqrt


def Get_Angle(a:list[float],b:list[float]) ->float:
    c=0
    for i in range(len(a)):
         c+=a[i]*b[i]
    asum=0
    bsum=0
    for i in range(len(a)):
        asum+=a[i]**2
    for i in range(len(b)):
        bsum+=b[i]**2
    anrm=sqrt(asum)
    bnrm=sqrt(bsum)
    nrm=anrm*bnrm
    return c/nrm
