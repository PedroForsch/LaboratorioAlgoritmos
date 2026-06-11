def main():
    lista = []
    for x in range(15):
        loop = True
        numero = int(input("Insira um número:"))
        while loop:
                if x != numero:
                    lista.append(numero)
                    loop = False
                else:
                    print("Recusado!")
                    loop = False
    print (lista)

main()