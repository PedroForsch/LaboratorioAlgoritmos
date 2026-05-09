pares = 0
impares = 0
zero = 0
numero = 0
divisao = 1

for contador in range (1,11):
    numero = int(input("Insira um número inteiro:"))
    if numero == 0:
        zero += 1
    elif numero % 2 == 0:
        pares += 1
    elif numero % 2 != 0:
        impares += 1

print (f"Pares:{pares}")
print (f"Impares:{impares}")
print (f"Zeros:{zero}")