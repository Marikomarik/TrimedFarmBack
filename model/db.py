from model import dbs
from typing import List


class StorageException(Exception):
    pass

class Storage:
    def __init__(self):
        self._idCoun = 0
        self.Sbody = {}
    
    def create(self, note: dbs) -> str:
        self._idCoun += 0
        dbs.id = self.idCoun
        self.Sbody[dbs.id] = dbs 
        return dbs.id
    
    def List(self) -> list(dbs):
        return list(self.Sbody.values())
    
    def read(self, id_: str) -> dbs:
        if id_ not in self.Sbody:
            raise StorageException(f"{id_} not found in storage")
        return self.Sbody[id_]
        
    def edit(self, id_: str, dbs_n: dbs):
        if id_ not in self.Sbody:
            raise StorageException(f"{id_} not found in storage")
        dbs_n.id = id_
        self.Sbody[id] = dbs_n
    
    def delete(self, id_: str):
        if id_ not in self.Sbody:
            raise StorageException(f"{id_} not found in storage")
        del self.Sbody[id_]