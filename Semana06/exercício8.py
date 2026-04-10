opcao = 0
caixa = float(input("Insira o valor do caixa atual:"))
venda = 0
retirar = 0

while opcao != 4:
    print ("1 - Realizar Venda")
    print ("2 - Retirar Dinheiro")
    print ("3 - Dinheiro em caixa")
    print ("4 - Sair")
    opcao = int(input("Selecione a opção:"))

    if opcao == 1:
        venda = float(input("Qual o valor da venda?"))
        caixa += venda
    elif opcao == 2:
        retirar = float(input("Qual o valor que deseja retirar?"))
        caixa = caixa - retirar
    elif opcao == 3:
        print (f"O dinheiro em caixa atual é {caixa:.2f}")
    elif opcao == 4:
        print ("Saindo...")
    else:
        print ("Opção Inválida!")
