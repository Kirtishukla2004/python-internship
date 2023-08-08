'''*
**
***
****
*****'''
for i in range(1,7,1):
    for j in range(1,i,1):
        print("*",end="")
    print()

'''
- - - - - 1
- - - - 12
- - - 123
- - 1234
- 12345
123456'''
print("SECOND PATTERN ")
for i in range(1,7,1):
    for k in range(6,i,-1):
        print("-",end=" ")
    
    for j in range(1,i+1,1):
         print(j,end="")
    print()

'''
12345
- 1234
- - 123
- - - 12
- - - - 1'''
print("third pattern ")

for i in range(6, 1, -1):
    for k in range(1, 7 - i):
        print("-", end=" ")
    for j in range(1, i,1):
        print(j, end="")
    print()

'''1
23
456
78910'''
print("fourth pattern ")

k = 1
for i in range(1, 5,1):
    for j in range(1,i+1,1):
        print(k, end="")
        k += 1
    print()
'''
----*
---***
--*****
-*******
*********'''
print("fift pattern ")

a = 10
for p in range(1, 2*a, 2):
    for k in range(a, 1, -1):
        print("-", end="")
    a -= 1
    for m in range(0, p, 1):
        print("*", end="")
    print()

print("sixth pattern ")
'''----1
---123
--12345
-1234567
123456789'''
d=5
for p in range(1, 2 * d, 2):
    for k in range(d, 1, -1):
        print("-", end="")
    d -= 1
    for m in range(1, p+1, 1):
        print(m, end="")
    print()

'''----*
---***
--*****
-*******
*********
*******
******
-*****
--****
---***
----**
-----*'''
print("seventh pattern ")
b=5
for i in range(1,2*b,2):
    for k in range(b,1,-1):
        print("-",end="")
    b-=1
    for j in range(1,i+1,1):
        print("*",end="")
    print()
e=7
h=8
for i in range(1,e*2,2):
    for k in range(1,7-e,1):
        print("-",end="")
    for j in range(h,1,-1):
        print("*",end="")
    h-=1
    e-=1
    print()