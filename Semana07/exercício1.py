oliveiras = 0
totaloliveiras = 0
diamaior = 0
diamenor = 10000
contador = 1
menor = 0
maior = 0

while contador <= 7:
    oliveiras = int(input("Insira a quantidade de oliveiras colhidas:"))
    totaloliveiras += oliveiras
    if oliveiras > diamaior:
        diamaior = oliveiras
        maior = contador
    if diamenor > oliveiras:
        diamenor = oliveiras
        menor = contador  

    contador += 1

print(f"Total:{totaloliveiras}")
print(f"O dia com maior colheita foi {maior}")
print(f"O dia com menor colheita foi {menor}")