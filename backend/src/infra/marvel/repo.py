from ...core.interfaces.loader import Loader

class Repository(Loader):
    def findAll(self):
        return [1, 2, 3, "Abc"] 
    