import mysql.connector as c
mydb=c.connect(
    host="localhost",
    user="root",
    password="1234",
    database="cvr")
mycursor=mydb.cursor()
mycursor.execute("""
CREATE TABLE library (
book_id INT ,
title VARCHAR(100),
author VARCHAR(100)
)
""")