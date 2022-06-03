str=input("enter a string: ")
l=[]
for i in str:
    l.append(i)
l.sort()
for i in l:
    print(i,end='') 
