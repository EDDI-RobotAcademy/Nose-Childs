from rest_framework import serializers

from fruit_mart.entity.fruit_mart_entity import FruitMart


class FruitMartSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitMart
        fields = ['id', 'number']
        # fields = ['number']
