def inverso(lista):
    lista2 = []
    for x in range (9 , -1, -1):
        lista2.append(lista[x])
    print (lista2)

def main():
    lista = [1,2,3,4,5,6,7,8,9,10]
    print (lista)
    inverso(lista)

main()