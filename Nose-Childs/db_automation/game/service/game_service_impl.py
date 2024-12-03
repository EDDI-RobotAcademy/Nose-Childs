from fontTools.merge.util import sumLists

from account.entity.account import Account
from dice.entity.dice import Dice
from game.entity.game import Game
from dice.repository.dice_repository_impl import DiceRepositoryImpl
from game.repository.game_repository_impl import GameRepositoryImpl
from account.repository.account_repository_impl import AccountRepositoryImpl
from game.service.game_service import GameService
from dice.controller.dice_controller import DiceController

class GameServiceImpl(GameService):
    __instance = None

    sumList = []

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

            # Service Layer에서 Repository Layer를 연결하는 방법
            cls.__instance.__gameRepository = GameRepositoryImpl.getInstance()
            cls.__instance.__accountRepository = AccountRepositoryImpl.getInstance()
            cls.__instance.__diceRepository = DiceRepositoryImpl.getInstance()

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def diceResultSum(self, diceList):

        self.__diceRepository.rollDice()  # diceList = [[2,3], [1,6]]
        for seq in diceList:  # seq = [2,5]
            sum = seq[0] + seq[1]
            self.sumList.append(sum)   # sumList[0] : 첫번째 플레이어 sum 값, sumList[1] : 두번째 플레이어

        return self.sumList   # sumList = [5, 7]

    def checkWinner(self):
        #A = self.sumList[0]
        #B = self.sumList[1]

        if self.sumList[0] > self.sumList[1]:
            return self.__gameRepository.playerAWinPrint()

        elif self.sumList[0] < self.sumList[1]:
            return self.__gameRepository.playerBWinPrint()

        else:
             return self.__gameRepository.drawPrint()

