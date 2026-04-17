idade = 0
contador = 1
media = 0

 
while contador <= 15:
    idade = int(input("Insira a idade do estudante:"))
    media += idade
    contador += 1

mediatotal = media / 15
print (f"A média da turma é {mediatotal:.2f}")
if mediatotal >= 0 and mediatotal <= 25:
    print ("A turma é jovem")
elif mediatotal > 25 and mediatotal <= 60:
    print ("A turma é adulta")
elif mediatotal > 60:
    print ("A turma é idosa")