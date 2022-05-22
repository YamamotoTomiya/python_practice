import random
import No0301Module

score=[]
print(score)
for i in range(5):
    a=random.randint(0,100)
    score.append(a)

print(score)

b=No0301Module.Get_Average(score)
c=No0301Module.Get_Variance(score)
print(b)
print(c)

