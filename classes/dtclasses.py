from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    email: str
    idade: int

    def exibir_clientes(self):
        print(f'Meu nome é {self.nome}, meu email é {self.email} e tenho {self.idade} anos.')

cliente2 = Cliente(nome='Tiago', email='tih@tih.com', idade=25)

print(cliente2)

cliente2.exibir_clientes()

