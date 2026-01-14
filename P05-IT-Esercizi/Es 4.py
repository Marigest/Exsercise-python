testo = input("Inserisci una parola o frase: ") # Leggi la stringa dall'utente

testo_pulito = testo.replace(" ", "").lower() # Rimuovi gli spazi e metti tutto in minuscolo. Replace(" ", "") toglie tutti gli spazi mentre lower()converte tutto in minuscolo, così non fa differenza tra maiuscole e minuscole.

# Verifica se il testo pulito è uguale al suo inverso
if testo_pulito == testo_pulito[::-1]: #testo_pulito[::-1] → crea la stringa al contrario.
    print("La stringa è un palindromo!")
else:
    print("La stringa NON è un palindromo.")