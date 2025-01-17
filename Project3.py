import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr")
mycursor=mydb.cursor()

id=input("Enter your id")

mycursor.execute("DELETE FROM library WHERE book_id = %s", (id,))
mydb.commit()