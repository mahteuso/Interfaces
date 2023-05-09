from repositorio import RepositorioInterface
from typing import Type


class MongoRepositorio(RepositorioInterface):

    def inserir(self, dado: Type[RepositorioInterface]) -> None:
        print(f'Inserindo {dado}, no banco de Mongo')

    def remover(self, dado: Type[RepositorioInterface]) -> None:
        print(f'Removendo {dado} do banco de Mongo')