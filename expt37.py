import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="password123",database="school")
mycursor=mydb.cursor()
mycursor.execute("insert into staff values('adas',13,12,'adasdas')")
mydb.commit()
mydb.close()
for i in mycursor:
    print(i)
