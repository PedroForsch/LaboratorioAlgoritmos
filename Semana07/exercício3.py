oliveiras = float(input("Insira o total de oliveiras:"))

fileiras = float(input("Insira o número de fileiras:"))

oliveirasfileira = oliveiras / fileiras
print (f"A quantidade de oliveiras que ficará em cada fileira é {oliveirasfileira:.0f}")

if oliveiras % fileiras != 0:
    sobra = oliveiras % fileiras
    print (f"A quantidade de sobras é {sobra:.0f}")