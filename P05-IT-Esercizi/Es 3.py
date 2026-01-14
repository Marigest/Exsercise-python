F_min = float(input("Inserisci la temperatura più bassa (°F): ")) #chiedi la temperatura bassa
F_max = float(input("Inserisci la temperatura più alta (°F): ")) #chiedi la temperatura alta
n_intermedi = int(input("Indica quanti valori intermedi bisogna calcolare: ")) #chiedi quanti intervalli vuoi chee ci siano intermedi

# calcolo del passo
step = (F_max - F_min) / (n_intermedi + 1) #serve a dividere lo spazio tra F_min e F_max in intervalli uniformi

# intestazione tabella
print("\n°F\t\t°C") # \n = serve per andare a capo, \t = inserisce uno spazio orizzontale simile al tasto TAB.
print("-" * 20) # "-" * 20 diventa una stringa lunga 20 trattini (tipo: ------------------------------)

# ciclo per stampare tutte le temperature
for i in range(n_intermedi + 2):  # +2 perché vogliamo includere la temperatura minima e massima
    F = F_min + i * step #prende la temperatura di partenza e aggiunge “i” volte lo step per arrivare alla temperatura corrente del ciclo
    C = (5/9) * (F - 32) #formula di conversione da Fahrenheit a Celsius
    print(f"{F:6.1f} °F\t{C:10.9f} °C") #stampa formattata con 1 decimale per Fahrenheit e 9 decimali per Celsius, come nell’esempio della tabella