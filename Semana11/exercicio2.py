valores = []
valores100 = []
valor = 0
quantos = 0

for i in range (10):
    valor = int(input("Insira um valor:"))
    valores.append(valor)

    if valor > 100:
        quantos += 1
        valores100.append(valor)

print (f"Existem {quantos} valores maiores que 0")
print ("Números maiores que 100:")
print (valores100)
