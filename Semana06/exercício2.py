brinquedo = 1
contador = 0

while brinquedo != 0:
    brinquedo = int(input("Digite o código do brinquedo:"))
    if brinquedo == 1040:
        contador += 1
        print (f"O número 1040 foi digitado {contador} vezes.")
