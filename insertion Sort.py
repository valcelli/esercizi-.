
lista=[12,11,13,5,6]

for i in range(1,len(lista)):
    #toorder contiene l'elemento da ordinare
    toorder=lista[1]
if lista[1]<lista[0]:
    lista[1]=lista[0]
    lista[0]=toorder
print(lista)
#[11,12,13,5,6]
toorder=lista[2]
for i in range(0,2):
    if lista[i]>lista[1]:
        lista[i]=lista[1]
        lista[1]=toorder
print(lista)
    


