clientes = 0
cafeA = 0
cafeB = 0
cafeC = 0

while clientes < 10:
    print ("A - Café Expresso")
    print ("B - Cappuccino")
    print ("C - Chá")
    opcao = (input("Insira seu voto:")).upper()
    if opcao == "A":
        cafeA += 1
        clientes += 1
    elif opcao == "B":
        cafeB += 1
        clientes += 1
    elif opcao == "C":
        cafeC += 1
        clientes += 1
    else:
        print ("Opção Inválida!")
    
porcA = (100 * cafeA) / 10
porcB = (100 * cafeB) / 10
porcC = (100 * cafeC) / 10
print (f"O café expresso teve {cafeA} votos, representando {porcA}%")
print (f"O cappuccino {cafeB} votos, representando {porcB}%")
print (f"O chá teve {cafeC} votos, representando {porcC}%")
