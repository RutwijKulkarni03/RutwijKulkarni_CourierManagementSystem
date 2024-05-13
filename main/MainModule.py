import mysql.connector

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\dao")
from ICourierUserService import ICourierUserService

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\dao")
from ICourierAdminService import ICourierAdminService

class MainModule(ICourierUserService, ICourierAdminService):
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rutwij123',
            port='3306',
            database='courier_management_system'
        )
        self.mycursor = self.mydb.cursor()

    def display_menu(self):
        print("Welcome to Courier Management System Menu...")
        print("1. Place a new courier order")
        print("2. Get the status of a courier order")
        print("3. Cancel a courier order")
        print("4. Get a list of orders assigned to a specific courier staff member")
        print("5. Add a new courier staff member to the system.")
        print("6. Exit")

    def start_application(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            if choice == "1":
                self.place_order()
            elif choice == "2":
                self.get_order_status()
            elif choice == "3":
                self.cancel_order()
            elif choice == "4":
                self.get_assigned_orders()
            elif choice == "5":
                self.add_courier_staff()
            elif choice == "6":
                print("Exiting the application...")
                break
            else:
                print("Invalid choice. Please try again.")

            break

    def place_order(self):
        print("Placing a new courier order...")

        customer_id = input("Enter CustomerID: ")
        name = input("Enter Name: ")
        email = input("Enter Email id: ")
        contact_number = input("Enter Contact Number: ")
        address = input("Enter Address: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        try:
            self.mycursor.execute("""
                INSERT INTO customers (CustomerID, Name, Email, ContactNumber, Address, Username, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (customer_id, name, email, contact_number, address, username, password))

            self.mydb.commit()

            print("Courier order placed successfully!")
        except Exception as e:
            print("Failed to place courier order:", e)

    def get_order_status(self):
        order_id = input("Enter the order ID: ")
        print(f"Getting status of courier order {order_id}...")

        try:
            self.mycursor.execute("""
                SELECT Status FROM orders WHERE OrderID = %s
            """, (order_id,))
            result = self.mycursor.fetchone()
            if result:
                status = result[0]
                print(f"The status of courier order {order_id} is: {status}")
            else:
                print(f"No courier order found with ID {order_id}")
        except Exception as e:
            print("Failed to get order status:", e)

    def cancel_order(self):
        order_id = input("Enter the order ID to cancel: ")
        print(f"Canceling courier order {order_id}...")

        try:
            self.mycursor.execute("""
                DELETE FROM customers WHERE CustomerID = %s
            """, (order_id,))
            self.mydb.commit()

            print(f"Courier order {order_id} canceled successfully!")
        except Exception as e:
            print("Failed to cancel courier order:", e)

    def get_assigned_orders(self):
        user_id = input("Enter the user ID: ")
        print(f"Getting list of orders assigned to user {user_id}...")

        try:
            self.mycursor.execute("""
                SELECT * FROM orders WHERE UserID = %s
            """, (user_id,))
            results = self.mycursor.fetchall()

            if results:
                print("Orders assigned to user:")
                for result in results:
                    print(result)  # Adjust printing according to your database schema
            else:
                print(f"No orders found for user {user_id}")
        except Exception as e:
            print("Failed to get assigned orders:", e)

    def add_courier_staff(self):
        employee_id = input("Enter the Employee ID: ")
        name = input("Enter the Name: ")
        email = input("Enter the Email: ")
        contact_number = input("Enter the Contact Number: ")
        role = input("Enter the Role: ")
        salary = input("Enter the Salary: ")
        username = input("Enter the Username: ")
        password = input("Enter the Password: ")
        print("Adding a new courier staff member...")
        try:
            self.mycursor.execute("""
                INSERT INTO employee (EmployeeID, Name, Email, ContactNumber, Role, Salary, Username, Password)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, (employee_id, name, email, contact_number, role, salary, username, password))
            print("Courier staff member added successfully!")
        except Exception as e:
            print("Failed to add courier staff member:", e)

if __name__ == "__main__":
    main_module = MainModule()
    main_module.start_application()
