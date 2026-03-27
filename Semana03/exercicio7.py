valor = float(input("Digite o valor da compra:"))

if valor > 100:
    valorfinal = valor * 0.90
    print ("Sua compra custa", valorfinal, "Reais")
else:
    print ("Sua compra custa", valor, "Reais")