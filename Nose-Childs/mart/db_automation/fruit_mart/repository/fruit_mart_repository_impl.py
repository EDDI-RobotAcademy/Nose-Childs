

from django.forms import model_to_dict
from fruit_mart.entity.fruit_mart_entity import FruitMart
from fruit_mart.repository.fruit_mart_repository import FruitMartRepository


class FruitMartRepositoryImpl(FruitMartRepository):
    __instance = None


    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, order, customer, fruitAmount=None):
        fruitMart = FruitMart(fruitAmount=fruitAmount, order=order, customer=customer)
        fruitMart.save()

        return model_to_dict(fruitMart)

    def findById(self, id):
        return FruitMart.objects.get(id=id)

    def findByOrderId(self, game):
        return FruitMart.objects.filter(order=game)

    def findAll(self):
        return FruitMart.objects.all()

    def findByOrderAndcustomer(self, order, customer):
        return FruitMart.objects.filter(order=order, customer=customer)
