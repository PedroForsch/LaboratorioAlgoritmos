import random

def main():
    colheita = []
    for i in range(5):
        while True:
            try:
                valor = float(input(f"Força do lote {i+1}: "))
                colheita.append(valor)
                break
            except ValueError:
                print("Entrada inválida. Digite um número válido.")
    pragas = random.sample(range(1 , 101), 5)
    confronto(pragas , colheita)

def confronto (pragas , colheita):
    protegido = 0
    perdido = 0
    final = []

    for x in range (5):
        if colheita[x] > pragas[x]:
            print (f"O lote {x + 1} ganhou!")
            protegido += 1
            final.append(colheita[x])
        else:
            print (f"A praga {x + 1} ganhou!")
            perdido += 1
            final.append(pragas[x])

    print (f"A força das equipes são {colheita}")
    print (f"A força das pragas são {pragas}")
    print (f"Foram perdidos {perdido} lotes!")
    print (f"Foram protegidos {protegido} lotes!")



    


main()