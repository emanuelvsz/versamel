from ..interfaces.manager import Manager
from ...infra.marvel.repo import Repository

class Services(Manager):
    
    def loadAll(self):
        data = Repository().findAll()
        return data
    