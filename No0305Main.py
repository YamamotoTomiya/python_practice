import No0305Module

a=No0305Module.Get_Initial(10)
print(a)
n2=6
b=No0305Module.Get_List(a,n2)
print(b)
c=[]
for i in range(len(b)):
    c.append(a[b[i]])
print(c)