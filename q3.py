def operations(a,comm,b):
    if comm=="+":
        return a+b
    elif comm=="-":
        return a-b
    elif comm=="/":
        return a/b
    elif comm=="*":
        return a*b

a=int(input("enter the first numbers: "))
command=(input("enter the command: "))
b=int(input("enter the second number: "))
print(operations(a,command,b))