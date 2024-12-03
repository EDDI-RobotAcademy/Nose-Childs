from django.urls import path, include
from rest_framework.routers import DefaultRouter
from game.controller.game_controller import GameController


# 웹 브라우저에서 아래 요청에 대한 기본 URL이 /game로 시작
router = DefaultRouter()
router.register(r"game", GameController, basename='game')

urlpatterns = [
    path('', include(router.urls)),
    path('dice-Result-Sum',
         GameController.as_view({ 'get': 'diceResultSum' }),
         name='주사위 게임 결과 합산'),
    path('check-Winner',
         GameController.as_view({ 'get': 'checkWinner' }),
         name='Winner 찾기'),
]