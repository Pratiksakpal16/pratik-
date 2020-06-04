import tablencalci
x='y'
while(x=='y'):
    print("Press 1 to get Table")
    print("Press 2 to get Calculator")
    a=int(input())
    if(a==1):
        tablencalci.table()
        x=input("To continue press y or to stop press n:")
    elif(a==2):
        tablencalci.calculator()
        x=input("press Y or y to continue or press n to stop:")


