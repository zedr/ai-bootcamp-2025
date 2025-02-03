# BONUS: esercizio n.2 opzioale per mercoledì 5
Estendere il programma della rubrica implementando le seguenti funzionalità:
 1. Linea di comando
 2. Salvataggio e caricamento del database su un file in formato JSON

## Linea di comando
Una volta eseguito il file [`main.py`](main.py), l'utente si troverà in una
modalità interattiva che gli permetterà di eseguire i seguenti comandi.

### Help

    > h
    Comands:
        a (person|business)     Add
        f <text>                Find
        s <path>                Save (JSON)
        l <path>                Load (JSON)

### Aggiunta (add) di un record Persona

    > a person
    ? Name: Margaret
    ? Surname: Hamilton
    ? Phone: 01-234-567

### Aggiunta (add) di un record Business

    > a business
    ? Name: Vedrai
    ? Phone: +39-333-3333333

### Ricerca di un record

    > f vedrai
    person: name="Vedrai" phone="+39-333-333333"
    > f mistral
    ! not found
    > f margaret
    business: name="Margaret" surname="Hamilton" phone="01-234-567"