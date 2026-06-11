def main():
    lista = []

    for x in range(10):
       rfid = 0
       while rfid <= 1000:
            rfid = int(input("Insira o código:"))
            if rfid > 1000:
                lista.append(rfid)
                print (lista)
                break
            else:
                print("Erro!")      
                     
            

main()