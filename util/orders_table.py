import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port=3306,
    database='courier_management_system'
)

mycursor = mydb.cursor()

order_id = input("Enter OrderID: ")
customer_id = input("Enter CustomerID: ")
order_date = input("Enter OrderDate (YYYY-MM-DD): ")

query = "INSERT INTO orders (OrderID, CustomerID, OrderDate) VALUES (%s, %s, %s)"

mycursor.execute(query, (order_id, customer_id, order_date))

mydb.commit()

print(mycursor.rowcount, "record inserted.")
