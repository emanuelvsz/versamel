from abc import ABC, abstractmethod

class Manager(ABC):
    @abstractmethod
    def loadAll(self):
        pass