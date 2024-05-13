'''7. Create an array to store the tracking history of a parcel, where each entry represents a location
update.'''

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


# Function to create an array to store tracking history of a parcel
def create_tracking_history(parcel_id):
    query = "SELECT * FROM Parcels WHERE ParcelID = %s"
    parcel_info = execute_query(query, (parcel_id,))

    if parcel_info:
        tracking_history = []
        print(f"Tracking history for parcel with ID {parcel_id}:")

        # Assuming the order of attributes in the result is [Location, Status, Timestamp]
        for info in parcel_info:
            tracking_history.append({
                "Location": info[1],
                "Status": info[2],
                "Timestamp": info[3]
            })

        for entry in tracking_history:
            print(entry)
    else:
        print(f"No information found for parcel with ID {parcel_id}.")


# Prompt user to enter the parcel ID
parcel_id = input("Enter the parcel ID: ")
create_tracking_history(parcel_id)
