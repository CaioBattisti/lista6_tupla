#Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida
#exibir o número de índice (ou seja, posição na lista) desse item na tupla.
paises = ("Brasil","russia","canada","china","mexico")
print("paises:",paises)
pais_usuario=input("Digite um dos paises exibidos: ")
if pais_usuario in paises:
    print(f"O pais {pais_usuario} esta na posição: {paises.index(pais_usuario)}")
    print("caioLuizbattsiti")
else: 
    print("este pais nao esta na lista!")
    print("caioLuizbattsiti") 