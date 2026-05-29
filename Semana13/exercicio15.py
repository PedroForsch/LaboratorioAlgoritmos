#Regra: o array só aceita códigos pares. Se o usuário digitar ímpar, mostre erro e volte ao menu.
def menu(opcao):
    print('1 - Inserir lote')
    print('2 - Listar lotes')
    print('3 - Retirar um lote')
    print('4 - Limpar todos os lotes')
    print('5 - Contar quantos lotes têm produção maior que X (X informado pelo usuário)')
    print('6 - Verificar se um código está presente')
    print('7 - Encontrar maior e menor código no array')
    print('8 - Sair')
    opcao = int (input('Opção: '))
    return opcao

def inserirLote(listaLotes):
    lote = 1
    while lote % 2 == 1:
        lote = int(input("Insira o lote:"))
        if lote % 2 == 0:
            listaLotes.append(lote)
        elif lote % 2 == 1:
            lote = 0
    print (f"A lista de lotes é {listaLotes}")
    return listaLotes

def listaLote(listaLotes):
    print (f"A lista de lotes é {listaLotes}")
    return listaLotes

def retirarLote(listaLotes):
    lote = int(input("Qual lote você deseja retirar?"))
    listaLotes.remove(lote)
    print (f"A lista de lotes é {listaLotes}")
    return listaLotes

def verificarProdução(listaLotes):
    producao = []
    x = int(input("Qual a produção?"))
    producao = [j for j in listaLotes if j > x]
    print (f"Os lotes maiores que a produção são {producao}")
    return listaLotes

def limparLotes(listaLotes):
    for x in range (len(listaLotes)):
        listaLotes.pop()
    print (f"A lista de lotes é {listaLotes}")
    return listaLotes

def verificarCodigo(listaLotes):
    verificar = int(input("Qual código deseja verificar?"))
    for x in range (len(listaLotes)):
        if verificar == listaLotes[x]:
            print(f"O código {verificar} está presente!")
            return
    print(f"O código {verificar} não está presente!")

def maiorMenorCodigo(listaLotes):
    maior = listaLotes[0]
    menor = listaLotes[0]
    for x in listaLotes:
        if x > maior:
            maior = x
        if x < menor:
            menor = x
    print (f"O menor código é {menor}")
    print (f"O maior código é {maior}")
    return

def main():
    opcao = 0
    listaLotes = []
    while opcao != 8:
        opcao = menu(opcao)
        if opcao == 1:
            listaLotes = inserirLote(listaLotes)
        elif opcao == 2:
            listaLotes = listaLote(listaLotes)
        elif opcao == 3:
            listaLotes = retirarLote(listaLotes)
        elif opcao == 4:
            listaLotes = limparLotes(listaLotes)
        elif opcao == 5:
            verificarProdução(listaLotes)
        elif opcao == 6:
            verificarCodigo(listaLotes)
        elif opcao == 7:
            maiorMenorCodigo(listaLotes)
        elif opcao == 8:
            print ("Saindo...")
        else:
            print ("Inválido!")
main()