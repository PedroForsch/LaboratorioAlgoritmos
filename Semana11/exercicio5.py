elemento = []
contador = 0
valor = 0
op = 0
posicao = 0

while contador != 1:
    print ("1 - Inserir Item")
    print ("2 - Retirar Item")
    print ("3 - Listar Itens")
    print ("4 - Retirar todos os itens")
    print ("5 - Sair")
    op = int(input("Insira uma opção:"))

    if op == 5:
        contador = 1
    
    if op == 4:
        elemento = []
    
    if op == 3:
        for i in range(len(elemento)):
            print (elemento[i])

    if op == 2:
        posicao = int(input("Insira o número que deseja excluir:"))
        elemento.remove(posicao)

    if op == 1:
        valor = int(input("Insira um valor:"))
        elemento.append(valor)


