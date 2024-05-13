import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='courier_management_system'
)

mycursor = mydb.cursor()

payment_id = int(input("Enter PaymentID: "))
courier_id = int(input("Enter CourierID: "))
location_id = int(input("Enter LocationID: "))
amount = float(input("Enter Amount: "))
payment_date = input("Enter PaymentDate (YYYY-MM-DD): ")

sql_query = f"INSERT INTO payment (PaymentID, CourierID, LocationID, Amount, PaymentDate) VALUES ({payment_id}, {courier_id}, {location_id}, {amount}, '{payment_date}')"

try:
    mycursor.execute(sql_query)
    mydb.commit()
    print("Data inserted successfully.")
except mysql.connector.Error as err:
    print(f"Error inserting data into payment table: {err}")


mycursor.close()
mydb.close()
