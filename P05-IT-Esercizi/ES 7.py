n = int(input("Inserisci un numero intero: ")) # chiedi all'utente di inserire un numero

# controllo dei casi in cui n non è primo
if n <= 1:
    print(f"{n} NON è un numero primo.") #print(f"{variabile} qualcosa"): serve per inserire il valore di una variabile dentro una stringa in modo semplice e leggibile
else:
    primo = True # variabile per tenere traccia se troviamo un divisore
    
    # controlla tutti i numeri da 2 fino a n-1
    for i in range(2, n):
        if n % i == 0:  # se n è divisibile per i (che parte da 2) | == 0 serve per comparare 0 con 0 (es 2/2 = 0... 0 e' uguale a 0... si, quindi il numeno non e' primo)
            primo = False
            break  # non serve controllare oltre

    
    # stampa il risultato
    if primo:
        print(f"{n} è un numero primo!") #stampa in output se e' il numero e' primo (grazie al cabbo)
    else:
        print(f"{n} NON è un numero primo.") #stampa in output se non e' il numero e' primo (grazie al cabbo)