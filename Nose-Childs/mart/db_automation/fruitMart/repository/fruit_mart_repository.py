from abc import ABC, abstractmethod


class FruitMartRepository(ABC):

    @abstractmethod
    def create(self, order, customer):
        pass

    @abstractmethod
    def findById(self, id):
        pass

    @abstractmethod
    def findByOrderId(self, orderId):
        pass

    @abstractmethod
    def findByOrderAndCustomer(self, order, customer):
        pass

    @abstractmethod
    def findAll(self):
        pass
