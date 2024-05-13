'''6. Implement a while loop to track the real-time location of a courier until it reaches its destination.'''

from datetime import datetime
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

# Function to track real-time location of a courier
def track_courier():
    courier_id = input("Enter the CourierID: ")
    query = "SELECT * FROM location WHERE CourierID = %s ORDER BY Timestamp ASC"
    while True:
        locations = execute_query(query, (courier_id,))
        if locations:
            print("Current location of courier:")
            print(locations[-1])  # Display the latest location
            latest_location_timestamp = locations[-1][4]  # Assuming timestamp is the fifth attribute in the tuple
            latest_location_datetime = datetime.strptime(latest_location_timestamp,
                                                         '%Y-%m-%d %H:%M:%S')  # Convert timestamp to datetime

            today_date = datetime.now().date()  # Get today's date
            if latest_location_datetime.date() > today_date:
                print("Courier will reach its destination.")
            else:
                print("Courier has reached its destination.")
                break
        else:
            print("No location data available for the courier.")
            break

# Example usage:
track_courier()
