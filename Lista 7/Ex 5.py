# 5. Catálogo de Produtos
# Crie um dicionário onde as chaves representem códigos de produtos e os valores sejam tuplas contendo o nome do produto e seu preço.
# Permita que o usuário informe um código para buscar o nome e o preço do produto correspondente.

produtos = {
    "PROD001": ("Laptop", 2500.00),
    "PROD002": ("Smartphone", 1200.00),
    "PROD003": ("Tablet", 800.00)
}

codigo_produto = input("Digite o código do produto: ")

if codigo_produto in produtos:
    nome_produto, preco_produto = produtos[codigo_produto]
    print(f"Nome: {nome_produto}, Preço: R$ {preco_produto:.2f}")
else:
    print("Produto não encontrado.")