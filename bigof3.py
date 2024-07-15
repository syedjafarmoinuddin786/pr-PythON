# WRITING A PROGRAM TO FIND THE LARGEST OF THREE NUMBERS...
a=int(input("ENTER m:"))
b=int(input("ENTER n:"))
c=int(input("ENTER o:"))
if a>b and a>c:
    print("a is LARGE",a)
elif b>a and b>c:
    print("b is LARGE",b)
elif c>a and c>b:
    print("c is LARGE",c)
else:
    print("INVALID EXPRESSION")
