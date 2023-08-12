'''wap print no from 1to 10
Wap print reverse no from 31 to 1
Wap print all even no from 20 to 70
Wap print all odd no from 30 to 1 in reverse format
Wap print table of 6
Wap a program sum of given any 10 no.
Wap print table of any given no.
Wap calculate factorial value given of any no.
 Wap sum of all even no. From 1 to n given no.
Wap print reverse given of any no
Wap sum of all digits given of any no
Wap count all digits given of any no.'''
i=1
while i <11:
    print(i)
    i+=1
a=32
while a>0:
    print(a)
    a-=1
a=19
while a<70 and a>=19:
    if(a%2==0):
        print(a)
    else:
        {
            print(" ")
        }
    a+=1

a=31
while a>0 :
    if(a%2==0):
        print(" ")
    else:
        {
            print(a)
        }
    a-=1
a=0
while a<61:
    i=1
    print(a*i)
    a+=6


n= int(input("enter any number "))
sum=0
while 0<n:
    sum+=n
    n-=1
print(sum)
a=int(input("enter any number "))
i=0
while i<10:
    i+=1
    print(a*i)


n=int(input("enter any number "))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)

n=int(input("enter any number "))
a=0
sum=0
while a<=n:
    if(a%2==0):
        sum=sum+a
    a+=1
print(sum)
n= int(input("enter number "))
r=0
while (n>0):
    d=n%10
    r=r*10+d
    n=n//10
print(r)
n=int(input("enter number "))
count=0
while (n!=0):
    n//=10
    count+=1
   
print(str(count))