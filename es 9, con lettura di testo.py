#si vuole creare un programma che leggendo da un file di testo contenete
#una serie di valori misurati di temperatura,calcoli
#la media,la varianza e la mediana della distrubuzione.


#sotto problemi:
#1 leggere il file riga per riga e creare una lista
#2 calcolo della media della lista
#3 calcolo la varianza di una lista
#4 calcola la mediana di una lista

def leggiFile(pathInput):
    temperture=[]
    with open (pathInput) as f:
        for line in f:
            elemento=int(line.strip())
            temperature.append(elemento)
        return(temperature)
#media con l'iteratore 
def media_iterator(lista):
    somma=0
    for i in range(0,len(lista)):
        somma = somma+lista[i]
    media_c =somma/len(lista)
    print(media_c)
#richimo la funzione       
lista = leggiFile("temperature.py")
media_iterator(lista)
    