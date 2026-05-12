import mysql.connector

def get_db():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kali@0609",
        database="school"
    )
    return db

