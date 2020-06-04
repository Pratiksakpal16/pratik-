def vendingmachine():
     a=500
     m='y'
     while(m=='y'):
        print("Main Menu")
        print("press 1 for lays=10")
        print("press 2 for chocolate=20")
        print("press 3 for biscuits=10")
        print("press 4 for cola=20")
        print("press 5 for soda=20")
        c=input()
        if(c=='1'):
            print("Balance is:",a-10)
        elif(c=='2'):
            print("Balance is:",a-20)
        elif(c=='3'):
            print("Balance is:",a-10)
        elif(c=='4'):
            print("Balance is:",a-20)
        elif(c=='5'):
            print("Balance is:",a-20)
        else:
            print("Error")
        m=input("If you want to continue Press y or to exit Press n:")
vendingmachine()
            
            
        
