# Esercizio per il giorno venerdì 7
Scrivere un programma in Python che carichi il file CSV [students.csv](students.csv)
e crei una tabella SQLite contententi i dati del file. Fare caso al `delimiter`!

Definire la tabella scegliendo i tipi di campi (datatype) corretti per ciascuna
colonna. Per una colonna va usato un DEFAULT: quale?

Attenzione: il file CSV ha un problema che va sistemato prima di eseguire il programma.

Una volta caricati i dati, estendere il programma in modo che stampi a schermo:
 - gli studenti nati nell'anno 2000
 - la persona che ha consegnato il maggior numero di assignments (usando `MAX()` in SQL o in Python)
 - il cognome delle studentesse di nome "Jane"
 - leggere la [documentazione Python](https://docs.python.org/3/library/sqlite3.html#sqlite3-tutorial)
   e stampare la graduatoria degli studenti ordinati in base al numero di assignment usando `ORDER BY` 
   (non farlo in Python!)

## Bonus
Creare un altro database (con un nome diverso) definendo una seconda tabella con i seguenti campi:
 - id
 - data di consegna di un assignment

Creare due file CSV con la colonna assignment rimossa nella prima tabella `students`. Provare
a replicare i risultati della prima parte dell'esercizio creando dati fittizi e usando
le `JOIN`.