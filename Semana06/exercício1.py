
ingressos = 0
opcao = 0


while opcao != 4:
    print ("1 - Diminuir quantidade de ingressos")
    print ("2 - Adicionar ingresos extras")
    print ("3 - Mostrar ingressos disponíveis")
    print ("4 - Encerrar")
    opcao = int(input("Digite a opção:"))
    
    if opcao == 1:
        diminuir = float(input("Quantos ingressos deseja diminuir?"))
        ingressos -= diminuir
        print (f"Quantidade de ingressos:{ingressos}")
    
    elif opcao == 2:
        aumentar = float(input("Quantos ingressos deseja aumentar?"))
        ingressos += aumentar
        if ingressos > 100:
            print (f"Capacidade Máxima Ultrapassada!")
        elif ingressos <= 100:
            print (f"Quantidade de ingressos:{ingressos}")
    
    elif opcao == 3:
        atual = ingressos
        print (f"A quantidade atual de ingressos é {atual}")
    
    elif opcao == 4:
        print ("Encerrando...")
    else:
        print ("Valor Digitado Inválido!")