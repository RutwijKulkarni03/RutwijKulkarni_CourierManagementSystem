import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='courier_management_system'
)

mycursor = mydb.cursor()

def insert_location():
    location_id = input("Enter LocationID: ")
    location_name = input("Enter LocationName: ")
    address = input("Enter Address: ")

    sql = "INSERT INTO location (LocationID, LocationName, Address) VALUES (%s, %s, %s)"
    val = (location_id, location_name, address)

    try:
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except mysql.connector.Error as err:
        mydb.rollback()
        print("Error inserting data into location table:", err)

insert_location()
mycursor.close()
mydb.close()
