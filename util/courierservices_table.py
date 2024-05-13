import mysql.connector

def insert_courier_services():
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rutwij123',
        port='3306',
        database='courier_management_system'
    )

    mycursor = mydb.cursor()

    service_id = input("Enter Service ID: ")
    service_name = input("Enter Service Name: ")
    cost = float(input("Enter Cost: "))

    sql = "INSERT INTO courierservices (ServiceID, ServiceName, Cost) VALUES (%s, %s, %s)"
    val = (service_id, service_name, cost)

    try:
        # Loop to insert data into the 'courierservices' table
        #for _ in range(1):

        mycursor.execute(sql, val)

        mydb.commit()

        print("Data inserted successfully into the 'courierservices' table.")

    except mysql.connector.Error as err:
        print("Error inserting data into courierservices table:", err)

    finally:
        mycursor.close()
        mydb.close()

insert_courier_services()
