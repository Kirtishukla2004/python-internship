# wap to  calculate operation enter your choice number sum sub mul div given of any two number
a=int(input("enter first number "))
b=int(input("enter second number "))
choice=str(input("what you operation you want enter these \nsum=+\nsubtract=-\nmulti=*\ndivide=/  "))
if(choice =='+'):
    print("sum",a+b)
elif(choice =='-'):
    print("subtraction",a-b)
elif(choice =='*'):
    print("multiply",a*b)
elif(choice =='/'):
    print("divide",a/b)
else:
    print("WRONG INPUT.....")


# wap calculate given result all subjects marks of students act to condition
sci =int(input("enter science marks "))
maths =int(input("enter maths marks "))
eng=int(input("enter english marks "))
hindi=int(input("enter hindi marks "))
sum_sub=sci+maths+eng+hindi
per= (sum_sub/400)*100
if(per>90 and per<=100):
    print("A GRADE ")
    print("percentage",per)
    print("total marks ",sum_sub)
elif(per>80 and per<=90):
    print("B GRADE")
    print("percentage",per)
    print("total marks ",sum_sub)
elif(per>70 and per<=80):
    print("C GRADE")
    print("percentage",per)
    print("total marks ",sum_sub)
elif(per>60 and per<=70):
    print("D GRADE")
    print("percentage",per)
    print("total marks ",sum_sub) 
elif(per>50 and per<=60):
    print("FAIL.... :(")
    print("percentage",per)
    print("total marks ",sum_sub)
else:
    print("WRONG INPUTS......")

# wap to check greatest number given  between three number
a = int(input("enter  a"))
b = int(input("enter b "))
c = int(input("enter c "))
if (a > b):
    if (a > c):
        print("a is the greatest", a)
    else:
          print("c is the greast ", c)
elif (b > a):
    if (b > c):
        print("b is the greatest", b)
    else:
        print("c is the greatest ", c)
else:
      print("c is the greatest ", c)

#sum of any given 10 number using list 
li=[]
s=0
for i in range(0,10,1):
     a=int(input("enter list element"))
     li.append(a)
     s=li[i]+s

print(li)
print("sum",s)
print(sum(li))
