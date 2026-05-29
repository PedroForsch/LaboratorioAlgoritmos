def inserir(azeitonas):
    for i in range(8):
        inserir1 = int(input("Insira a quantidade da produção:"))
        azeitonas.append(inserir1)
    return azeitonas    

def mediana(media , azeitonas):
    for x in range(8):
        media += azeitonas[x]
    media = media / 8
    print (media)
    return media

def acima_media(acimadamedia , media , azeitonas):
    acimadamedia = [j for j in azeitonas if j >= media]        
    print (f"Os elementos acima da média são {acimadamedia}")
    return acimadamedia

def main():
    media = 0
    acimadamedia = []
    azeitonas = []
    azeitonas = inserir(azeitonas)
    media = mediana(media , azeitonas)
    acimadamedia = acima_media(acimadamedia , media , azeitonas)
    print (azeitonas)

main()