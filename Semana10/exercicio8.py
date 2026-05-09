fora = 0
dento = 0
numero = 0

for contador in range (0 , 10):
    numero = int(input("Insira um número:"))

    if numero >= 10 and numero <= 20:
        dento += 1
    else:
        fora += 1

print (f"Dentro:{dento}")
print (f"Fora:{fora}")
