# risoluzione equazione di 3 grado x^3 + 4.5 * x^2 + 3.5 * x -3 = 0 

minimo = 0.3
massimo = 0.75
b = 4.5
c = 3.5
approssimazione = 0.00001
passaggi = 0
  
while minimo < massimo:

    x = (minimo + massimo) / 2.
    val = x ** 3 + 4.5 * x ** 2 + 3.5 * x - 3
    min_val = minimo ** 3 + 4.5 * minimo ** 2 + 3.5 * minimo - 3

    if abs(val) < approssimazione:
        break
    elif val * min_val > 0:
        minimo = x

    else:
        massimo = x

    passaggi += 1

print(x)
print(passaggi)
