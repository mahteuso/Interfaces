from abc import ABC, abstractmethod


class RepositorioInterface(ABC):

    @abstractmethod
    def inserir(self, dado) -> None:
        ...

    @abstractmethod
    def remover(self, dado) -> None:
        ...
