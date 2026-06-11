def main():
    lista = []
    for x in range(5):
        variavel = int(input("Insira o valor de produção:"))
        lista.append(variavel)
    print (lista)
    inverso(lista)

def inverso(lista):
    lista2 = []
    for x in range(4 , -1, -1):
        lista2.append(lista[x])
    print (lista2)

main()