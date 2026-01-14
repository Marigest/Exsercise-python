n = int(input("Inserisci un numero: ")) #chiedi all'utente di inserti un numero da invertire. Il numero viene salvato nella variabile int n

inv = 0 #variabile che ci servira per salvare i numeri che poi andiamo a invertire

while n != 0: #usiamo un while per continuare il ciclo finche' il nostro numero non sara incertito
    inv = inv * 10 + (n % 10) #Questa operazione ci serve per comporre il numero al contrario richiesto dall'utente (n%10: serve a salvarci l'ultimo numero(quello piu a destra))
    n = n // 10 #n//10: serve ad eliminarci l'ultima cifra che abbiamo eliminato prima cosi da salvarci le altre

print(inv) #Stampa il risultato al contrario (Grazie al cabbo (lo so era banale))