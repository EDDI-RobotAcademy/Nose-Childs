from django.forms import model_to_dict
from rest_framework import viewsets, status
from rest_framework.response import Response

from rest_framework import viewsets
from game.service.game_service_impl import GameServiceImpl


class GameController(viewsets.ViewSet):
    gameService = GameServiceImpl.getInstance()

    def requestGame(self, request):  # 막 넣었어요...
        #game = self.GameService.rollDice()

        return Response(status=status.HTTP_200_OK)


    def requestResult(self, request): # 이것도요...
    #    requestGetData = request.GET
    #    requestDiceNumber = requestGetData.get('number')

    #    foundDice = self.diceService.findDice(requestDiceNumber)

        return Response(status=status.HTTP_200_OK)
