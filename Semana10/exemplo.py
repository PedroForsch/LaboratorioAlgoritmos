abacate = 0 
laranja = 0
maca = 0
opcao = 0 

for pessoa in range (10):
    print ("Qual fruta você mais gosta?")
    print ("1 - Abacate")
    print ("2 - Laranja")
    print ("3 - Maçã")
    try:
        opcao = int(input("Insira a opção:"))
    except:
        print ("Digite um valor inteiro")
    if opcao == 1:
        abacate += 1
    elif opcao == 2:
        laranja += 1
    elif opcao == 3:
        maca += 1

print (f"Abacate: {abacate}")
print (f"Laranja: {laranja}")
print (f"Maçã: {maca}")


