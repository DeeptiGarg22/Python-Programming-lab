name=[]
age=[]
for i in range(3):
    name=list(map(str,input().split()))
    age=list(map(int,input().split()))
    a=dict(zip(name,age))
    print(i)