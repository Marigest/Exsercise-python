# Chiedi all'utente il numero di elementi della serie
n = int(input("Inserisci il numero di elementi della serie di Fibonacci: ")) #chiedi all'utente il numero di elementi che poi vai a salvare in n

# Controllo minimo
if n <= 0:
    print("Errore! Inserisci un numero intero positivo.")
else:
    # Inizializzo i primi due elementi della serie
    fib1 = 1
    fib2 = 1

    print("Serie di Fibonacci:", end=" ") #RICORDO: end="": evita il ritorno a capo dopo ogni numero

    for i in range(1, n + 1): #range(1, n + 1) genera tutti i numeri da 1 a n inclusi | "i" rappresenta la posizione corrente nella serie di Fibonacci
        if i == 1 or i == 2: # ==: serve a comparare due numeri e capire se sono uguali. In questo caso se i == 1 oppure i == 2 svolgera il print, in caso contrario svolgera' elese
            # I primi due elementi sono 1
            print(1, end=" ")
        else:
            # Calcola il prossimo elemento
            fib_n = fib1 + fib2
            print(fib_n, end=" ")
            # Aggiorna i valori precedenti
            fib1, fib2 = fib2, fib_n

    print()  #stampa un ritorno a capo (puoi anche tralasciarlo, ma da un tocco si stile e pulizia del programma in output)