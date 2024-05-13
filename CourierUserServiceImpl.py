import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\dao")
from ICourierUserService import ICourierUserService
class CourierUserServiceImpl(ICourierUserService):
    def __init__(self):
        CourierUserServiceImpl.connection = DBConnection.getConnection()

    def place_order(self):
        pass

    def get_order_status(self, order_id):
        pass

    def cancel_order(self, order_id):
        pass

    def get_assigned_orders(self, user_id):
        pass


