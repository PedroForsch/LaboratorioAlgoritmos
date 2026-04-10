
notas = 0
contador = 0 
while contador < 3:
    nota = float(input("Digite uma nota:"))
    notas = notas + nota
    contador = contador + 1


media = notas / 3
print(f"Média:{media:.2f}")
