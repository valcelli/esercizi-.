#dato un insime di punti su un piano cartesiano,
#random compresi tra l'intervallo 0,10. Calcolare il
#punto con ascissa massima e con ordinata minim.

import random
x=[]
y=[]
for i in range(0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))

    
#ascissa massima,scorrere la lista delle x, trovare il massimo e salvare l'indice
#visualizzare poi con un print il numero
massimo=x[0]
for i in range(1,20):
    if x[i]>massimo:
        massimo=x[i]
        indice_massimo=i
print(massiimo,y[indice_massimo])


massimo=y[0]
for i in range(1,20):
    if y[i]>massimo:
        massimo=y[i]
        indice_massimo=i
print(massiimo,x[indice_massimo])
    
#le tuple sono numeri raggruppati nelle parentisi tonde

punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)

    
#come accedere alla x del primo punto:
print (punti_cartesiano[0][0])
#come accedere alla y del primo punto:
print (punti_cartesiano[0][1]) 
        
