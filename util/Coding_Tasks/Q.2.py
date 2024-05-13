'''2. Implement a switch-case statement to categorize parcels based on their weight into "Light,"
"Medium," or "Heavy." '''

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

# Define the function to categorize parcels based on their weight
def categorize_parcel(weight):
    category = {
        0: "Light",
        1: "Medium",
        2: "Heavy"
    }
    if 0 <= weight < 5:
        return category[0]
    elif 5 <= weight < 10:
        return category[1]
    elif weight >= 10:
        return category[2]
    else:
        return "Invalid weight"

# Get the weight of the parcel from the user
parcel_id = input("Enter the parcel ID: ")
query = "SELECT Weight FROM Parcels WHERE ParcelID = %s"
result = execute_query(query, (parcel_id,))
if result:
    parcel_weight = result[0][0]  # Extract weight from the result
    parcel_category = categorize_parcel(parcel_weight)
    print("The parcel is categorized as:", parcel_category)
else:
    print("Parcel ID not found.")
