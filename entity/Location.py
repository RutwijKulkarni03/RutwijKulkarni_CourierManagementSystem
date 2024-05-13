class Location:
    def __init__(self, locationID, locationName, address):
        self.__locationID = locationID
        self.__locationName = locationName
        self.__address = address

    def __str__(self):
        return f"Location(ID: {self.__locationID}, Name: {self.__locationName}, Address: {self.__address})"
