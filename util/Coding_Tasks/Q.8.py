''' 8. Implement a method to find the nearest available courier for a new order using an array of couriers.
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

# Function to calculate distance between two points
def calculate_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Function to find the nearest available courier for a new order
def find_nearest_courier(new_order_location):
    query = "SELECT * FROM Courier WHERE Availability = 'Available'"
    couriers = execute_query(query)

    if couriers:
        nearest_courier = None
        min_distance = float('inf')

        for courier in couriers:
            courier_id = courier[0]
            courier_location = (courier[1], courier[2])
            distance = calculate_distance(new_order_location[0], new_order_location[1], courier_location[0], courier_location[1])

            if distance < min_distance:
                nearest_courier = courier_id
                min_distance = distance

        return nearest_courier
    else:
        print("No available couriers found.")
        return None

# Function to get location for new order from user input
def get_new_order_location():
    try:
        x = float(input("Enter the x-coordinate for the new order: "))
        y = float(input("Enter the y-coordinate for the new order: "))
        return x, y
    except ValueError:
        print("Invalid input. Please enter numeric values for coordinates.")
        return None

# Example usage:
def main():
    new_order_location = get_new_order_location()
    if new_order_location:
        nearest_courier = find_nearest_courier(new_order_location)
        if nearest_courier:
            print(f"The nearest available courier for the new order is Courier ID {nearest_courier}.")

if __name__ == "__main__":
    main()
