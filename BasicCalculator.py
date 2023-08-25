def addition(a,b):
    answer=a+b
    print  (f"{a}+{b}={answer}")

def subtraction(a,b):
    answer=a-b
    print  (f"{a}-{b}={answer}")

def multiplication(a,b):
    answer=a*b
    print  (f"{a}X{b}={answer}")

def division(a,b):
    answer=a/b
    print (f"{a}/{b}={answer}")

while True:
    print("A.ADDITION")
    print("B.SUBTRACTION")
    print("C.MULTIPLICATION")
    print("D.DIVISION")
    print("E.EXIT")

    choice=input("Enter your choice:")

    if choice=='a'or choice=='A':
       print("ADDITION")
       a=int(input("Enter first number:"))
       b=int(input("Enter second number:"))
       addition(a,b)
    elif choice=='b'or choice=='B':
       print("SUBTRACTION")
       a=int(input("Enter first number:"))
       b=int(input("Enter second number:"))
       subtraction(a,b)
    elif choice=='c'or choice=='C':
       print("MULTIPLICATION")
       a=int(input("Enter first number:"))
       b=int(input("Enter second number:"))
       multiplication(a,b)
    elif choice=='d'or choice=='D':
       print("DIVISION")
       a=int(input("Enter first number:"))
       b=int(input("Enter second number:"))
       division(a,b)
    elif choice=='e'or choice=='E':
       print("Calcualtor switching off...")
       quit()
    else:
        print("Wrong Choice")
