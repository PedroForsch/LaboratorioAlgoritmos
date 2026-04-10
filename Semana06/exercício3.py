tempo = 0
corredores = 0
rapidos = 0
lentos = 0
tempototal = 0

while corredores != 7:
    tempo = float(input("Digite o tempo do corredor:"))
    if tempo < 30:
        rapidos += 1
        print (f"{rapidos} corredores terminaram em menos de 30 minutos")
    if tempo > 30 and tempo <= 60:
        lentos += 1
        print (f"{lentos} corredores terminaram entre 30 a 60 minutos")
    tempototal += tempo
    corredores += 1
    resultado = tempototal / 7
porcentagem = (lentos * 100) / 7
print (f"A média de todos os corredores é {resultado:.2f}")
print (f"{porcentagem:.2f}% dos corredores terminaram entre 30 a 60 minutos")


