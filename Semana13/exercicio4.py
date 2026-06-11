def main():
    lista = []
    for x in range(5):
        variavel = int(input("Insira o valor de produção:"))
        lista.append(variavel)
    print (lista)
    soma(lista)

def soma(lista):
    soma = 0
    media = 0
    for x in range (5):
       soma += lista[x]
       media = soma / 5
    print (f"A soma é {soma}")
    print (f"A média é {media}")

main()