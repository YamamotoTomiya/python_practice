a=[2,4,5,3,7]
print("元の配列：",a)
for i in range(5):
    count=0
    for j in range(4):
        if a[count]<=a[count+1]:
            a[count],a[count+1]=a[count+1],a[count]

        count+=1
    print(i+1,"回入れ替え後：",a)
