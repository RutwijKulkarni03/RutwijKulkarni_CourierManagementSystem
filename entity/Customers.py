class Customer:
    def __init__(self, customerID, orderID, name, email, contactNumber, address, username, password):
        self.__customerID = customerID
        self.__orderid = orderID
        self.__name = name
        self.__email = email
        self.__contactNumber = contactNumber
        self.__address = address
        self.__username = username
        self.__password = password

    def get_customerID(self):
        return self.__customerID

    def get_orderID(self):
        return self.__orderID

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_contactNumber(self):
        return self.__contactNumber

    def get_address(self):
        return self.__address

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def __str__(self):
        return f"Customer(ID: {self.__customerID}, OrderID: {self.__orderid}, Name: {self.__name}, Email: {self.__email}, Contact: {self.__contactNumber}, Address: {self.__address}, Username: {self.__username}, Password: {self.__password})"
