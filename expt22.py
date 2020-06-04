def pin():
    x=int(input("Enter Pin:"))
    if(x==1234):
        atm()
    else:
        verifypin()
trials=1
def atm():
    a=50000
    m='y'
    while(m=='y'):
            print("Welcome to ATM")
            print("Select the below option to continue:")
            print("press 1 to check the balance")
            print("press 2 to deposit money")
            print("press 3 to withdraw")
            c=input()
            if(c=='1'):
             print("Balance is:",a)
            elif(c=='2'):
             b=int(input("enter the amount to deposit:"))
             print("New Balance is",a+b)
            elif(c=='3'):
             c=int(input("enter the amount to withdraw:"))
             print("New Balance is",a-c)
            else:
             print("Error")
            m=input("Do you want to continue press y to stop press n:")

 
def verifypin():
    while(trials<3):
        p=1234
        if(p!=1234):
            print("wrong pin enter your pin again:")
verifypin()               
       
