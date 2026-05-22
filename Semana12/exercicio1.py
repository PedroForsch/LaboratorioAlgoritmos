
def calcular_media():
    nota1 = float(input("Insira uma nota:"))
    nota2 = float(input("Insira outra nota:"))
    media = (nota1 + nota2) / 2
    print(media)
    return media

def aprovado_reprovado(valormedia):
    if valormedia >= 7:
        print ("Aprovado")
    else:
        print("Reprovado")

def main():
    valormedia = calcular_media()
    aprovado_reprovado(valormedia)

main()