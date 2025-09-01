import mysql.connector

def ConnectionDB():
    Connection = mysql.connector.connect(
        host="Your Ip or Localhost",
        user="Your username",
        password="Your password",
        database="Database Name"
    )
    return Connection
