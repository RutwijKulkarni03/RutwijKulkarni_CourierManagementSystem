'''
9. Parcel Tracking: Create a program that allows users to input a parcel tracking number.Store the
tracking number and Status in 2d String Array. Initialize the array with values. Then, simulate the
tracking process by displaying messages like "Parcel in transit," "Parcel out for delivery," or "Parcel
delivered" based on the tracking number's status.
'''

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


# Function to simulate parcel tracking process
def track_parcel(tracking_number, tracking_array):
    for parcel in tracking_array:
        if parcel[0] == tracking_number:
            status = parcel[1]
            if status == "In Transit":
                print("Parcel in transit")
            elif status == "Out for Delivery":
                print("Parcel out for delivery")
            elif status == "Delivered":
                print("Parcel delivered")
            else:
                print("Invalid status")
            return
    print("Tracking number not found")


# Function to initialize the tracking array with values from the database
def initialize_tracking_array():
    query = "SELECT TrackingNumber, Status FROM Parcels"
    results = execute_query(query)
    tracking_array = []
    if results:
        for row in results:
            tracking_array.append([row[0], row[1]])
    return tracking_array


# Function to get input from user
def get_tracking_number():
    return input("Enter the parcel tracking number: ")


# Main function
def main():
    tracking_array = initialize_tracking_array()
    if not tracking_array:
        print("No parcels found in the database")
        return

    tracking_number = get_tracking_number()
    track_parcel(tracking_number, tracking_array)


if __name__ == "__main__":
    main()
