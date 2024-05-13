class Parcel:
    def __init__(self, parcelID, orderID, courierID, senderName, senderAddress, receiverName, receiverAddress, weight, status, trackingNumber, orderDate, deliveryDate):
        self.__parcelID = parcelID
        self.__orderID = orderID
        self.__courierID = courierID
        self.__senderName = senderName
        self.__senderAddress = senderAddress
        self.__receiverName = receiverName
        self.__receiverAddress = receiverAddress
        self.__weight = weight
        self.__status = status
        self.__trackingNumber = trackingNumber
        self.__orderDate = orderDate
        self.__deliveryDate = deliveryDate

    def get_parcelID(self):
        return self.__parcelID

    def get_orderID(self):
        return self.__orderID

    def get_courierID(self):
        return self.__courierID

    def get_senderName(self):
        return self.__senderName

    def get_senderAddress(self):
        return self.__senderAddress

    def get_receiverName(self):
        return self.__receiverName

    def get_receiverAddress(self):
        return self.__receiverAddress

    def get_weight(self):
        return self.__weight

    def get_status(self):
        return self.__status

    def get_trackingNumber(self):
        return self.__trackingNumber

    def get_orderDate(self):
        return self.__orderDate

    def get_deliveryDate(self):
        return self.__deliveryDate

    def __str__(self):
        return f"Parcel(ID: {self.__parcelID}, OrderID: {self.__orderID}, CourierID: {self.__courierID}, SenderName: {self.__senderName}, SenderAddress: {self.__senderAddress}, ReceiverName: {self.__receiverName}, ReceiverAddress: {self.__receiverAddress}, Weight: {self.__weight}, Status: {self.__status}, TrackingNumber: {self.__trackingNumber}, OrderDate: {self.__orderDate}, DeliveryDate: {self.__deliveryDate})"
