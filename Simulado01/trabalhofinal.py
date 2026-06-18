from datetime import date



#-------------------------------------------------------------------------------------------------------------------------------

def menu():
    print('1 - Solicitar uma vaga para uma aeronave.')
    print('2 - Retirar uma aeronave do estacionamento.')
    print('3 - Retirar todas as aeronaves do estacionamento.')
    print('4 - Mostrar todas as aeronaves presentes no estacionamento.')
    print('5 - Adiantar o tempo ')
    print('6 - Mostrar informações do tempo do algoritmo.')
    print('7 - Gráfico')
    print('8 - Sair')
    opcao = int(input('Digite uma opção: '))
    return opcao


#-------------------------------------------------------------------------------------------------------------------------------

def solicitarVaga(estacionamento , listaEspera):
    if len(estacionamento) <= 4:
            inserir = int(input("Digite o código da aeronave:"))
            estacionamento.append(inserir)
    else:
        if len(listaEspera) == 1:
            print ("Aeroporto cheio!! Enviando para outro aeroporto.")
        elif len(listaEspera) < 1:
            print ("Espaço Insuficiente! Inserindo na lista de espera...")
            inserir = int(input("Digite o código da aeronave:"))
            listaEspera.append(inserir)
    return estacionamento, listaEspera

#-------------------------------------------------------------------------------------------------------------------------------

def retirarAeronave(estacionamento , listaEspera):
    retirar = int(input("Digite o código da aeronave que deseja retirar do estacionamento:"))
    estacionamento.remove(retirar)
    estacionamento.extend(listaEspera)
    listaEspera.clear()
    return estacionamento , listaEspera

#-------------------------------------------------------------------------------------------------------------------------------

def retirarTudo(estacionamento , listaEspera):
    estacionamento.clear()
    listaEspera.clear()
    print ("Estacionamento e Lista limpos!!")
    return estacionamento , listaEspera

#-------------------------------------------------------------------------------------------------------------------------------

def mostrarAeronaves(estacionamento , listaEspera):
    print (f"Estacionamento: {estacionamento}")
    print (f"Lista de Espera: {listaEspera}")

#-------------------------------------------------------------------------------------------------------------------------------

def main():
    estacionamento = []
    listaEspera = []
    while True:
        opcao = menu()
        if opcao == 1:
            estacionamento , listaEspera = solicitarVaga(estacionamento , listaEspera)
            print (f"Estacionamento: {estacionamento}")
            print (f"Lista de Espera: {listaEspera}")
        if opcao == 2:
            estacionamento , listaEspera = retirarAeronave(estacionamento , listaEspera)
            print (f"Estacionamento: {estacionamento}")
            print (f"Lista de Espera: {listaEspera}")
        if opcao == 3:
            estacionamento , listaEspera = retirarTudo(estacionamento , listaEspera)
            print (f"Estacionamento: {estacionamento}")
            print (f"Lista de Espera: {listaEspera}")
        if opcao == 4:
            mostrarAeronaves(estacionamento , listaEspera)
        elif opcao == 8:
            break

main()