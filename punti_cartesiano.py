#dato un insime di punti su un piano cartesiano,
#random compresi tra l'intervallo 0,10. calcolare il
#punto con ascissa massima e con ordinata minim.

import random
x=[]
y=[]
for i in range(0,20):
    x.append(random.randint(0,10))
    y.append(random.randint(0,10))
    
#le tuple sono numeri raggruppati nelle parentisi tonde
    
punti_cartesiano=[]
for i in range(0,20):
    punto=(random.randint(0,10),random.randint(0,10))
    punti_cartesiano.append(punto)
    
#come accedere alla x del primo punto:
print (punti_cartesiano[0][0])
#come accedere alla y del primo punto:
print (punti_cartesiano[0][1]) 
        
    
   
    
