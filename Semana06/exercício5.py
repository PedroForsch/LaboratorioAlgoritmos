idade = 0
pessoas = 0
maior = 0

while pessoas != 10:
    idade = float(input("Insira a idade:"))
    if idade >= 18:
        maior += 1
    pessoas += 1
print (f"A quantidade de pessoas maiores de idade é {maior}")