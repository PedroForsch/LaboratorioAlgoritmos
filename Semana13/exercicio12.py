def main():
    listaKG_colhidos = [1 , 2 , 3 , 4 , 5]
    listaKG_preco = [10 , 20 , 30 , 40 , 50] 
    multiplicacao(listaKG_colhidos , listaKG_preco)

def multiplicacao(listaKG_colhidos , listaKG_preco):
    listaproduto = []
    for x in range(5):
        multiplicar = listaKG_preco[x] * listaKG_colhidos[x]
        listaproduto.append(multiplicar)
    print (listaproduto)




main()