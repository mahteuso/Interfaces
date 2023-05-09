from repositorio import RepositorioInterface
from typing import Type
from mongo_repositorio import MongoRepositorio
from db.mysql_repositorio import MySqlRepositorio

class Usuario(RepositorioInterface):
    def __init__(self) -> None:
        self.mongo = MongoRepositorio()
        self.mysql = MySqlRepositorio()


    def inserir(self, dado: Type[RepositorioInterface]) -> None:
        if dado == isinstance(dado, MongoRepositorio):
            return self.mongo.inserir(dado)
        else:
            return self.mysql.inserir(dado)


    def remover(self, dado: any) -> None:
        pass

