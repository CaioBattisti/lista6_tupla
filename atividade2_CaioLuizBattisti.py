#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos
#solicite ao usuário para digitar um nome de produto e exiba a posição dele
#em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
for i in range(10):
    produtos = input("Digite o nome do produto {i+1}:")
    print("\nLista de Produtos:",produtos)
    produto_usuario =input("Digite um produto exibido")
if produto_usuario in produtos:
    print(f"O produto {produto_usuario} esta na posição {produtos.index(produto_usuario)}")
else:
    print("este pais nao esta na lista!")
