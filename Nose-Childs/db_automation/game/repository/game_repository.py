from abc import ABC, abstractmethod


class GameRepository(ABC):

    @abstractmethod
    def playerAWinPrint(self):  # sum
        pass

    @abstractmethod
    def playerBWinPrint(self):
        pass

    @abstractmethod
    def drawPrint(self):
        pass
