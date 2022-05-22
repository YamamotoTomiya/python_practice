from random import random


import random

sum=0
for i in range(10):
    a=random.randint(0,100)
    print(i,'=',a)
    sum+=a
    
average=sum/10
print('average=',average)
