oliveiras = 0
variavel = 67

while oliveiras != variavel:
    oliveiras = float(input("Digite um número entre 1 a 100:"))

    if oliveiras > variavel:
        print(f"Há menos oliveiras, tente um número menor")
    elif oliveiras < variavel:
        print(f"Há mais oliveiras, tente um número maior")
    elif oliveiras == variavel:
        print(f"Parabéns!Você descobriu a quantidade de oliveiras!")