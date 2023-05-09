from repositorio import RepositorioInterface
from typing import Type

class MySqlRepositorio(RepositorioInterface):

    def inserir(self, dado: Type[RepositorioInterface]) -> None:
        print(f'Inserindo {dado}, no banco de MySql')


    def remover(self, dado: Type[RepositorioInterface]) -> None:
        print(f'Removendo {dado} do banco de MySql')
