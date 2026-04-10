valorcompra = 0
opcao = 0

while opcao != 4:
    print ("1 - Inserir produto:")
    print ("2 - Valor atual da compra")
    print ("3 - Simulação de parcelamento")
    print("4 - Sair")
    opcaoparcelamento = int(input("Digite a opção:"))

    if opcaoparcelamento == 1:
        valorproduto = float(input("Valor do produto:"))
        valorcompra = valorcompra + valorproduto
        #valorcompra += valorproduto

    elif opcaoparcelamento == 2:
        print (f"Valor atual da compra:{valorcompra:.2f}")

    elif opcaoparcelamento == 3:
        print ("1 - A vista")
        print ("2 - 2x")
        print ("3 - 3x")
        print ("4 - Retorna ao menu principal")

        if opcaoparcelamento == 1:
            print (f"Valor a vista: {valorcompra:.2f}")

        elif opcaoparcelamento == 2:
            print (f"Valor parcela(2x): {valorcompra / 2 :.2f}")

        elif opcaoparcelamento == 3:
            print (f"Valor parcela(3x): {valorcompra / 3 :.2f}")

        elif opcaoparcelamento == 4:
            print("Retornando...")

        else:
            print ("Opção Inválida!")

    elif opcao == 4:
        print(f"Até mais, valor da compra R${valorcompra}")
        
    else:
        print("Opção Inválida!")