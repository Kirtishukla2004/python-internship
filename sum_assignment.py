#WAP of given 3 numbers calculate total percentage of given subjects marks of students '''
maths=int(input("enter maths marks "))
sci=int(input("enter science marks "))
sst=int(input("enter sst marks "))

sum_sub=maths +sci +sst
print("sum of all subjects",sum_sub)
percentage=(sum_sub/300)*100
print("percentage",percentage)
#wap to swap two variable values with each other using third variable given of any number 
num1=int(input("enter first number "))
num2=int(input("enter first number "))
print("number1 before ",num1)
print("numbe2 before ",num2)
swap=num1
num1=num2
num2=swap

print(" after swape numbers num1 ,num2",num1,num2)
#wap to swap two variable with each other without using 3rd variable 
c=int(input("enter first variable"))
d=int(input("enter second variable "))
c,d=d,c
print("c",c)
print("d",d)
#calculate area of rectangle 
l=int(input("enter lenght "))
b=int(input("enter breath"))
area=l*b
print("area of rectangle",area)

#area of circle 
pie=3.14
radius=int(input("enter radius of circle "))
area_circle=pie*radius*radius
print("area of circle is",area_circle)
#net salary 
salary=int(input("enter salary"))
pa=salary*2/100
print("pa",pa)
ba=salary*3/100
print("ba",ba)
hra=salary*3/100
print("hra",hra)
income_tax=salary*2/100
print("incoometax",income_tax)
sumof_extra=pa+ba+hra+income_tax
final_sal=salary-sumof_extra
print("net salary",final_sal)
print(id(salary))