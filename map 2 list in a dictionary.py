z={}
name=list(map(str,input().split()))
age=list(map(int,input().split()))
a=len(name)
for i in range(a):
    b=name[i]
    c=age[i]
    z[b]=c
print(z)
