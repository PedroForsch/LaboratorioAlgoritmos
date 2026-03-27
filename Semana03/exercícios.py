horas= float(input("Quantas horas você trabalhou?"))

salario = horas * 35 

if salario < 1000:
    salariofinal = salario + 300
    print ("Seu salário é", salariofinal, "Reais")
else:
    print ("Seu salários é", salario, "Reais")
