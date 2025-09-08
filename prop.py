import math
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
print(mul())