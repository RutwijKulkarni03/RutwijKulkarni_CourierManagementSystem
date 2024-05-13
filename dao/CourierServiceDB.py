import mysql.connector

import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\dao")
from DBConnection import DBConnection

class CourierServiceDb:
    connection = None

    def __init__(self):
        self.connection = DBConnection.get_connection()

courier_service_db = CourierServiceDb()

connection = courier_service_db.connection
