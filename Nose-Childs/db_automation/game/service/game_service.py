from abc import ABC, abstractmethod


class GameService(ABC):

    @abstractmethod
    def diceResultSum(self):  # player1 [2,4] -> return 6 / player2 [1,4] -> return 5
        pass

    @abstractmethod
    def checkWinner(self):
        pass
    # diceResultSum을 가지고 승패를 가림 E.g) {id}: Win or {id}: Lose


    # 무승부는 어떻게 처리? 그냥 print('무승부')?