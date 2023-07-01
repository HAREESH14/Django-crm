import mysql.connector as con
dataBase=con.connect(
    host="127.0.0.1",
    user="root",
    password="wcchj85rxu"
)
mycursor = dataBase.cursor()

mycursor.execute("CREATE DATABASE haridata")
