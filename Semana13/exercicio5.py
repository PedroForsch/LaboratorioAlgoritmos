def main():
    indice = []
    for i in range (5):
        x = float(input("Insira a produção:"))
        indice.append(x)
    print (indice)
    maiorMenor(indice)

def maiorMenor (indice):
    maior = indice[0]
    menor = indice[0]
    for x in indice:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    print (f"O maior número é {maior}")
    print (f"O menor número é {menor}")
    indiceArvore(indice)

def indiceArvore(indice):
    for x in range (5):
        print (f"Árvore {x + 1} - Indice {indice[x]}")

main()