# wap to count given of any string
# wap countspace of given of any string
# wap to print given string in sentence case
# wap print reverse given of any string
# wap count vowels and consonents
# wap count word of given any string
# wap find words in any string
# print shortcut charter given of any string
print("QUETION1 ...........")
string = input('enter string to count')
print(len(string))
space = " "
print("spacecount", string.count(space))
print("in sentace case ", string.capitalize())
print("reverse of string", string[::-1])
vowels = 0
con = 0
string_lower=string.lower()
for i in range(len(string_lower)):
    if (string_lower[i]=="a" or string_lower[i]=="i" or string_lower[i]=="o" or string_lower[i]=="u" or string_lower[i]=="e" ):
        vowels = vowels+1
    else:
        con = con+1

print("vowels in string", vowels)
print("consonents", con)

word= input("enter the word you wanna find in given string")
print("found ",string.find(word))
print("counted",string.count(word))
print(string[0],end="")
case=" "
for i in range(len(string)):
    if(string[i]==space):
        case=string[i+1]
        print(case,end="")