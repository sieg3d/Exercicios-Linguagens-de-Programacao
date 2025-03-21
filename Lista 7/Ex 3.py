# 3. Dicionário de Tradução
# Crie um dicionário que contenha algumas palavras em português como chave e suas respectivas traduções para inglês como valor.
# Permita que o usuário digite uma palavra em português e retorne sua tradução. 
# Caso a palavra não esteja no dicionário, exiba uma mensagem informando que a tradução não foi encontrada.

tradutor = {
    "casa": "house",
    "carro": "car",
    "livro": "book",
    "computador": "computer"
}

palavra_portugues = input("Digite uma palavra em português: ")

if palavra_portugues in tradutor:
    print(f"Tradução: {tradutor[palavra_portugues]}")
else:
    print("Tradução não encontrada.")