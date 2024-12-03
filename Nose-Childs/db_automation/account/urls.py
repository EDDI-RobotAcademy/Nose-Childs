from django.urls import path, include
from rest_framework.routers import DefaultRouter

from account.controller.account_controller import AccountController

# 웹 브라우저에서 아래 요청에 대한 기본 URL이 /dice로 시작
router = DefaultRouter()
router.register(r"account", AccountController, basename='account')

urlpatterns = [
    path('', include(router.urls)),
    path('request-Create-Name',
         # 웹 브라우저 상에서 /request-roll-dice 요청이 오면 'requestRollDice()' 구동
         # 결론적으로 /dice/request-roll-dice 로 시작
         AccountController.as_view({ 'get': 'requestCreateName' }),
         name='player 이름 생성'),
    path('request-Find-Account',
         AccountController.as_view({ 'get': 'requestFindAccount' }),
         name='player account 찾기'),
    #path('request-every-dice',
    #     DiceController.as_view({ 'get': 'requestEveryDice' }),
    #     name='주사위 전체 정보 획득'),
]