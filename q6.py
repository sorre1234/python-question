a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
for i in range (b,a+1):
    x=0
    for j in range (2,i):
        if (i%j==0):
     
            break;
        else:
            x=x+1
    if(x==i-2):
        print(i,"is a prime number")        
        


            



 
    
    


