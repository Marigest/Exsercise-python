# Chiedi due numeri all'utente
a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))

# Algoritmo di Euclide
x, y = a, b # x prende il valore di a e y quello di b
while y != 0: # y diverso da 0
    resto = x % y #divisione
    x = y # x prende il valore di y
    y = resto # y prende il valore del resto

# Alla fine, x contiene il MCD
print(f"Il MCD di {a} e {b} è {x}") #stampa il risultato con gia' i numeri salvati nelle variabili