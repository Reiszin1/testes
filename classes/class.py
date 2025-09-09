class cliente:

    def __init__(self, nome, email, telefone, idade):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.idade = idade


    def exibir_cliente(self):
        print(f'Nome: {self.nome}, Email: {self.email}, Telefone: {self.telefone}, Idade: {self.idade}')
    
    def chamar_exibir_cliente(self):
        self.exibir_cliente()

cliente1 = cliente('Tiago', 'email@email.com', '11999999999', 25)

cliente1.chamar_exibir_cliente()