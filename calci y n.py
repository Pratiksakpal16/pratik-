m='y'
while(m=='y' or m=='Y'):
        a=int(input("enter first number:"))
        b=int(input("enter second number:"))
        print("for addition press +")
        print("for subtraction press -")
        print("for multiplication press *")
        print("for divison press/")
        print("for modulus press %")      
        c=input()
        if(c=='+'):
           print(a+b)
        elif(c=='-'):
            print(a-b)
        elif(c=='*'):
            print(a*b)
        elif(c=='/'):
            print(a/b)
        elif(c=='%'):
            print(a%b)
        else:
            print("error")
        m=input("press Y or y to continue or press n to stop:")
