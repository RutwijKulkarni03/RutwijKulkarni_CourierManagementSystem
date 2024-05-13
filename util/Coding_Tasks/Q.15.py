'''15. Find Similar Addresses: Implement a function that finds similar addresses in the system. This can be
useful for identifying duplicate customer entries or optimizing delivery routes. Use string functions to
implement this.'''

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

# Function to find similar addresses in the system
def find_similar_addresses():
    query = "SELECT SenderAddress FROM Courier"
    addresses = execute_query(query)

    if addresses:
        similar_addresses = set()
        for address in addresses:
            address_str = address[0].lower()  # Convert to lowercase for case-insensitive comparison
            similar_addresses.add(address_str)

        return similar_addresses
    else:
        print("No addresses found in the system.")
        return None

# Example usage:
similar_addresses = find_similar_addresses()
if similar_addresses:
    print("Similar Addresses in the System:")
    for address in similar_addresses:
        print(address)
