#data una list di 10 elementi random interi nell'intervallo -10,+10
#calcolare il numero degli elementi pari da quelli dispari

#1) crare una lista di10 elementi random
#2) creare gli elemti pari e dispari tramite procedura

import random

def generaLista(lista): #__> procedura e il fattore (lista) viene passato per riferimento
    for i in range(0,10):
        n=random.randint(-10,10)
        lista.append(n)
    
def calcolaNumeri(lista):
    dispari=0
    pari=0
    for element in lista:#>> scorro gli elementi
        if element%2==0:
            pari=pari+1
        else:
            dispari=dispari+1
    print(pari)
    print(dispari)
    
    
def generaListaMentre(lista):
    contatore=0
    while contatore <10:
        n1=random.randint (-10,10)
        lista.append(n1)
        contatore=contatore+1
        
        
if __name__=="__main__":
    myList=[]
    myList2=[]
    generaLista(myList)
    calcolaNumeri(myList)
    generaListaMentre(myList2)
    
