class Clientes:
    pass


class Produtos:
    pass

class ControleRemoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
    
    def passar_canal(self, botao):
        if botao == '+':
            print('Aumentar o canal')
        elif botao == '-':
            print('Diminuir o canal')


controle_remoto = ControleRemoto('preto', '10cm', '2cm', '2cm')
controle_remoto2 = ControleRemoto('cinza', '10cm', '2cm', '2cm')

controle_remoto.passar_canal('+')
controle_remoto2.passar_canal('-')

print(controle_remoto2.cor)
