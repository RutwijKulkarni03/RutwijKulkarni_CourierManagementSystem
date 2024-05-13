import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\exception")
from TrackingNumberNotFoundException import TrackingNumberNotFoundException

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    port='3306',
    database='courier_management_system'
)

mycursor = mydb.cursor()

def insert_tracking_number():
    try:
        while True:
            tracking_number = input("Enter Tracking Number: ")
            if len(tracking_number) != 6:
                raise TrackingNumberNotFoundException("Tracking number must be 6 characters long.")
            break
    except TrackingNumberNotFoundException as e:
        print(str(e))
        return tracking_number

tracking_number = insert_tracking_number()

courier_id = int(input("Enter CourierID: "))
location_id = int(input("Enter LocationID: "))
user_id = int(input("Enter UserID: "))
employee_id = int(input("Enter EmployeeID: "))
sender_name = input("Enter SenderName: ")
sender_address = input("Enter SenderAddress: ")
receiver_name = input("Enter ReceiverName: ")
receiver_address = input("Enter ReceiverAddress: ")
weight = float(input("Enter Weight: "))
status = input("Enter Status: ")
delivery_date = input("Enter DeliveryDate (YYYY-MM-DD): ")
proximity = input("Enter Proximity: ")
load_capacity = input("Enter Load Capacity: ")
availability = input("Enter Availability: ")


sql = "INSERT INTO courier (CourierID, LocationID, UserID, EmployeeID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate, Proximity, LoadCapacity, Availability) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
val = (courier_id, location_id, user_id, employee_id, sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, delivery_date, proximity, load_capacity, availability)

try:
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Record inserted successfully.")
except mysql.connector.Error as err:
    mydb.rollback()
    print("Error inserting data into courier table:", err)

if __name__ == "__main__":
    insert_tracking_number()
    mydb.close()
