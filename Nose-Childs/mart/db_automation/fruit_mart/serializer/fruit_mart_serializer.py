"""""

from rest_framework import serializers

from fruit_mart.entity.fruit_mart import FruitMart


class DiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FruitMart
        fields = ['id', 'number']
        # fields = ['number']
        
        
        """""
