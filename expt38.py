import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password123",database="school")
mycursor=mydb.cursor()
for i in mycursor:
    print(i)
m='y'
while(m=='y' or m=='Y'):
        print("Press 1 to show databases:")
        print("Press 2 to show description of table:")
        print("Press 3 to show table contents:")
        c=input("Enter your option:")
        if(c=='1'):
           mycursor=mydb.cursor()
           mycursor.execute("show databases")
           for i in mycursor:
               print(i)
        elif(c=='2'):
            mycursor=mydb.cursor()
            mycursor.execute("desc staff")
            for i in mycursor:
                print(i)
        elif(c=='3'):
            mycursor=mydb.cursor()
            mycursor.execute("select * from staff")
            for i in mycursor:
                print(i)
        else:
            print("error")
        m=input("press Y or y to continue or press n to stop:")

