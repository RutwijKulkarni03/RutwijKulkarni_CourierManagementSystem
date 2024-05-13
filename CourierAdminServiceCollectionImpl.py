from dao.ICourierAdminService import ICourierAdminService

class CourierAdminServiceCollectionImpl(CourierUserServiceCollectionImpl, ICourierAdminService):
    def __init__(self, companyObj):
        super().__init__(companyObj)

    # Implement methods of ICourierAdminService interface here
    # For example:
    def add_courier(self, courier):
        self.companyObj.add_courier(courier)

    def remove_courier(self, courier_id):
        self.companyObj.remove_courier(courier_id)

    # Implement other methods as needed

# Example usage:
# Instantiate the CourierAdminServiceCollectionImpl class
admin_service = CourierAdminServiceCollectionImpl(companyObj)

# Use the admin service methods
admin_service.add_courier(courier)
admin_service.remove_courier(courier_id)
