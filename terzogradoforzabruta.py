#risoluzione equazione di 3 grado x^3 + 4.5 * x^2 + 3.5 * x -3 = 0 

b = 4.5
c = 3.5
passaggi = 0
i = 0.3
massimo = 0.75
incremento = 0.001
approssimazione = 0.00001
while i < massimo:
    passaggi += 1
    terzogrado = i ** 3
    secondogrado = i ** 2
    soluzione = abs(terzogrado + secondogrado * b + i * c + (-3)) #la presenza del termine -3 potrebbe far scaturire dei numeri con la virgola
    if soluzione < approssimazione: 
        break
    else:
        i += incremento
        

#for i in range(0,30.75,0.001): non funziona!!!
   
   
print(i)
print(passaggi)
