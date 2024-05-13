from dao.ICourierAdminService import ICourierAdminService

class CourierAdminServiceImpl(CourierUserServiceImpl, ICourierAdminService):
    def __init__(self):
        super().__init__()

    # Implement methods of ICourierAdminService interface here
    # For example:
    def add_courier(self, courier):
        self.companyObj.add_courier(courier)

    def remove_courier(self, courier_id):
        self.companyObj.remove_courier(courier_id)

    # Implement other methods as needed

# Example usage:
# Instantiate the CourierAdminServiceImpl class
admin_service = CourierAdminServiceImpl()

# Use the admin service methods
admin_service.add_courier(courier)
admin_service.remove_courier(courier_id)
