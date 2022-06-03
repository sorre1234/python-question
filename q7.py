l=eval(input("enter array"))
p=[]

for i in l:
    if i not in p:
        p.append(i)
for i in p:
    x=0
    y=0
    k=0
    for j in l:
        if(j==i):
            y=y+1
    if(y>x):
        x=y
        k=i
print("highest frequency=",k)
        



