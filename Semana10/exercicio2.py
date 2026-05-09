numero = 0
media = 0

for contador in range (1 , 11):
    numero = float(input("Insira um número:"))
    media += numero

media = media / 10
print (f"{media}")