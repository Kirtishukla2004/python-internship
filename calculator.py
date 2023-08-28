def sum(a, b):
    s = a+b
    return s


def sub(a, b):
    s = a-b
    return s


def div(a, b):
    s = a/b
    return s


def mul(a, b):
    s = a*b
    return s


def dividend(a, b):
    s = a % b
    return s


def main():
    choice = input(
        "enter what operation you want to run enter +,-,*,/,%, space for all function")
    a = int(input("enter first digit"))
    b = int(input("enter second digit"))
    if (choice == '+'):
        print("sum", sum(a, b))
    elif (choice == '-'):
        print("subtract", sub(a, b))
    elif (choice == '*'):
        print("multiply", mul(a, b))
    elif (choice == '/'):
        print("divide", div(a, b))
    elif (choice == "%"):
        print("dividend", dividend(a, b))
    elif (choice == " "):
        print("sum", sum(a, b))
        print("subtract", sub(a, b))
        print("multipky", mul(a, b))
        print("divide", div(a, b))
        print("dividend", dividend(a, b))
    else:
        print("WRONG INPUT.....")
