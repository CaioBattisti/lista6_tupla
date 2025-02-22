#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos
#solicite ao usuário para digitar um nome de produto e exiba a posição dele
#em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
produtos =()
for i in range(10):
    produtos = input("Digite o nome do produto: ")
    print("\nLista de Produtos:",produtos)
produto_usuario =input("Digite um produto exibido: ")
if produto_usuario in produtos:
    print(f"O produto {produto_usuario} esta na posição {produtos.index(produto_usuario)}")
else:
    print("este produto nao esta na lista!")
indice = -1
while indice not in range(10):
    indice =int(input("digite um numero entre 0 e 9: "))
    print(f"O produto na posição {indice} é: {produtos[indice]}")
if indice not in range(10):
    print("Erro,Tente novamente!")