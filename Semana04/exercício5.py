ingresso = float(input("Insira o valor do ingresso:"))
print ("Para adulto selecione 1")
print ("Para estudante selecione 2")
print ("Para criança até 12 anos selecione 3")
print ("Para idoso selecione 4")

op = int(input("Insira a opção:"))

if op == 1:
    print (f"O valor do seu ingresso é {ingresso:.2f}")

elif op == 2:
    valortotal = ingresso * 0.50
    print(f"O valor do ingresso é {valortotal:.2f}")

elif op == 3:
    valortotal = ingresso * 0.40
    print(f"O valor do ingresso é {valortotal:.2f}")
elif op == 4:
    valortotal = ingresso * 0.60
    print(f"O valor do ingresso é {valortotal:.2f}")


