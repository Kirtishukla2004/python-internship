
li = []
m = 3
n = 3
s=0

for i in range(n):
    row = []
    for j in range(m):
        val = int(input("Enter a value: "))
        row.append(val)
        s=s+val
    li.append(row)

print(li)
print("sum",s)
