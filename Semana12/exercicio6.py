def menu():
    print('1 - sacar')
    print('2 - depositar')
    print('3 - saldo')
    print('4 - sair')
    opcao = int (input('opção: '))
    return opcao
    
def mostrarsaldo(saldo):
    print('Saldo atual: ',saldo)
    
    
def sacar(saldo):
    valor = float(input('Digite valor para saque: '))
    if valor <= saldo:
        saldo -= valor
        mostrarsaldo(saldo)
    else:
        print('saldo insuficiente')
    return saldo
    
def depositar(saldo):
    valor = float(input('Digite valor para deposito: '))
    saldo += valor
    mostrarsaldo(saldo)
    return saldo
    
    
def main():
    saldo = 0
    opcao = 0
    
    while opcao !=4:
        opcao = menu()
        if opcao == 1:
            saldo = sacar(saldo)
        elif opcao == 2:
            saldo = depositar(saldo)
        elif opcao == 3:
            mostrarsaldo(saldo)
main()