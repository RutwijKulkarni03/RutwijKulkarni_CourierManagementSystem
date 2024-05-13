import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\exception")
from TrackingNumberNotFoundException import TrackingNumberNotFoundException

import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='rutwij123',
    database='courier_management_system'
)

mycursor = mydb.cursor()

parcel_id = input("Enter ParcelID: ")
order_id = input("Enter OrderID: ")
sender_name = input("Enter SenderName: ")
sender_address = input("Enter SenderAddress: ")
receiver_name = input("Enter ReceiverName: ")
receiver_address = input("Enter ReceiverAddress: ")
weight = input("Enter Weight: ")
status = input("Enter Status: ")
tracking_number = input("Enter TrackingNumber: ")
delivery_date = input("Enter DeliveryDate (YYYY-MM-DD): ")

query = "INSERT INTO parcels (ParcelID, OrderID, SenderName, SenderAddress, ReceiverName, ReceiverAddress, Weight, Status, TrackingNumber, DeliveryDate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

mycursor.execute(query, (parcel_id, order_id, sender_name, sender_address, receiver_name, receiver_address, weight, status, tracking_number, delivery_date))

mydb.commit()

print(mycursor.rowcount, "record inserted.")
