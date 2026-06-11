def main():
    lista = []
    for x in range(5):
        pergunta = int(input("Insira um número?"))
        lista.append(pergunta)
    identificar(lista)

def identificar(lista):
    duplicado = False
    
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j:
                if lista[i] == lista[j]:
                    duplicado = True
    
    if duplicado:
        print("Há duplicatas")
    if not duplicado:
        print("Distintos")

main()