def valor_compra(laranja):
    if laranja <= 12:
        total = laranja * 0.40
    elif laranja > 12:
        total = laranja * 0.25
    return total



def main():
    laranja = int(input("Quantas Laranjas você quer comprar?"))
    total = valor_compra(laranja)
    print(total)
    


main()