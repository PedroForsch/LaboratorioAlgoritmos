sexo = 0
sexoM = 0
sexoF = 0
olhos = 0
olhoazul = 0
olhoverde = 0
olhocastanho = 0
cabelo = 0
cabeloloiro = 0
cabelocastanho = 0
cabelopreto = 0
idade = 0
maioridade = 0
ponto1 = 0

for contagem in range (1 , 16):
    sexo = input("M ou F?").upper()
    olhos = input ("Azul, Verde ou Castanho?").lower()
    cabelo = input ("Loiro, Castanho ou Preto?").lower()
    idade = int(input("Qual sua idade?"))

    if sexo == "M":
        sexoM += 100
    elif sexo == "F":
        sexoF += 100

    if olhos == "azul":
        olhoazul += 100
    elif olhos == "verde":
        olhoverde += 100
    elif olhos == "castanho":
        olhocastanho += 100

    if cabelo == "loiro":
        cabeloloiro += 100
    elif cabelo == "castanho":
        cabelocastanho += 100
    elif cabelo == "preto":
        cabelopreto += 100

    if idade > maioridade:
        maioridade = idade
    
    if idade <= 35 and idade >= 18 and olhos == "verde" and cabelo == "preto":
        ponto1 += 1

print (f"A maior idade do grupo é:{maioridade}")
print (f"A quantidad de indivíduos é:{ponto1}")

porcentagemazul = (olhoazul * 15) / 100
print (f"A porcentagem de olhos azuis é {porcentagemazul}%")

porcentagemverde = (olhoverde * 15) / 100
print (f"A porcentagem olhos verde é {porcentagemverde}%")

porcentagemolhocastanho = (olhocastanho * 15) / 100
print (f"A porcentagem de olhos castanhos é {porcentagemolhocastanho}% ")

porcentagemloiro = (cabeloloiro * 15) / 100
print (f"A porcentagem de cabelos loiros é {porcentagemloiro}%")

porcentagempreto = (cabelopreto * 15) / 100
print (f"A porcentagem de cabelos pretos é {porcentagempreto}%")

porcentagemcastanho = (cabelocastanho * 15) / 100
print (f"A porcentagem de cabelos castanhos é {porcentagemcastanho}%")

porcentagemM = (sexoM * 15) / 100
print (f"A porcentagem de sexo masculino é {porcentagemM}%")

porcentagemF = (sexoF * 15) / 100
print (f"A porcentagem de sexo feminino é {porcentagemF}%")
