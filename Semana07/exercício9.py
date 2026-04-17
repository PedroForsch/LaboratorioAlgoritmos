idade = 0
salario = 0
sexo = 'f' 'm' 
estado = 's' 'c' 'v' 'd'
repetir = 1

while repetir > 0:
    idade = int(input("Insira sua idade:"))
    salario = float(input("Insira seu salário:"))
    sexo = input("Insira seu sexo(f ou m):").lower()
    estado = input("Insira seu estado civil (s c v d):").lower()
    if idade >= 0 and idade <= 150:
        if salario > 0:
            if sexo == "f" or sexo == "m":
                if estado == "s" or estado == "c" or estado == "v" or estado == "d":
                    repetir = repetir - 1
                    print ("Validado!")
                else:
                    print ("Inválido! Digite Novamente!")
            else:
                print ("Inválido! Digite Novamente!")
        else:
            print ("Inválido! Digite Novamente!")
    else:
        print ("Inválido! Digite Novamente!")

