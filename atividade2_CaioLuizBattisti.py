#Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos
#solicite ao usuário para digitar um nome de produto e exiba a posição dele
#em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.
produtos =tuple(input(f"Digite o nome do produto {i+1}: ")for i in range(10))
print("\nprodutos inseridos: ")
for produto in produtos:
    print(produto)
    nome_produto = input("\nDigite o nome de um produto: ")
    if nome_produto in produto:
        print(f"O produto '{nome_produto}' esta na posição: {produtos.index(nome_produto)}")
    else:
        print(f"O produto '{nome_produto}' nao foi encontrado!")
    try:
        indice = int(input("\nDigite o produto entre 0 e 9: "))
        if indice <= 0 and indice < 10:
            print(f"O produto na posição {indice} é '{produto[indice]}'")
    except ValueError:
            print("Entrada invalida,tente de novo!")