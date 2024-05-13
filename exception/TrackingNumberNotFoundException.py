class TrackingNumberNotFoundException(Exception):

    def __init__(self, tracking_number):
        self.tracking_number = tracking_number
        super().__init__(f"Tracking number: {tracking_number} not found")
