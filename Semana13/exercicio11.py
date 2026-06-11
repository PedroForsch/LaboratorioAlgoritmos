import random

def main():
    lista = []
    for contador in range (10):
        x = random.randint(1,50)
        lista.append(x)
    print (lista)
    pares(lista)

def pares(lista):
    par = []
    impar = []
    numpar = 0
    numimpar = 0
    for x in lista:
        if x % 2 == 0:
            numpar += 1
        if x % 2 != 0:
            numimpar += 1
    print (f"Existem {numimpar} números impares")
    print (f"Existem {numpar} números pares")

main()