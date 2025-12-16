#scrivere un programma che generi un lista di numeri ù
#casuali compresi tra 1,100 che rappresentano misurazioni di intendità
#di un segnale. Il programma dopo avere generato la lista deve essere in
#in grado di modificarla in questa maniera: gli elementi di indice pari
#devono essere azzerati. Inoltre ,dopo la modifica, si vuole contare il numero di
#elementi sopra una soglia numerica.

#sottoproblemi:
#1) generare un lista di numeri compresi tra 1,100
#2) modificare la lista con la regola sopra
#3) contare il numero elementi sopra soglia

import random
def generaLista(n):
    mylist=[]
    for i in range(0,n):
        elemento =random. randint(1,100)
        mylist.append(elemento)
    return mylist


def proceduraGeneraLista(n,lista):
    for i in range(0,n):
        elemento =random.randint(1,100)
        lista.append(elemento)
    
def soglia(n,lista,nsoglia):
    contatore=0
    for i in range(0,n):
        if lista[i]>nsoglia:
            contatore=contatore+1
        return contatore
    
def modificaLista(n,lista):
    for i in range(0,n):
        if i%2==0:
            lista[i]=0
            


listaX = generaLista(6)
listaP = []
proceduraGeneraLista(6,listaP)
proceduraGeneraLista(lista=listaP, n=6)
modificaLista(6,listaX)
nsoglia = soglia(6,listaX,50)
