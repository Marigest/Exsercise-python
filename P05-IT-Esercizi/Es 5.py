# Loop per assicurarsi che l'utente inserisca un numero valido
while True: #in questo caso TRUE perche' la nostra condizione in caso se FALSE continuera a ciclare finche' non avremo l'utente non seguira le indicazioni
    n = int(input("Inserisci un numero intero compreso tra 2 e 20: ")) #chiedi il numero e lo salvi sulla variabile n
    if 2 <= n <= 20:
        break  # esci dal ciclo se il numero è corretto
    else:
        print("Errore! Il numero deve essere compreso tra 2 e 20. Riprova.") #messaggio di errore

# Stampa delle tabelline
for i in range(1, n + 1):          # righe
    for j in range(1, n + 1):      # colonne
        print(f"{i * j:4}", end="")  # stampa il prodotto con 4 spazi di larghezza, senza andare a capo | end="": evita il ritorno a capo dopo ogni numero 
    print()  #print() senza argomenti crea il ritorno a capo alla fine di ogni riga