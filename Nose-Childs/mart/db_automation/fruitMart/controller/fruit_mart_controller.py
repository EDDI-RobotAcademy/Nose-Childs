from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from fruit_mart.serializer.fruit_mart_serializer import FruitMartSerializer
from fruit_mart.service.fruit_mart_service_impl import FruitMartServiceImpl


# Create your views here.
class FruitMartController(viewsets.ViewSet):
    fruitMartService = FruitMartServiceImpl.getInstance()

    def requestSellingFruit(self, request, fruitMart=None):
        requestGetData = request.GET
        requestCustomerId = requestGetData.get('customerId')
        orderId = requestGetData.get('orderId')

        fruit_mart = self.fruitMartService.sellingFruit(orderId, requestCustomerId)
        return Response(fruitMart, status=status.HTTP_200_OK)

    def requestFindDice(self, request):
        requestGetData = request.GET
        requestFruitMart = requestGetData.get('id')

        foundFruitMart = self.fruitMartService.findFruitMart(requestFruitMart)

        return Response(
            model_to_dict(foundFruitMart),
            status=status.HTTP_200_OK)

    def requestEveryFruitMart(self, request):
        fruitList = self.fruitMartService.findEveryFruitMart()

        # fruitList 중 JSON 변환 할 항목들을 미리 지정하고
        # serializer.data로 변환한 항목을 리턴함
        serializer = FruitMartSerializer(fruitList, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
