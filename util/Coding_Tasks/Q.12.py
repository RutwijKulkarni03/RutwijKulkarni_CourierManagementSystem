'''12. Order Confirmation Email: Create a program that generates an order confirmation email. The email
should include details such as the customer's name, order number, delivery address, and expected
delivery date.'''

# Function to generate order confirmation email
def generate_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date):
    email_subject = "Order Confirmation"
    email_body = f"Dear {customer_name},\n\n" \
                 f"We are pleased to confirm your order with order number {order_number}.\n" \
                 f"Your order will be delivered to the following address:\n" \
                 f"{delivery_address}.\n" \
                 f"Expected delivery date: {expected_delivery_date}.\n\n" \
                 f"Thank you for choosing our service.\n\n" \
                 f"Best regards,\n" \
                 f"The Courier Management System Team"
    return email_subject, email_body

# Example usage:
def main():
    customer_name = input("Enter customer's name: ")
    order_number = input("Enter order number: ")
    delivery_address = input("Enter delivery address: ")
    expected_delivery_date = input("Enter expected delivery date: ")

    email_subject, email_body = generate_order_confirmation_email(customer_name, order_number, delivery_address, expected_delivery_date)
    print("Email Subject:", email_subject)
    print("Email Body:", email_body)

if __name__ == "__main__":
    main()
