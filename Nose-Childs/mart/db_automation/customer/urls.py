from django.urls import path, include
from rest_framework.routers import DefaultRouter

from customer.controller.customer_controller import CustomerController

router = DefaultRouter()
router.register(r"customer", CustomerController, basename='customer')
# customer OR order OR fruitMart 통일해주기. 여긴 customer.

# 이쪽부분 작성할땐 Controller 참고하기
urlpatterns = [
    path('', include(router.urls)),
    path('request-Create-Customer', # Controller에 def requestCreateCustomer(self, request): 있었음.
         CustomerController.as_view({ 'get': 'requestCreateName' }),
         name='Customer 이름 생성'),

    path('request-Find-Customer',
         CustomerController.as_view({ 'get': 'requestFindCustomer' }),
         name='Customer account 찾기'),

    #path('request-every-dice',
    #     DiceController.as_view({ 'get': 'requestEveryDice' }),
    #     name='주사위 전체 정보 획득'),
]