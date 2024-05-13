'''3. Implement User Authentication 1. Create a login system for employees and customers using Java/Python
control flow statements.'''

# Import the necessary module for database connection
import mysql.connector

# Define the function to authenticate users
def authenticate_user(user_type, username, password):
    # Database connection parameters
    # Replace the placeholders with your actual database credentials
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'rutwij123',
        'database': 'courier_management_system'
    }

    # Establish a connection to the database
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Check user type and query the database accordingly
        if user_type == 1:  # Employee
            query = "SELECT Username, Password FROM Employee WHERE Username = %s AND Password = %s"
        elif user_type == 2:  # Customer
            query = "SELECT Username, Password FROM Customers WHERE Username = %s AND Password = %s"
        else:
            return "Invalid user type selection."

        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        # Check if the user exists in the database
        if result:
            if user_type == 1:
                return "Employee login successful!"
            elif user_type == 2:
                return "Customer login successful!"
        else:
            return "Invalid credentials. Please try again."

    except mysql.connector.Error as error:
        return "Error connecting to the database: {}".format(error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main function to handle user input and authentication
def main():
    print("Welcome to the User Authentication System")

    # Prompt user to select user type
    print("Select user type:")
    print("1. Employee")
    print("2. Customer")
    user_type = int(input())
    if user_type not in [1, 2]:
        print("Invalid user type selection.")
        return

    # Prompt user for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Authenticate the user
    result = authenticate_user(user_type, username, password)
    print(result)

# Execute the main function
if __name__ == "__main__":
    main()
