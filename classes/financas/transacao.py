from dataclasses import dataclass
from categoria import Categoria

@dataclass
class Transacao:
    descricao: str
    valor: float
    categoria: Categoria

    def exibir(self):
        print("Detalhes da transação:")
        print(f"Descrição: {self.descricao}")
        print(f"Valor: R${self.valor:.2f}")
        print(f"Categoria: {self.categoria.nome}")