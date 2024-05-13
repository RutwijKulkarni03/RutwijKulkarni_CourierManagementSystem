from ICourierUserService import ICourierUserService
import sys
sys.path.append(r"D:\RUTWIJ DATA\MIT ADT - CSE Notes\HEXAWARE TECHNOLOGIES\Foundational Technical Training\Assignment - Courier Management System\CourierManagementSystem\entity")
from CourierCompanyCollection import CourierCompanyCollection

class CourierUserServiceCollectionImpl(ICourierUserService):
    def __init__(self):
        self.__companyObj = CourierCompanyCollection()

    def add_courier(self, courier):
        self.__companyObj.add_courier(courier)

    def remove_courier(self, courier):
        self.__companyObj.remove_courier(courier)

    def get_all_couriers(self):
        return self.__companyObj.get_couriers()
