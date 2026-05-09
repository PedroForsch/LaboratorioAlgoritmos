sequencia = 0
atual = 1
passado = 0

for contador in range (0 , 10):
    print (f"{sequencia}")
    passado = atual
    atual = sequencia + atual
    sequencia = passado
    
