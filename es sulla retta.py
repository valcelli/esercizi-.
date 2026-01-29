#scrivere un programma che dati due punti in un piano cartesiano
#scriva l'equazione della retta associata e mandi in output il
#mesaggio con la positività del coefficente angolare

#1- m=y-y/x-x ---->> questa è una funzione  [parametri (xUno,xDue,xTre,XQuattro)]
#2- y-y=m(x-x) ----->> questa è una procedura   [parametri (m,xDue,xTre)]
import random
def calcolo_m(xUno,xDue,yUno,yDue):
    m=(yDue-yUno)/(xDue-xUno)
    return (m)


def equazione(m,x,y):
    eq="y"+str(y)+"="+str(m)+"(x-"+str(x)+")"  #--->succesione di stringhe, faato un messagio e il +serve per conatenate le stringhe, inizi la stringa da una parte
#fissa +il valore di y che è variabile.
    print(eq)
    
def controllo_m(m):
    if m>0:
        print("m ha segno positivo")
    elif m==0:
        print("mè nullo")
    else:
        print("m ha segno negativo")
    
if __name__ =='__main__':
    xUno=random.randint(-20,20)
    xDue=random.randint(-20,20)
    yUno=random.randint(-20,20)
    yDue=random.randint(-20,20)

    
    coefficente_angolare=calcolo_m(xUno,xDue,yUno,yDue)
    print(coefficente_angolare)
    equazione(coefficente_angolare,xDue,yDue)
    controllo_m(coefficente_angolare)