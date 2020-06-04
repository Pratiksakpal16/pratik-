import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password123",database="school")
mycursor=mydb.cursor()
for i in mycursor:
    print(i)
a=input("Enter your name:")
b=int(input("Enter your idno:"))
c=int(input("Enter your phoneno:"))
d=input("Enter your empwork:")
mycursor=mydb.cursor()
mycursor.execute("insert into staff values('{}',{},{},'{}')".format(a,b,c,d))
mydb.commit()
mydb.close()
for i in mycursor:
    print(i)
    
