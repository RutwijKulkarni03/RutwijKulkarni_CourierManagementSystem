import mysql.connector

class DBConnection:
    @staticmethod
    def get_connection():
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='rutwij123',
                port=3306,
                database='courier_management_system'
            )
            print("Connected to the database successfully.")
            return connection
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")
            return None
