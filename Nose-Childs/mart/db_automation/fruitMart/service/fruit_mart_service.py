from abc import ABC, abstractmethod


class FruitMartService(ABC):

    @abstractmethod
    def sellingFruit(self, orderId, customerId):
        pass

    @abstractmethod
    def findFruitMart(self, requestFruitMartId):
        pass

    @abstractmethod
    def findEveryFruitMart(self):
        pass
