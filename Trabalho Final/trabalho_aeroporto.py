from datetime import datetime, timedelta
from calendar import monthrange
import math
import time

#-------------------------------------------------------------------------------------------------------------------------------

def menu():
    print('1 - Solicitar uma vaga para uma aeronave.')
    print('2 - Retirar uma aeronave do estacionamento.')
    print('3 - Retirar todas as aeronaves do estacionamento.')
    print('4 - Mostrar todas as aeronaves presentes no estacionamento.')
    print('5 - Adiantar o tempo.')
    print('6 - Mostrar informacoes do tempo do algoritmo.')
    print('7 - Grafico.')
    print('8 - Sair.')
    opcao = input('Digite uma opcao: ').strip().lower()
    return opcao

#-------------------------------------------------------------------------------------------------------------------------------

def formatarDataHora(dataHora):
    return dataHora.strftime('%d/%m/%Y %H:%M:%S')

#-------------------------------------------------------------------------------------------------------------------------------

def registrarHistorico(historico, tempoAtual, estacionamento, listaEspera, acao):
    historico.append({
        'dataHora': tempoAtual,
        'estacionamento': len(estacionamento),
        'listaEspera': len(listaEspera),
        'acao': acao
    })
    return historico

#-------------------------------------------------------------------------------------------------------------------------------

def calcularValorEstacionamento(entrada, saida):
    diferenca = saida - entrada
    diarias = math.ceil(diferenca.total_seconds() / 86400)

    if diarias < 1:
        diarias = 1

    if diarias > 30:
        valorDiaria = 115
    else:
        valorDiaria = 127

    valorTotal = diarias * valorDiaria
    return diarias, valorDiaria, valorTotal

#-------------------------------------------------------------------------------------------------------------------------------

def solicitarVaga(estacionamento, listaEspera, temposEntrada, tempoAtual, totalEstacionamentos):
    inserir = int(input("Digite o codigo da aeronave: "))

    if inserir in estacionamento or inserir in listaEspera:
        print("Essa aeronave ja esta no estacionamento ou na lista de espera.")
        return estacionamento, listaEspera, temposEntrada, totalEstacionamentos

    if len(estacionamento) < 5:
        estacionamento.append(inserir)
        temposEntrada.append(tempoAtual)
        totalEstacionamentos += 1
        print(f"Aeronave estacionada em {formatarDataHora(tempoAtual)}.")
    else:
        if len(listaEspera) == 1:
            print("Aeroporto cheio!! Enviando para outro aeroporto.")
        elif len(listaEspera) < 1:
            print("Espaco insuficiente! Inserindo na lista de espera...")
            listaEspera.append(inserir)

    return estacionamento, listaEspera, temposEntrada, totalEstacionamentos

#-------------------------------------------------------------------------------------------------------------------------------

def alocarAeronaveDaEspera(estacionamento, listaEspera, temposEntrada, tempoAtual, totalEstacionamentos):
    if len(listaEspera) > 0 and len(estacionamento) < 5:
        codigoAeronave = listaEspera.pop(0)
        estacionamento.append(codigoAeronave)
        temposEntrada.append(tempoAtual)
        totalEstacionamentos += 1
        print(f"Aeronave {codigoAeronave} saiu da espera e entrou no estacionamento em {formatarDataHora(tempoAtual)}.")

    return estacionamento, listaEspera, temposEntrada, totalEstacionamentos

#-------------------------------------------------------------------------------------------------------------------------------

def retirarAeronave(estacionamento, listaEspera, temposEntrada, tempoAtual, totalRetiradas, valorCaixa, totalEstacionamentos):
    retirar = int(input("Digite o codigo da aeronave que deseja retirar do estacionamento: "))

    if retirar not in estacionamento:
        print("Aeronave nao encontrada no estacionamento.")
        return estacionamento, listaEspera, temposEntrada, totalRetiradas, valorCaixa, totalEstacionamentos

    indice = estacionamento.index(retirar)
    entrada = temposEntrada[indice]
    estacionamento.pop(indice)
    temposEntrada.pop(indice)

    diarias, valorDiaria, valorTotal = calcularValorEstacionamento(entrada, tempoAtual)
    totalRetiradas += 1
    valorCaixa += valorTotal

    print(f"Aeronave {retirar} retirada em {formatarDataHora(tempoAtual)}.")
    print(f"Entrada: {formatarDataHora(entrada)}")
    print(f"Diarias cobradas: {diarias}")
    print(f"Valor da diaria: R${valorDiaria:.2f}")
    print(f"Valor total: R${valorTotal:.2f}")

    estacionamento, listaEspera, temposEntrada, totalEstacionamentos = alocarAeronaveDaEspera(
        estacionamento, listaEspera, temposEntrada, tempoAtual, totalEstacionamentos
    )

    return estacionamento, listaEspera, temposEntrada, totalRetiradas, valorCaixa, totalEstacionamentos

#-------------------------------------------------------------------------------------------------------------------------------

def retirarTudo(estacionamento, listaEspera, temposEntrada, tempoAtual, totalRetiradas, valorCaixa):
    if len(estacionamento) == 0 and len(listaEspera) == 0:
        print("Estacionamento e lista de espera ja estao vazios.")
        return estacionamento, listaEspera, temposEntrada, totalRetiradas, valorCaixa

    valorRetiradaTotal = 0
    retiradasNestaAcao = 0

    while len(estacionamento) > 0:
        codigoAeronave = estacionamento.pop(0)
        entrada = temposEntrada.pop(0)
        diarias, valorDiaria, valorTotal = calcularValorEstacionamento(entrada, tempoAtual)

        totalRetiradas += 1
        retiradasNestaAcao += 1
        valorCaixa += valorTotal
        valorRetiradaTotal += valorTotal

        print(f"Aeronave {codigoAeronave} retirada.")
        print(f"Entrada: {formatarDataHora(entrada)} | Diarias: {diarias} | Valor: R${valorTotal:.2f}")

    listaEspera.clear()
    print("Estacionamento e lista de espera limpos!!")
    print(f"Total de retiradas nesta acao: {retiradasNestaAcao}")
    print(f"Valor recebido nesta acao: R${valorRetiradaTotal:.2f}")

    return estacionamento, listaEspera, temposEntrada, totalRetiradas, valorCaixa

#-------------------------------------------------------------------------------------------------------------------------------

def mostrarAeronaves(estacionamento, listaEspera):
    print(f"Estacionamento: {estacionamento}")
    print(f"Lista de espera: {listaEspera}")

#-------------------------------------------------------------------------------------------------------------------------------

def mostrarCodigosEEntradas(estacionamento, listaEspera, temposEntrada):
    if len(estacionamento) == 0:
        print("Nao existem aeronaves no estacionamento.")
    else:
        print("Aeronaves no estacionamento:")
        for indice in range(len(estacionamento)):
            print(f"Codigo: {estacionamento[indice]} | Entrada: {formatarDataHora(temposEntrada[indice])}")

    if len(listaEspera) > 0:
        print(f"Aeronave na lista de espera: {listaEspera[0]}")
        print("A aeronave da espera ainda nao possui data e hora de entrada no estacionamento.")

#-------------------------------------------------------------------------------------------------------------------------------

def adicionarMeses(dataHora, meses):
    mesCalculado = dataHora.month - 1 + meses
    ano = dataHora.year + mesCalculado // 12
    mes = mesCalculado % 12 + 1
    dia = min(dataHora.day, monthrange(ano, mes)[1])
    return dataHora.replace(year=ano, month=mes, day=dia)

#-------------------------------------------------------------------------------------------------------------------------------

def adiantarTempo(tempoAtual):
    tipo = input("Deseja adiantar em dias ou meses? Digite D para dias ou M para meses: ").strip().lower()
    quantidade = int(input("Digite a quantidade: "))

    if quantidade <= 0:
        print("A quantidade precisa ser maior que zero.")
        return tempoAtual

    if tipo == 'd':
        tempoAtual = tempoAtual + timedelta(days=quantidade)
        print(f"Tempo adiantado em {quantidade} dia(s).")
    elif tipo == 'm':
        tempoAtual = adicionarMeses(tempoAtual, quantidade)
        print(f"Tempo adiantado em {quantidade} mes(es).")
    else:
        print("Opcao invalida. O tempo nao foi alterado.")

    print(f"Data e hora atual do sistema: {formatarDataHora(tempoAtual)}")
    return tempoAtual

#-------------------------------------------------------------------------------------------------------------------------------

def mostrarInformacoesTempo(tempoAtual, inicioAlgoritmo):
    tempoExecucao = time.perf_counter() - inicioAlgoritmo
    print(f"Data e hora atual do sistema: {formatarDataHora(tempoAtual)}")
    print(f"Tempo de execucao do algoritmo: {tempoExecucao:.4f} segundos")

#-------------------------------------------------------------------------------------------------------------------------------

def mostrarGrafico(historico):
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        print("Biblioteca matplotlib nao encontrada. Instale com: pip install matplotlib")
        return

    if len(historico) == 0:
        print("Ainda nao existem dados para gerar o grafico.")
        return

    eventos = list(range(len(historico)))
    ocupacaoEstacionamento = []
    ocupacaoEspera = []

    for registro in historico:
        ocupacaoEstacionamento.append(registro['estacionamento'])
        ocupacaoEspera.append(registro['listaEspera'])

    plt.figure(figsize=(9, 5))
    plt.plot(eventos, ocupacaoEstacionamento, marker='o', label='Aeronaves no estacionamento')
    plt.plot(eventos, ocupacaoEspera, marker='o', label='Aeronaves na lista de espera')
    plt.title('Ocupacao do estacionamento ao longo do algoritmo')
    plt.xlabel('Eventos registrados')
    plt.ylabel('Quantidade de aeronaves')
    plt.ylim(0, 6)
    plt.xticks(eventos)
    plt.grid(True)
    plt.legend()
    plt.show()

#-------------------------------------------------------------------------------------------------------------------------------

def mostrarResumoFinal(totalEstacionamentos, totalRetiradas, valorCaixa):
    print("Encerrando o algoritmo...")
    print(f"Total de estacionamentos realizados com sucesso: {totalEstacionamentos}")
    print(f"Total de retiradas de aeronaves: {totalRetiradas}")
    print(f"Valor em caixa: R${valorCaixa:.2f}")

#-------------------------------------------------------------------------------------------------------------------------------

def main():
    estacionamento = []
    listaEspera = []
    temposEntrada = []
    tempoAtual = datetime.now()
    inicioAlgoritmo = time.perf_counter()
    historico = []
    totalEstacionamentos = 0
    totalRetiradas = 0
    valorCaixa = 0

    historico = registrarHistorico(historico, tempoAtual, estacionamento, listaEspera, 'Inicio')

    while True:
        opcao = menu()

        if opcao == '1':
            estacionamento, listaEspera, temposEntrada, totalEstacionamentos = solicitarVaga(
                estacionamento, listaEspera, temposEntrada, tempoAtual, totalEstacionamentos
            )
            historico = registrarHistorico(historico, tempoAtual, estacionamento, listaEspera, 'Solicitar vaga')
            print(f"Estacionamento: {estacionamento}")
            print(f"Lista de espera: {listaEspera}")

        elif opcao == '2':
            estacionamento, listaEspera, temposEntrada, totalRetiradas, valorCaixa, totalEstacionamentos = retirarAeronave(
                estacionamento, listaEspera, temposEntrada, tempoAtual, totalRetiradas, valorCaixa, totalEstacionamentos
            )
            historico = registrarHistorico(historico, tempoAtual, estacionamento, listaEspera, 'Retirar aeronave')
            print(f"Estacionamento: {estacionamento}")
            print(f"Lista de espera: {listaEspera}")

        elif opcao == '3':
            estacionamento, listaEspera, temposEntrada, totalRetiradas, valorCaixa = retirarTudo(
                estacionamento, listaEspera, temposEntrada, tempoAtual, totalRetiradas, valorCaixa
            )
            historico = registrarHistorico(historico, tempoAtual, estacionamento, listaEspera, 'Retirar tudo')
            print(f"Estacionamento: {estacionamento}")
            print(f"Lista de espera: {listaEspera}")

        elif opcao == '4':
            mostrarAeronaves(estacionamento, listaEspera)
            mostrarCodigosEEntradas(estacionamento, listaEspera, temposEntrada)

        elif opcao == '5':
            tempoAtual = adiantarTempo(tempoAtual)
            historico = registrarHistorico(historico, tempoAtual, estacionamento, listaEspera, 'Adiantar tempo')

        elif opcao == '6':
            mostrarInformacoesTempo(tempoAtual, inicioAlgoritmo)

        elif opcao == '7':
            mostrarGrafico(historico)

        elif opcao == '8':
            mostrarResumoFinal(totalEstacionamentos, totalRetiradas, valorCaixa)
            break

        else:
            print("Opcao invalida.")

main()
