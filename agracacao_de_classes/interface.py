from abc import ABC, abstractmethod


class CarrinhoInterface(ABC):

    @abstractmethod
    def __repr__(self):
        ...
