'''1. Write a program that checks whether a given order is delivered or not based on its status (e.g.,
"Processing," "Delivered," "Cancelled"). Use if-else statements for this.'''

import mysql.connector

# Function to establish connection to MySQL database
def connect_to_mysql():
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="rutwij123",
            database="courier_management_system"
        )
        print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print("Error connecting to MySQL database:", err)
        return None

# Function to execute SQL queries
def execute_query(query, params=None):
    connection = None
    try:
        connection = connect_to_mysql()
        if connection:
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.commit()
            return result
        else:
            print("Connection failed.")
            return None
    except mysql.connector.Error as err:
        print("Error executing query:", err)
        return None
    finally:
        if connection:
            connection.close()

# Define the function to check order status
def check_order_status(order_id):
    # SQL query to fetch the order status based on order ID
    query = "SELECT Status FROM Orders WHERE OrderID = %s"
    result = execute_query(query, (order_id,))
    if result:
        status = result[0][0]  # Extract status from the result
        if status == "Delivered":
            print("The order is delivered.")
        elif status == "Processing":
            print("The order is still processing.")
        elif status == "Cancelled":
            print("The order is cancelled.")
        else:
            print("Invalid status. Please provide a valid order status.")
    else:
        print("Order ID not found.")

# Get the order ID from the user
order_id = input("Enter the order ID: ")
# Check the order status
check_order_status(order_id)
