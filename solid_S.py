"""Estudo da reponsabilidades única"""


class Cadastro:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade

    def _validacao(self):
        if isinstance(self.nome, str) and isinstance(self.idade, int):
            return True
        else:
            raise PermissionError

    def cadastro(self):
        try:
            self._validacao()
            print("Cadastro realizado com sucesso!")

        except PermissionError:
            raise ValueError('Dados incorretos, colocque somente latras em nome e somente números em idade')
