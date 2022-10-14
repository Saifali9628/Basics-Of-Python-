#Write a program to find greatest of four numbers enterd by the user
a= int(input("Enter a First No: "))
b= int(input("Enter a Second No: "))
c= int(input("Enter a Third No: "))
d= int(input("Enter a Fourth No: "))
if(a>d):
    f1=a
else:
    f1=d
    if(b>c):
        f2=b
    else:
        f2=c
if(f1>f2):
    print(f1, "is the Greater number")
    
else:
    print(f2, "is the Greater number")