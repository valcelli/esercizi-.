misurazioni = [25.5, 24.8, 23.9, 24.2, 22.8]
# Ciclo while
i = 0
while i < len(misurazioni):
    if misurazioni[i] > 24.0:
        print("ATTENZIONE: temperatura elevata")
    i = i + 1
    

#ciclo while corretto
    
for valore in  misurazioni:
    if misurazioni [i] > 24.0:
        print("attenzione: temperatura elevata")
    i = i+1

