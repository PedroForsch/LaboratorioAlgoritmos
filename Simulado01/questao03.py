valorpago = 0
opcao = 0
vender = 0
diesel = 0
gasolina = 0
valortotal = 0
troco = 0

while opcao != 2:
    print ("1 - Vender Combustível")
    print ("2 - Sair")
    opcao = int(input("Insira a opcão:"))
    if opcao == 1:
        print ("1 - Gasolina (R$ 6,89)")
        print ("2 - Diesel (R$ 4,80)")
        vender = int (input("Insira a opção:"))
        if vender == 1:
            valorpago = float(input("Insira o valor pago:"))
            gasolina = float(input("Insira a gasolina:"))
            valortotal = gasolina * 6.89
            print (f"O valor total é R${valortotal}")
            troco = valortotal - valorpago
            if troco < 0:
                print (f"Seu troco é R$ {troco}")
            elif troco > 0:
                print (f"Falta pagar R${troco}")
        elif vender == 2:
            valorpago = float(input("Insira o valor pago:"))
            diesel = float(input("Insira o diesel:"))
            valortotal = diesel * 4.80
            print (f"O valor total é R${valortotal}")
            troco = valortotal - valorpago
            if troco < 0:
                print (f"Seu troco é R$ {troco}")
            elif troco > 0:
                print (f"Falta pagar R${troco}")
        else:
            print("Erro")
    if opcao != 1 and opcao != 2:
        print ("Erro")

print (f"Gasolina: {gasolina}")
print (f"Diesel:{diesel}")
porcentagem = diesel + gasolina
porcentagemgas = (porcentagem * gasolina) / 100
print (f"A porcentagem de gasolina é {porcentagemgas}%")
porcentagemdiesel = (porcentagem * diesel) / 100
print (f"A porcentagem do diesel é {porcentagemdiesel}%")

