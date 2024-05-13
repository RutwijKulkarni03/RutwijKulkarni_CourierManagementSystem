'''5. Write a Java program that uses a for loop to display all the orders for a specific customer.'''

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

# Function to display orders for a specific customer
def display_customer_orders():
    customer_id = input("Enter the customer ID: ")
    query = "SELECT * FROM Orders WHERE CustomerID = %s"
    orders = execute_query(query, (customer_id,))

    if orders:
        print(f"Orders for customer with ID {customer_id}:")
        for order in orders:
            print(order)
    else:
        print("No orders found for the customer.")


# Example usage:
display_customer_orders()
