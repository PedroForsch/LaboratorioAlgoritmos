valor = 0
contador = 0

while contador != 1:
    valor = int(input("Insira o valor:"))
    if valor >= 1 and valor <= 59:
        print ("1 bimestre")
    elif valor > 59 and valor <= 120:
        print ("2 bimestre")
    elif valor > 120 and valor <= 181:
        print ("3 bimestre")
    elif valor > 181 and valor <= 243:
        print ("4 bimestre")
    elif valor > 243 and valor <= 304:
        print ("5 bimestre")
    elif valor > 304 and valor <= 365:
        print ("6 bimestre")
    elif valor < 1 or valor > 365:
        print ("Inválido!")
    if valor >= 1 and valor <= 365:
        contador = 1