# risoluzione equazione di 3 grado x^3 + 4.5 * x^2 + 3.5 * x -3 = 0 

minimo = 0.30
massimo = 0.75
b = 4.5
c = 3.5
termine_noto = -3
approssimazione = 0.00001
passaggi = 0
#calcolo automatico del valore minimo senza sottopassaggi

min_val = (minimo ** 3) + (b * (minimo ** 2)) + (c * minimo) + termine_noto
while minimo <= massimo:

    x = (minimo + massimo) / 2
    terzogrado = x ** 3
    secondogrado = x ** 2 * b
    primogrado = x * c
    soluzione = terzogrado + secondogrado + primogrado + termine_noto


    if abs(soluzione) <= approssimazione:
        break
    elif soluzione * min_val >= 0:
        minimo = x

    else:
        massimo = x

    passaggi += 1

print("la soluzione e' " , x)
print("passaggi adoperati tramite il metodo bisezione", passaggi)
