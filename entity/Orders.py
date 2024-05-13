class Orders:
    def __init__(self, orderID, customerID, userID, orderDate, status):
        self.__orderID = orderID
        self.__customerID = customerID
        self.__userID = userID
        self.__orderDate = orderDate
        self.__status = status

    def get_orderID(self):
        return self.__orderID

    def get_customerID(self):
        return self.__customerID

    def get_userID(self):
        return self.__userID

    def get_orderDate(self):
        return self.__orderDate

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"Order(ID: {self.__orderID}, CustomerID: {self.__customerID}, UserID: {self.__productID}, OrderDate: {self.__orderDate}, Status: {self.__status})"
