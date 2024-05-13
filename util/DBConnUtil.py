import mysql.connector

def connect_to_mysql(host='localhost', user='root', password='rutwij123', port=3306, database='courier_management_system'):

    try:
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='rutwij123',
            port=3306,
            database='courier_management_system'
        )
        print("Connected to the database successfully.")
        return mydb
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

connect_to_mysql()
