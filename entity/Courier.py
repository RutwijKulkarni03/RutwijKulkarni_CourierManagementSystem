class Courier:
    def __init__(self, courierID, senderName, senderAddress, receiverName, receiverAddress, weight, status, trackingNumber, deliveryDate):
        self.__courierID = courierID
        self.__senderName = senderName
        self.__senderAddress = senderAddress
        self.__receiverName = receiverName
        self.__receiverAddress = receiverAddress
        self.__weight = weight
        self.__status = status
        self.__trackingNumber = trackingNumber
        self.__deliveryDate = deliveryDate


    def __str__(self):
        return f"Courier(ID: {self.__courierID}, Sender: {self.__senderName}, Receiver: {self.__receiverName}, Status: {self.__status})"
