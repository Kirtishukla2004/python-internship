#non parametrizwd function 
def sum_digi():
    a=4
    v=10
    c=a+v
    print("non parametrized function called",c)

def subtract(a,b):
    c=a+b
    print("parametrized  with return keyword function called")
    return c

def multiply(a,b):
    mul=a*b
    print("parametrized function called",mul)

def divide():
    a=1000
    b=100
    c=a/b
    print("non parametrized with return keyword")
    return c



sum_digi();
print(subtract(20,3))
multiply(30,2)
print(divide())

from calculator import*
main();
a=int(input("enter digti to check  "))
temp=a
s=0
str=str(a)
c=len(str)
while temp>0:
    digti=temp%10
    cube=digti**c
    s=s+cube
    temp//=10

if(s==a):
    print(a,"is an armstrong number")
else:
     print(a,"is not an armstrong number")
    
