from abc import ABC, abstractmethod

class Loader(ABC):
    @abstractmethod
    def findAll(self):
        pass