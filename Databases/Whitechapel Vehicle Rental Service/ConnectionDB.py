import mysql.connector

def ConnectionDB():
    Connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="WhitechapelVehicleRentalService"
    )
    return Connection
