
import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr")
mycursor=mydb.cursor()
name=input("Enter your name")
id=input("Enter your id")
aname=input("enter aname")
mycursor.execute("insert into library values(%s,%s,%s)",(id,name,aname))
mydb.commit()