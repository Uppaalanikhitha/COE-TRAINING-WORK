import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr")
mycursor=mydb.cursor()
name=input("Enter your name")
id=input("Enter your id")
mycursor.execute("UPDATE library SET title= %s WHERE book_id = %s", (name, id))

mydb.commit()