import random
import No0303Module

a=[]
for i in range(10):
    b=random.randint(0,10)
    a.append(b)
print(a)
b=No0303Module.Get_List(a,3,4)
print(b)
c=No0303Module.Get_List(a,2,11)
print(c)