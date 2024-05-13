'''4. Implement Courier Assignment Logic 1. Develop a mechanism to assign couriers to shipments based
on predefined criteria (e.g., proximity, load capacity) using loops.'''

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


# Define the function to assign couriers to shipments
def assign_couriers(criteria):
    # Fetch relevant data from the database based on the criteria
    query = "SELECT * FROM Courier WHERE " + criteria
    couriers = execute_query(query)

    # Implement assignment logic using loops
    for courier in couriers:
        # Implement assignment logic here based on proximity, load capacity, etc.
        # Example:
        print("Assigning courier:", courier)


# Example usage:
criteria = "Proximity = 'Nearby' AND LoadCapacity >= 10"
assign_couriers(criteria)
