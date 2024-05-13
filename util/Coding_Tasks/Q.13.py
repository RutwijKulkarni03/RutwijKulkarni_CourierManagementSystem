'''
13. Calculate Shipping Costs: Develop a function that calculates the shipping cost based on the distance
between two locations and the weight of the parcel. You can use string inputs for the source and
destination addresses.
'''

import mysql.connector
from math import sqrt

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

# Function to calculate distance between two locations
def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to calculate shipping cost
def calculate_shipping_cost(source_coords, destination_coords, weight):
    distance = calculate_distance(source_coords[0], source_coords[1], destination_coords[0], destination_coords[1])

    shipping_cost = distance * weight * 0.1  # Example formula for shipping cost calculation

    return shipping_cost

# Example usage:
def main():
    source_x = float(input("Enter source X-coordinate: "))
    source_y = float(input("Enter source Y-coordinate: "))
    destination_x = float(input("Enter destination X-coordinate: "))
    destination_y = float(input("Enter destination Y-coordinate: "))
    weight = float(input("Enter parcel weight (in kg): "))

    source_coords = (source_x, source_y)
    destination_coords = (destination_x, destination_y)

    shipping_cost = calculate_shipping_cost(source_coords, destination_coords, weight)
    if shipping_cost is not None:
        print("Shipping cost:", shipping_cost)
    else:
        print("Failed to calculate shipping cost.")

if __name__ == "__main__":
    main()
