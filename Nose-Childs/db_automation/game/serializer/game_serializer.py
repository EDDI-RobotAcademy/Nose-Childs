from rest_framework import serializers

from game.entity.game import Game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['id','diceNumber','gameFinalResult' ]