import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port=3306,
    database='courier_management_system'
)

mycursor = mydb.cursor()

customer_id = input("Enter CustomerID: ")
order_id = input("Enter OrderID: ")
name = input("Enter Name: ")
email = input("Enter Email: ")
contact_number = input("Enter ContactNumber: ")
address = input("Enter Address: ")

query = "INSERT INTO customer (CustomerID, OrderID, Name, Email, ContactNumber, Address) VALUES (%s, %s, %s, %s, %s)"

mycursor.execute(query, (customer_id, order_id, name, email, contact_number, address))

mydb.commit()

print(mycursor.rowcount, "record inserted.")
