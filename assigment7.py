li = []
even_sum = 0
odd_sum = 0
count_even = 0
count_odd = 0
print("enter elements")
for i in range(10):
    a = int(input(" "))
    li.append(a)
    if (li[i] % 2 == 0):
        even_sum = li[i]+even_sum
        count_even += 1

    else:
        odd_sum = li[i] + odd_sum
        count_odd += 1
print("numbers are ", li)
print("even number sum ", even_sum)
print("odd sum", odd_sum)
print("count of even numbers", count_even)
print("count of odd numbers ", count_odd)
for i in range(0, 10, 1):
    if (li[i] > li[0]):
        li[0] = li[i]
print(li[0])

n = int(input("enter number "))
m=int(input("enter the umber you wanna replace"))
count_number = 0
sum_number=0

for i in range(0, 10, 1):
    if (li[i] == n):
        print("n is on li[", i, "]")
        count_number += 1
        sum_number=n+sum_number
print("count of exiting number ", count_number)
print("sum of existing number ",sum_number)
l = []
for i in range(5):
    a = int(input(" "))
    l.append(a)

n = int(input("enter number "))
m = int(input("enter the number you wanna replace"))
for i in range(0, 5, 1):
    if (l[i] == n):
        # li.insert(i,m)
        l[i] = m

print(l)
