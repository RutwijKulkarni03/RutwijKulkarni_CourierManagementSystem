class User:
    def __init__(self, userID, name, email, password, contactNumber, address):
        self.__userID = userID
        self.__name = name
        self.__email = email
        self.__password = password
        self.__contactNumber = contactNumber
        self.__address = address

    def get_userID(self):
        return self.__userID

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_contactNumber(self):
        return self.__contactNumber

    def get_address(self):
        return self.__address

    def __str__(self):
        return f"User(ID: {self.__userID}, Name: {self.__name}, Email: {self.__email}, Contact: {self.__contactNumber})"
