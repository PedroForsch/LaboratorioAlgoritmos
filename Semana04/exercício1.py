valorcarro = float(input("Insira o valor do carro:"))

print (f"1 - Pagamento a vista (4% de desconto)")
print (f"2 - Pagamento em 12x (2% de juros)")
print (f"3 - Pagamento em 24x (7% de juros)")
print (f"4 - Pagamento em 36x (15% de juros)")

opcao = int(input("Digite a opção:"))

if opcao == 1:
    valor_total= valorcarro * 0.96
    print (f"O valor com desconto é: {valor_total:.2f}")
    print (f"O pagamento é a vista")

elif opcao == 2:
    valor_total= valorcarro * 1.02
    parcela = valor_total / 12
    print (f"O valor com juros é: {valor_total:.2f}")
    print (f"A parcela é: {parcela:.2f}")

elif opcao == 3:
    valor_total= valorcarro * 1.07
    parcela = valor_total / 24
    print (f"O valor com juros é: {valor_total:.2f}")
    print (f"A parcela é: {parcela:.2f}")

elif opcao == 4:
    valor_total= valorcarro * 1.15
    parcela = valor_total / 36
    print (f"O valor com juros é: {valor_total:.2f}")
    print (f"A parcela é: {parcela:.2f}")
    
else:
    print ("Inválido!")

 