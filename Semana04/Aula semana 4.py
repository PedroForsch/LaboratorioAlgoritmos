idade = int(input("Idade:"))

if idade > 60:
    print ("Sênior")
elif idade > 20:
    print ("Adulto")
elif idade > 10:
    print ("Júnior")
elif idade > 0:
    print ("Infantil")
else:
    print ("Idade Inválida")