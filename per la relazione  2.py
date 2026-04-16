#analisi delle temperature settimanali.
#Una stazione meteo ha registrato le temperature ( °c) di ogni ora per 7 giorni. Devi calcolare statistiche giornaliere e
#trovare la giornata più calda e più fredda della settimana. Struttura dati: lista di liste (7 giorni x 24 ore)
#varianza ci indica quando i valori che ciò si distaccano dai valori medi, derivazione standard

import random
def giorni():
    mylist=[]
    for i in range (-3,25):
        elemento=random.randint (3,25)
        mylist.append(elemento)
    return (mylist)
 
def media(mylist, arrotondamento=0):
    somma=0
    for i in range (0,len(mylist)):
        somma=somma+mylist[i]
        media= somma/len(mylist)
        media=round(media,arrotondamento)
    return (media)


def varianza(media,lista_giorni):
    somma=0
    for i in range(0,len(lista_giorni)):
        num=(lista_giorni[i]-media)**2
        somma=somma+num
        somma/(media-1)
    return(somma)
    
         

    
    
if __name__ == "__main__":
    lunedì=giorni()
    print (lunedì)
    martedì=giorni()
    print (martedì)
    mercoledì=giorni()
    print (mercoledì)
    giovedì=giorni()
    print (giovedì)
    venerdì=giorni()
    print (venerdì)
    sabato=giorni()
    print (sabato)
    domenica=giorni()
    print (domenica)
    
    media_lunedì=media(lunedì)
    print("la media del lunedì è ", media_lunedì)
    media_martedì=media(martedì)
    print("la media del martedì è ", media_martedì)
    media_mercoledì=media(mercoledì)
    print("la media del mercoledì è ", media_mercoledì)
    media_giovedì=media(giovedì)
    print("la media del giovedì è ", media_giovedì)
    media_venerdì=media(venerdì)
    print("la media del venerdì è ", media_venerdì)
    media_sabato=media(sabato)
    print("la media del sabato è ", media_sabato)
    media_domenica=media(domenica)
    print("la media del domenica è ", media_domenica)
    
    lun =varianza(media_lunedì,lunedì)
    print("la varianza del lunedi è",lunedì)
    mart=varianza(media_martedì,martedì)
    print("la varianza del martedi é",martedì)
    merc=varianza(media_mercoledì,mercoledì)
    print("la varianza del mercoledi è ",mercoledì)
    giov=varianza(media_giovedì,giovedì)
    print("la varianza del giovedi è ",giovedì)
    ven=varianza(media_venerdì,venerdì)
    print("la varianza del venerdi è ", venerdì)
    sab=varianza(media_sabato,sabato)
    print("la varianza del sabato è ",sabato)
    dom=varianza(media_domenica,domenica)
    print("la varianza della domeinca é",domenica)
    
    
