import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\exception")
from InvalidEmployeeIdException import InvalidEmployeeIDException

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    database='courier_management_system'
)

mycursor = mydb.cursor()

def insert_employee():
    try:
        while True:
            employee_id = input("Enter Employee ID: ")
            try:
                employee_id = int(employee_id)
                break
            except ValueError:
                raise InvalidEmployeeIDException(employee_id)
    except InvalidEmployeeIDException as e:
        print(str(e))
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    contact_number = input("Enter Contact Number: ")
    role = input("Enter Role: ")
    salary = float(input("Enter Salary: "))

    sql_query = "INSERT INTO employee (EmployeeID, Name, Email, ContactNumber, Role, Salary) VALUES (%s, %s, %s, %s, %s, %s)"
    values = (employee_id, name, email, contact_number, role, salary)

    try:
        mycursor.execute(sql_query, values)
        mydb.commit()
        print("Employee data inserted successfully!")
    except mysql.connector.Error as err:
        mydb.rollback()
        print(f"Error inserting data into employee table: {err}")

    finally:
        if mydb is not None:
            mydb.close()


if __name__ == "__main__":
    insert_employee()
    mydb.close()


