import random

def main():
    lista = []
    for contador in range (10):
        x = random.randint(1,100)
        lista.append(x)
    print (lista)
    pares(lista)

def pares(lista):
    par = []
    for x in lista:
        if x % 2 == 0:
            par.append(x)
    print (par)

main()