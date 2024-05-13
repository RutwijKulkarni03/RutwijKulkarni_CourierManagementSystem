from abc import ABC, abstractmethod

class ICourierAdminService(ABC):
    @abstractmethod
    def add_courier_staff(self, name, contact_number):
        pass
