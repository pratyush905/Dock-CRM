import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'password'
)

cursorObject = dataBase.cursor()

cursorObject.execute(" CREATE DATABASE crm_database")

print("All Done!!!")