def primecheck(a):
    for i in range(2, a):
        if a % i == 0:
            return  a,"is not a prime"
            break
    else:
        return  a,"is a prime"

print (primecheck(45))

def countstring():
    str=input("enter string ")
    new_str=str.replace(" ","")
    print("without spaces",new_str)
    print(len(new_str))

        
countstring();