cidades = 0
temperatura = 0
C = 0

while cidades != 10:
    temperatura = float(input("Insira a temperatura:"))
    if temperatura >= 15 and temperatura <=25:
        C += 1
    cidades += 1
print (f"{C} cidades ficaram entre 15C e 25C")