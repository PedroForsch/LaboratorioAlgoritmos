
nome = input("Digite o nome do treinador:")

salarioatual = float(input("Digite o salário atual:"))

tempodeservico = float(input("Digite o tempo de serviço(Em anos):"))

print (nome)


if tempodeservico >= 5 and salarioatual <= 2000:
    aumento = salarioatual * 1.10
    print (f"O aumento concedido foi de 10% e seu novo salário é {aumento:.2f}")

else:
    aumento1 = salarioatual * 1.05
    print (f"O aumento concedido foi de 5% e seu novo salário é {aumento1:.2f}")



