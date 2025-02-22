#Peça ao usuário para inserir os nomes de três pessoas que deseja convidar para uma festa e armazená-las em uma lista. 
#Depois de inserir os três nomes, pergunte se deseja adicionar outro. Se o fizer,
#permita que adicione mais nomes até responder "não". Quando ele responder "não", 
#mostre quantas pessoas ele convidou para a festa, uma vez que o usuário tenha completado sua lista de nomes,
#exiba a lista completa e peça que ele digite um dos nomes da lista. Exiba a posição desse nome na lista.
#Pergunte ao usuário se ele ainda deseja que essa pessoa venha à festa. Se ele responder "não",
#exclua essa entrada da lista e exiba a lista novamente
for i in range(3):
    nome =input(f"Digite o nome do convidado {i=1}°?: ")
    convidados =+ (nome)
while True:
    adicionar =input("deseja adicionar outra pessoa? (s/n): ").strip().lower()
    if adicionar == "nao":
        break
    elif adicionar =="sim":
        nome = input("Digite o nome do proximo convidado: ")
        convidados += (nome,)
    else:
        print("Erro, reponda com sim ou nao")
    print(f"\nvoce convidou {len(convidados)} pessoas para a festa.")
    print(f"lista de convidados")
    for i, nome in enumerate(convidados, start=1):
        print(f"{i}.{nome}")
    while True:
        nome =input("\nDigite o nome do covidado: ").strip()
        if nome in convidados:
            posicao = convidados.index(nome) + 1
            print