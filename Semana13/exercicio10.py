def main():
    lista = []
    for i in range (5):
        x = int(input("Insira um código:"))
        lista.append(x)
    verificar(lista)
def verificar(lista):
    codigo = int(input("Insira um código para verificação:"))
    for i in lista:
        if codigo == i:
            print ("O código está presente")
            return
    print("O código não está presente")

main()