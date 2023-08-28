
li = []
m = 3
n = 3
s = 0
val=0
for i in range(n):
    row = []
    for j in range(m):
        val = int(input("Enter a value: "))
        row.append(val)
        s = s+val
    li.append(row)

print(li)
print("sum", s)



def rowwiseadd(li):
    sum_row = 0
    print("rowwise wise addition ")
    for i in range(0, len(li)):
        for j in range(0, len(li)):
            sum_row = sum_row+li[i][j]
            print(li[i][j], " + ", end="")
        print("=", sum_row)


def colwiswadd(li):
    sum_col = 0
    print("column wise addition ")
    for i in range(0, len(li)):
        for j in range(0, len(li)):
            sum_col = sum_col+li[j][i]
            print(li[j][i], " + ", end="")
        print("=", sum_col)

rowwiseadd(li);
colwiswadd(li);