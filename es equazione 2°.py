#scrivere un programma per il calcolo delle radici di un'equazione
#di secondo grado

def calcoloDelta (a,b,c):
    delta=(b*b)-(4*a*c)
    return (delta)

def controllaDelta(delta):
    if delta<0:
        print("impossibile")
    elif delta==0:
        calcoloUnaRadice(a,b)
    else:
        calcoloDueRadici(a,b,delta)

def calcoloUnaRadice(a,b):
    suluzUno=-b/2*a
    print(soluzUno)
    
def calcolaDueRadici(a,b,delta):
    soluzUno=(-b+math.sqrt(delta))/2*a
    print(soluzUno)
    soluzDue=(-b+math.sqrt(delta))/2*a
    print(soluzDue)
    
    
    
if __name__ =='__main__':
    a=input("inseriesci il coefficente a")
    a=float(a)
    b=input("inseriesci il coefficente b")
    b=float(b)
    c=input("inseriesci il coefficente c")
    c=float(c)
    delta=calcoloDelta(a,b,c)
    print(delta)
    
    
    
    controllaDelta(delta,a,b,c)
    
    
     