class InvalidEmployeeIDException(Exception):

    def __init__(self, employee_id):
        self.employee_id = employee_id
        super().__init__(f"Invalid employee ID: {employee_id}. Employee ID must be an integer.")