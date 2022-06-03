teststr=input("enter a string: ")
a=0
for i in teststr:
    
    if((ord(i)>=48) and ord(i)<=57):
       a=a+ord(i)-48
print(a)