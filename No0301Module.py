
from statistics import variance


def Get_Average(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    average=sum/len(a)
    return average

def Get_Variance(a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    average=sum/len(a)
    sum2=0.0
    for i in range(len(a)):
        sum2+=(average-a[i])**2.0
    var=sum2/len(a)
    return var
