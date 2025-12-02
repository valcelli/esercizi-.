def sommaLista (lista):
    somma=0
    for element in lista:
        somma=somma + element
    print(somma)

#generica espressione di funzione, la funzione non viene eseguita
lista=[1,2,3,4]
sommaLista(lista)
#ora funzione
lista2=[2,3,4,5]
sommaLista(lista2)

# scrivere una funzione che data una lista stampi a video
#il numero degli elementi pari

def numeriP (lista):
    contatore=0
    for elemnt in lista:
        if contatore % 2 == 0:
            contatore= contatore + 1
    print(contatore) 
        
        
lista = [1,2,3,4]
sommaLista(lista)
numeriP(lista)
lista2 = [2,3,4,5]
sommaLista(lista2)
numeriP(lista2)