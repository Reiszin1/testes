
valor = 100
estoque = 50
dia = 1
vendidos = 0


print('PROMOÇAO IMPERDIVEL!!')
print('A cada dia os produtos tem mais 10% de desconto ate o ultimo dia da semana! ou enquanto durarem os estoques!!!')
print('')
while valor >30 and estoque > 0 and dia <= 7:
	print(f'no dia {dia} o valor do produto e R${valor},00 e a quantidade disponivel e {estoque}')
	dia += 1
	valor = valor - (valor * 0.10)
	vendidos = input('Digite a quantidade de itens vendida nesse dia: ')
	estoque -= int(vendidos)
	print('')	
