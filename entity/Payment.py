class Payment:
    def __init__(self, payment_id, amount, payment_date, payment_method):
        self.payment_id = payment_id
        self.courier_id = courier_id
        self.location_id = location_id
        self.amount = amount
        self.payment_date = payment_date

    def __str__(self):
        return f"PaymentID: {self.payment_id}, CourierID: {self.courier_id}, LocationID: {self.location_id}, Amount: {self.amount}, PaymentDate: {self.payment_date}"
