oliveirasA = 80000
oliveirasB = 200000
anos = 0

while oliveirasA <= oliveirasB:
    oliveirasA = oliveirasA * 1.03
    oliveirasB = oliveirasB * 1.015
    anos += 1

print (oliveirasA)
print (oliveirasB)
print (f"O tempo necessário foi {anos} anos")