from categoria import Categoria
from transacao import Transacao
from utilitarios import cadastrar_categoria, cadastrar_transacao, saldo_total, LISTA_CATEGORIAS, LISTA_TRANSACOES


# Criação de categorias
categoria_receitas = cadastrar_categoria('Receitas')
categoria_contas = cadastrar_categoria('Contas Fixas')
categoria_lazer = cadastrar_categoria('Lazer')
categoria_viagens = cadastrar_categoria('Viagens')

# Criação de transações
cadastrar_transacao(
    descricao='Salário',
    valor=5000.00,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao='mesada',
    valor=1500.00,
    categoria=categoria_receitas
)

cadastrar_transacao(
    descricao='Ingressos show',
    valor=-150.00,
    categoria=categoria_lazer
)

cadastrar_transacao(
    descricao='Conta de Luz',
    valor=-500.00,
    categoria=categoria_contas
)

cadastrar_transacao(
    descricao='Disney',
    valor=-500.00,
    categoria=categoria_viagens
)

total = saldo_total()
print(f"Saldo total: R${total:.2f}")

print("\nTransações cadastradas:") 
for transacao in LISTA_TRANSACOES:
    transacao.exibir()
    print("---")

print("\nCategorias cadastradas:")
for categoria in LISTA_CATEGORIAS:
    print(f"- {categoria.nome}")
