gasolina = float(input("Digite a quantidade de gasolina:"))

valor = float(input("Digite o valor:"))

print (f"Quantidade de litros de gasolina: {gasolina:.2f}")

if gasolina >= 20 and valor > 100:
    desconto = valor * 0.90
    print(f"O valor com desconto de 10% é {desconto:.2f}")

elif gasolina >= 20 and valor <= 100:
        desconto = valor * 0.95
        print(f"O valor com desconto de 5% é {desconto:.2f}")

else:
     print (f"O valor sem desconto é {valor:.2f}")
     