class CourierServices:
    def __init__(self, serviceID, serviceName, cost):
        self.__serviceID = serviceID
        self.__serviceName = serviceName
        self.__cost = cost


    def __str__(self):
        return f"Service(ID: {self.__serviceID}, Name: {self.__serviceName}, Cost: {self.__cost})"
