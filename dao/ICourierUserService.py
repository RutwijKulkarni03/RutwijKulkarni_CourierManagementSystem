from abc import ABC, abstractmethod

class ICourierUserService(ABC):
    @abstractmethod
    def place_order(self):
        pass

    @abstractmethod
    def get_order_status(self, order_id):
        pass

    @abstractmethod
    def cancel_order(self, order_id):
        pass

    @abstractmethod
    def get_assigned_orders(self, user_id):
        pass
