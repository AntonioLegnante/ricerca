#risoluzione equazione di 3 grado x^3 + 4.5 * x^2 + 3.5 * x -3 = 0 

b = 4.5
c = 3.5
x = 0.3
termine_noto = -3

passaggi = 0
massimo = 0.75
incremento = 0.001
approssimazione = 0.00001


while x < massimo:
    passaggi += 1
    terzogrado = x ** 3
    secondogrado = x ** 2 * b
    primogrado = x * c
    soluzione = terzogrado + secondogrado + primogrado + termine_noto #la presenza del termine -3 potrebbe far scaturire dei numeri con la virgola

    if abs(soluzione) < approssimazione: 
        break
    else:
        x += incremento
        
   
print("la soluzione e' ", x)
print("numero di passaggi con forza bruta ", passaggi)
