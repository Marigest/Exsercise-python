giorno = int(input("Inserisci il giorno: ")) #chiedi il giorno e lo salvi
mese = int(input("Inserisci il mese: ")) #Chiedi il mese e lo salvi
anno = int(input("Inserisci l'anno: ")) #Chiedi l'anno e lo salvi

giorni_per_mese = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] #Crei un array per salvare quanti giorni hai per ogni mese che poi userai per calcolare l'anno bisestile

# controllo anno bisestile
if (anno % 4 == 0 and anno % 100 != 0) or (anno % 400 == 0): #anno % 4 == 0 | Controlla se l’anno è divisibile per 4 (2024 % 4 == 0 (e' divisibile))
    giorni_per_mese[1] = 29  # febbraio                      #anno % 100 != 0 | Serve a escludere gli anni come 1900, 2100
                                                             #anno % 400 == 0 Eccezione all’eccezione. Gli anni divisibili per 400 SONO bisestili
giorni_passati = 0 #variabile che si segna i giorni passati

# ciclo sui mesi precedenti
for i in range(mese - 1): #partiamo dal fatto che il for serve a ripetere delle istruzioni un certo numero di volte. In questo caso il for scorre i mesi uno alla volta e somma i giorni di ciascun mese precedente a quello inserito. 
    giorni_passati += giorni_per_mese[i] #aggiungo al totale i giorni del mese corrente del ciclo

# aggiungo il giorno del mese corrente
giorni_passati += giorno #serve a contare anche i giorni del mese corrente, non solo quelli dei mesi precedenti.

print("Giorni passati dal 1° gennaio:", giorni_passati) #stampa del risultato