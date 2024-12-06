from django.db import models

from order.entity.order import Order
from customer.entity.customer import Customer

from customer.entity.customer import Customer


class FruitMart(models.Model):
    # 앞서 우리가 고유한 유일 숫자값 만들 것
    id = models.AutoField(primary_key=True)
    # 주사위 눈금은 숫자
    fruitAmount = models.IntegerField()
    costomer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='fruitMart')
    order = models.ForeignKey(FruitMart, on_delete=models.CASCADE, related_name='fruitMart')

    def __str__(self):
        return f"과일 id: {self.id}, 눈금: {self.fruitAmount}"

    def getId(self):
        return self.id

    def getNumber(self):
        return self.fruitAmount

    def getPlayer(self):
        return self.costomer

    def getGame(self):
        return self.order

    class Meta:
        db_table = "fruit_mart"
