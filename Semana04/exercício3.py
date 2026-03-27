
time1 = int(input("Qual a pontuação do primeiro time:"))

time2 = int(input("Qual a pontuação do segundo time:"))

if time1 > time2:
    print ("O primeiro time ganhou")
    print ("O segundo time perdeu")
elif time2 > time1:
    print ("O segundo time ganhou")
    print ("O primeiro time perdeu")
elif time1 == time2:
    print ("Houve um empate")