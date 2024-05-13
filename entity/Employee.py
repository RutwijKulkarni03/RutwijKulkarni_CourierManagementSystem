class Employee:
    def __init__(self, employeeID, name, email, contactNumber, role, salary):
        self.__employeeID = employeeID
        self.__name = name
        self.__email = email
        self.__contactNumber = contactNumber
        self.__role = role
        self.__salary = salary


    def __str__(self):
        return f"Employee(ID: {self.__employeeID}, Name: {self.__name}, Role: {self.__role}, Salary: {self.__salary})"
