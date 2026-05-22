def lerNotas():
    n1 = float(input("Digite a primeira nota:"))
    n2 = float(input("Digite a segunda nota:"))
    return n1 , n2

def calcularMedia(nota1,nota2):
    media = (nota1 + nota2) / 2
    return media

def situacao(media):
    if media >= 7:
        print("Aprovado")
    elif media >= 4 and media < 7:
        print ("Exame")
    else:
        print ("Reprovado")

def main():
    nota1, nota2 = lerNotas()
    media = calcularMedia()
    situacao(media)

main()