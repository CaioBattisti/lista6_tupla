#Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma tupla. 
#Depois de inserir os três nomes, pergunte se deseja adicionar outro. Se o fizer,
#permita que adicione mais nomes até responder "não". Quando ele responder "não", 
#mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes,
#exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista.
#Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não",
#exclua essa entrada da lista e exiba a lista novamente
nomes =tuple(input("Digite um nome: ")for nomes in range(3))
novos_nomes = []
while True:
    adicionar = input("Deseja adicionar outro nome? (s/n): ").strip().lower()
    if adicionar == "n":
        break
    novo_nome = input("Digite o nome adicional: ")
    novos_nomes.append(novo_nome)
nomes += tuple(novos_nomes)
print(f"voce convidou {len(nomes)} pessoas para a festa.")
print("Lista de convidados:",nomes)
print("Caioluizbattisti")
nome_procurado = input("Digite um nome da lista para procura-lo: ")
if nome_procurado in nomes:
    print(f"O nome {nome_procurado} esta na posição {nomes.index(nome_procurado)} da lista.")
    print("Caioluizbattisti")
else:
    print("O nome digitado não esta na lista!")
    print("Caioluizbattisti")
remover = input(f"Deseja remover {nome_procurado} da lista? (s/n): ").strip().lower()
if remover == "s" and nome_procurado in nomes:
    nomes = tuple(nome for nome in nomes if nome != nome_procurado)
    print("lista atualizada ",nomes)
    print("Caioluizbattisti")
else:
    print("nenhuma alteração feita na lista.")
    print("Caioluizbattisti")