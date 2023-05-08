from abc import ABC, abstractmethod

class FormasInterface(ABC):

    @abstractmethod
    def get_perimetro(self):
        ...

    def get_area(self):
        ...