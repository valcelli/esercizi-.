def aggiungi_voto(registro,voto):
    registro.append(voto)
    pass

def media_registro(registro,arrotonda_a=0):
    somma=0
    for voto in registro:
        somma=somma+voto
    media=somma/len(registro)
    media=round(media,arrotonda_a)
    return media

def solo_sufficienti(registro):
    solosuff=[]
    for i in range(0,len(registro)):
        if registro[i]>=6:
            solosuff.append(registro[i])
    return(solosuff)


def stampa_esito(registro):
    for element in registro:
        if element >= 6:
            print("sufficiente")
    else:
        print("recupera")
            

if __name__ == "__main__":
    classe=[6,7,5,8]
    aggiungi_voto(classe,9)
    print(media_registro(classe,arrotonda_a=1))
    sufficenze=solo_sufficienti(classe)
    print(sufficenze)
    stampa_esito(classe)
    


    