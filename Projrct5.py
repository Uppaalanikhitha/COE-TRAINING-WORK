import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr")
mycursor=mydb.cursor()
mycursor.execute("select * from library")
library=mycursor.fetchall();
for book_id in library:
    print(book_id)
mydb.commit()