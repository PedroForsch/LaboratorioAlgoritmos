def main():
    azeitona = [ ]
    for j in range (6):
        lista = int(input("Insira a quantidade de Kgs:"))       
        azeitona.append(lista)
    print (azeitona)
    extrato = porcentagem()
    listaMultiplicada = multiplicacao(azeitona , extrato)
    print (listaMultiplicada)

def porcentagem():
    x = int(input("Insira uma porcentagem: "))
    print(f"A porcentagem é {x / 100}")
    return x / 100
    

def multiplicacao(azeitona , extrato):
    listaMultiplicada = []
    for item in azeitona:
        listaMultiplicada.append(item * extrato)
    return listaMultiplicada
main()