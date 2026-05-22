def dobro(valor):
    dobro = valor * 2
    print(dobro)

def triplo(valor):
    triplo = valor * 3
    print (triplo)

def main():
    valor = float(input("Insira o valor:"))
    opcao = float(input("Insira 1 - Dobro ou 2 - Triplo"))
    if opcao == 1:
        dobro(valor)
    elif opcao == 2:
        triplo(valor)

main()