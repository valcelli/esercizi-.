
lista=[12,11,13,5,6]

for i in range(1,len(lista)):
    #toorder contiene l'elemento da ordinare
    toorder=lista[1]
if lista[1]<lista[0]:
    lista[1]=lista[0]
    lista[0]=toorder
print(lista)
    


