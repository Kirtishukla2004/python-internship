#wap to print numbers from 1 to 10
for i in range(1,11,1):
    print(i)
#wap to print from 70 to 1 reverse counting 
print("reverse counting ")
for i in range(71,0,-1):
   
    print(i)
print("even numbers from 2 to 20 ")
#wap to print even numbers from 2 to 20 
for j in range(2,21,2):
   print(j)

#wap to print odd numbers from 50 to 1 in reverse format 
 
for i in range(50,1,-1):
    if(i%2==0):
        ""
    else:
        print(i)

#wap to implement sum of all even numbers from 2 to 20 
sum=0
for j in range(2,21,2):
    sum+=j
print("print sum of even numbers,",sum)

#sum of all odd numbers from 30 to 70 
sum_odd=0
for i in range(30,70,1):
    if(i%2==0):
        ' '
    else:
        sum_odd+=i
print("print sum of odd numbers ",sum_odd)
#wap to print table of 5 
for i in range(5,51,5):
    print(i)
#wap to sum 2 given numbers 
num1=int(input("enter first number "))
num2=int(input("enter second number "))
sum =num1+num2
print("sum of two number ",sum)
#wap to  print table of any given number 
digit=int(input("enter number of table you want "))
last_digit=(digit*10)+digit
for i in range(digit,last_digit,digit):
    print(i)
#wap to print factorial of a given number 
result = 1
fact_digit = int(input("Enter the number of which factorial you want: "))

if fact_digit < 0:
    print("Factorial is not defined for negative numbers.")
elif fact_digit == 0 or fact_digit == 1:
    print("Factorial of", fact_digit, "is 1")
else:
    for i in range(2, fact_digit + 1):
        result *= i
    print("Factorial of", fact_digit, "is", result)
