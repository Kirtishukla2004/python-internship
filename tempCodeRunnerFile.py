print("even number sum ", even_sum)
print("odd sum", odd_sum)
print("count of even numbers", count_even)
print("count of odd numbers ", count_odd)
for i in range(0, 10, 1):
    if (li[i] > li[0]):
        li[0] = li[i]
print(li[0])