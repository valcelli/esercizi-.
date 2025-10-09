#creazione un dizzionario

tom={}

#inserire un elemento nel dizzionario

tom["primo"]=2
tom["secondo"]=4

#creazione di un secondo dizzionario con inizializzazione

sam={"primo":6,"secondo":8}

#accedere agli elementi del dizzionario
tom["primo"]+sam["primo"]

#scorrere gli elementi di un dizzionario
for key, value in tom.items():
    print ("la chiave è: + key")
    print ("il valore corrispondente è:" +str(value))
           