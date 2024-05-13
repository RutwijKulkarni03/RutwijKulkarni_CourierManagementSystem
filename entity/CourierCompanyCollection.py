class CourierCompanyCollection:
    def __init__(self):
        self.__couriers = []

    def add_courier(self, courier):
        self.__couriers.append(courier)

    def remove_courier(self, courier):
        if courier in self.__couriers:
            self.__couriers.remove(courier)
        else:
            print("Courier not found in the collection.")

    def get_couriers(self):
        return self.__couriers

    def __str__(self):
        return f"Courier Company Collection: {self.__couriers}"
