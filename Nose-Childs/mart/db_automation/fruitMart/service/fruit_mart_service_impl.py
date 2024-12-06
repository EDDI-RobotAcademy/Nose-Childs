from fruit_mart.repository.fruit_mart_repository_impl import FruitMartRepositoryImpl
from fruit_mart.service.fruit_mart_service import FruitMartService
from order.repository.order_repository_impl import OrderRepositoryImpl
from customer.repository.customer_repository_impl import CustomerRepositoryImpl

from fruit_mart.service.fruit_mart_service import FruitMartService


class FruitMartServiceImpl(FruitMartService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            cls.__instance.__fruitMartRepository = FruitMartRepositoryImpl.getInstance()
            cls.__instance.__orderRepository = OrderRepositoryImpl.getInstance()
            cls.__instance.__customerRepository = CustomerRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def sellingFruit(self, orderId, customerId):
        order = self.__orderRepository.findById(orderId)
        customer = self.__customerRepository.findById(customerId)
        return self.__fruitMartRepository.create(order, customer)

    def findFruitMart(self, requestFruitMartId):
        return self.__fruitMartRepository.findById(requestFruitMartId)

    def findEveryDice(self):
        return self.__fruitMartRepository.findAll()
