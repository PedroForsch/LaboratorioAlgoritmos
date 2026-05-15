valores = []
valorespares = []
valoresposicao = []
valor = 0


for i in range (10):
    valor = int(input("Insira um valor:"))
    valores.append(valor)

    if valor % 2 == 0:
        valorespares.append(valor)
        
for x in range(len(valores)):
    if valores[x] % 2 == 0:
         print (f"Posição {x}:{valores[x]}")

print (valorespares)

