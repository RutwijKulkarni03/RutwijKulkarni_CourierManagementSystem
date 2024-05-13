import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\util")
import mysql.connector

class PropertyUtil:
    @staticmethod
    def get_parameters():
        host = input("Enter host: ")
        database = input("Enter database: ")
        user = input("Enter user: ")
        password = input("Enter password: ")
        return host, database, user, password

class DBConnUtil:
    @staticmethod
    def make_connection():
        host, database, user, password = PropertyUtil.get_parameters()
        try:
            mydb = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            print("Connection established successfully!")
            return mydb
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            return None

if __name__ == "__main__":
    conn = DBConnUtil.make_connection()
    if conn:
        conn.close()
