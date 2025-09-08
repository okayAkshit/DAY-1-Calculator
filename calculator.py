import math

def main():
    print("choose the number as per requirment")
    print("\n1. ADD\n2. Subtract\n3. divide\n4. multiply\n5. reminder\n6 Exit")
def add():
    a=[]
    print("enter the numbers you one by one anad when wanna stop just type'stop")
    while True:
        element=input("enter elements")
        if element.lower()=="stop":
            break
        try:
            n=list(map(int,element.split()))
            a.extend(n)
        except:
            print("enter thge valid number")
        return(sum(a))
def sub():
     a=int(input("enter the first number"))
     b=int(input("enter the second number"))
     return(a-b)
def mul():
        a=[]
        print("enter the numbers you one by one anad when wanna stop just type'stop")
        while True:
            element=input("enter elements")
            if element.lower()=="stop":
                break
            try:
                n=list(map(int,element.split()))
                a.extend(n)
                
            except:
                print("enter thge valid number")
            return(math.prod(a))
def rem():
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    return(a%b)
def div():
    a=int(input("enter the first number"))
    b=int(input("enter the second number"))
    return(a/b)



while True:
    main()
    choice=int(input("enter the no you wanna perform:"))
    try:


        if choice==1:
            print(add())

        if choice==2:
            print(sub())
        elif choice==3:
            print(div())
        elif choice==4:
            print(mul())
        elif choice==5:
            print(rem())
        elif choice==6:
            print("good bye")
            break
    except:
        print("enter a valid number")





