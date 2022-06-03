def change(nuset,n):
    
    comm=input("enter the command: ")
    if (comm=="asc"):
        return nuset.sort()
    elif(comm=="desc"):
        nuset.sort()
        nuset.reverse()
        return nuset
    elif(comm=="none"):
        return nuset
    
    
    
    
    
n=int(input("enter the length of list: "))
list1=[]
for i in range(n):
    element=int(input("enter the element "))
    list1.append(element)
print(change(list1,n))