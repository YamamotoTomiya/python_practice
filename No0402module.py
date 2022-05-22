from cmath import sqrt


def Get_V_Magnitude(a:list[float]):
    sum=0
    for i in range(len(a)):
        sum+=a[i]**2
    return sqrt(sum)


