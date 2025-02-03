# Esercizio n.1 per mercoledì 5
Finire l'esercizio di gruppo (facendosi passare il codice
dai propri compagni di squadra se serve).

Implementare un sistema che chieda, dopo una partita,
al giocatore se vuole continuare a giocare o terminare
il programma.

Implementare un sistema di high-score (tabella punteggi)
che chieda il nome del giocatore quando viene registrato 
un nuovo record, ovvero quando il numero di tentativi 
è inferiore a tutti i precedenti tentativi. Il nome 
viene stampato a schermo quando il programma viene 
terminato dall'utente.

Rendere persistente il high score salvando su file, in
formato JSON oppure CSV (a scelta della programmatrice), 
i dati seguenti:
 - nome del giocatore
 - numero di tentativi fatti
 - data e ora del record

Scrivere il high score quando il programma termina.
Caricare il high score quando il programma viene eseguito.
Il file del high score deve riportare i punteggi in maniera
ordinata e ascendente rispetto al numero tentativi.

# Bonus
Includere, nei dati di ciascun punteggio, anche il tempo,
in secondi intercorso, tra l'inizio della partita ed la fine
(quando il numero è stato indovinato).

Fare riferimento a [questo capitolo](https://docs.python.org/3/library/datetime.html#timedelta-objects) 
della documentazione ufficiale. Cosa si ottiene se si usa la
sottrazione per due oggetti datetime?