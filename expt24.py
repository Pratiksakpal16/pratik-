n=500
e=20
f=15
g=30
h=5
i=25
j=10
k=40
l=50
m=35
def snacks():
    snack=["lays-20","cheetos-15","balaji-30"]
    print(snack)
    a=input()
    if(a=='1'):
        print("your choice is lays and your balance is",n-e)
    elif(a=='2'):
        print("your choice is cheetos and your balance is",n-f)
    elif(a=='3'):
        print("your choice is balaji and your balance is",n-g)
def drinks():
    drink=["water-5","cocacola-25","pepsi-10"]
    print(drink)
    b=input()
    if(b=='1'):
        print("your choice is water and your balance is",n-h)
    elif(b=='2'):
        print("your choice is cocacola and your balance is",n-i)
    elif(b=='3'):
        print("your choice is pepsi and your balance is",n-j)
def lunchs():
    lunch=["idli-40","dosa-50","vadapav-35"]
    print(lunch)
    d=input()
    if(d=='1'):
        print("your choice is idli and your balance is",n-k)
    elif(d=='2'):
        print("your choice is dosa and your balance is",n-l)
    elif(d=='3'):
        print("your choice is vadapav and your balance is",n-m)
m='y'
while(m=='y'):
    print("Enter the item you want:")
    print("press 1 for snacks")
    print("press 2 for drinks")
    print("press 3 for lunchs")
    c=input()
    if(c=='1'):
        snacks()
    elif(c=='2'):
        drinks()
    elif(c=='3'):
        lunchs()
    else:
        print("Error")
    m=input("if you want to continue press y or press n:")
