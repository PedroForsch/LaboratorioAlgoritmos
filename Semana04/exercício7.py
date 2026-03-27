print ("Opções de Kit:")
print ("1 → Kit Básico: Número de peito + medalha - R$100,00")
print ("2 → Kit Plus: Número de peito + medalha + camiseta - R$120,00")
print ("3 → Kit Premium: Número de peito + medalha + camiseta + squeeze + boné - R$150,00")

valor = float(input("Digite o valor a ser pago:"))

kit = int(input("Selecione sua opção de kit:"))

if kit == 1:
     if valor >= 100:
         print("Você recebeu o Kit Básico")
         if valor > 100:
            troco = valor - 100
            print(f"Seu troco é {troco} reais")
elif kit == 2:
    if valor >= 120:
        print("Você recebeu o Kit Básico")
        if valor > 120:
            troco = valor - 120
            print(f"Seu troco é {troco} reais")
elif kit == 3:
    if valor >= 150:
        print("Você recebeu o Kit Básico")
        if valor > 150:
            troco = valor - 150
            print(f"Seu troco é {troco} reais")
