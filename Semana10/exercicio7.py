menor = int(input("Insira um número:"))
maior = int(input("Insira um número:"))
pares = 0

for contagem in range (menor , maior):
    if contagem % 2 == 0:
        pares +=1

print (pares)