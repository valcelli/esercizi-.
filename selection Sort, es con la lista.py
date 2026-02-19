from kallax import *

lista[5,3,8,1,2]

for i in range(0,len(lista)):
    #trovo il minimo
    minimo=minimoLista(lista[i:])
    #trova l'indice del minimo
    indice_minimo=lista[i:].index(minimo)
    #scambio
    lista[indice_minimo]=lista[i]
    lista[i]=minimo


    
