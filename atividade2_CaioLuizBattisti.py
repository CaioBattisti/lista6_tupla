#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos
#solicite ao usuário para digitar um nome de produto e exiba a posição dele
#em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
produtos = tuple(input(f"Digite o Nome do Produto {i+1}: ")for i in range(10))

print("\nLista de Produto: ")
for i,produto in enumerate(produtos):
    print(f"{i}:{produto}")

nome_produto = input("\nDigite o nome do produto: ")
if nome_produto in produtos:
    posicao = produtos.index(nome_produto)
    print(f"O produto {nome_produto} esta na posicao {posicao}")
else:
    print("produto nao encontrado!")
while True:
    indice =int(input("\nDigite um numero entre 0 e 9: "))
    if 0 <= indice <=9:
        print(f"O produto na posição {indice} é '{produtos[indice]}'")
        break
    else:
        print("produto nao encontrado")