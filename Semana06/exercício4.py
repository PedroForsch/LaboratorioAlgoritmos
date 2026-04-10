jogadores = 0
idade = 0
salario = 0
atacante = 0
atacante1 = 0
defensores = 0
menor = 100
maior = 0

while jogadores != 10:
    salario = float(input("Insira o salario do jogador:"))
    idade = float(input("Insira a idade do jogador:"))
    aoud = input("Insira a posição do jogador(A - Atacante ; D - Defensor)").upper()
    salario += salario
    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade
    if aoud == "A":
        atacante += 1
        if salario <= 10000:
            atacante1 += 1
    elif aoud == "D":
        defensores += 1
    jogadores += 1

media = salario / 10
print (f"A média salárial é de R$ {media:.2f}")
print (f"O jogador mais novo tem {menor} anos e o jogador mais velho tem {maior} anos")
print (f"A quantidade de atacantes é {atacante} e a quantidade de defensores é {defensores}")
print (f"A quantidade de atacantes com salário até R$ 10.000,00 é {atacante1}")



