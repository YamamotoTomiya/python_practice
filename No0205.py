import random

sum=0
while sum<100:
    b=random.random()
    a=b*10
    sum+=a
    print('乱数は',a)
    print('合計:',sum)

print('Finish:100を超えました')