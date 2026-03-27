h = float(input("Digite sua altura:"))
sexo = input("Digite seu gênero(H ou F):").upper()

if sexo =="M":
    pesofeminino = (62.1 * h) - 44,7
    print ("Seu peso é", pesofeminino, "KG")

if sexo =="H":
    pesomasc = (72.7 * h) - 58
    print ("Seu peso é", pesomasc, "KG")

    
