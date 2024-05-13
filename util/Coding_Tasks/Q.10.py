'''
10. Customer Data Validation: Write a function which takes 2 parameters, data-denotes the data and
detail-denotes if it is name address or phone number.Validate customer information based on
following criteria. Ensure that names contain only letters and are properly capitalized, addresses do not
contain special characters, and phone numbers follow a specific format (e.g., ###-###-####).
'''

import re
# Function to validate customer information
def validate_customer_info(data, detail):
    if detail == "name":
        if data.isalpha() and data.istitle():
            return True
        else:
            return False
    elif detail == "address":
        if re.match(r"^[a-zA-Z0-9\s]*$", data):
            return True
        else:
            return False
    elif detail == "phone":
        if re.match(r"^\d{3}-\d{3}-\d{4}$", data):
            return True
        else:
            return False
    else:
        print("Invalid detail provided.")
        return False

# Function to get user input for customer information
def get_customer_info():
    customer_name = input("Enter customer name: ")
    customer_address = input("Enter customer address: ")
    customer_phone = input("Enter customer phone number (format: ###-###-####): ")
    return customer_name, customer_address, customer_phone

# Example usage:
def main():
    customer_name, customer_address, customer_phone = get_customer_info()

    if validate_customer_info(customer_name, "name"):
        print("Name is valid")
    else:
        print("Name is not valid")

    if validate_customer_info(customer_address, "address"):
        print("Address is valid")
    else:
        print("Address is not valid")

    if validate_customer_info(customer_phone, "phone"):
        print("Phone number is valid")
    else:
        print("Phone number is not valid")

if __name__ == "__main__":
    main()