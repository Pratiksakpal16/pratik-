try:
    a=input("Enter First Name:")
    b=input("Enter Last Name:")
    c=int(input("Enter Age:"))
    d=input("Enter PhoneNo:")
    if(c<18):
        raise Exception("Please enter the age above 18")
    if((len(d)<10)):
        raise Exception("Please insert valid phone number")
except Exception as e:
    print(e.__class__)
