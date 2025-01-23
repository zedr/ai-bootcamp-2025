# Esercizio 2 - Funzioni
## Premessa
Scrivere tutto il codice all'interno del modulo [`main.py`](main.py)

## Parte prima
Implementare una funzione chiamata `mydivmod()` che replichi il funzionamento
della funzione *builtin* `divmod()` (senza riutilizzarla!). 
Gestite la divisione per zero *dentro* la funzione.

Per verificare la *signature* della funzione originale, aprire una console Python
e dare il seguente comando:

```
>>> help(divmod)
```

## Parte seconda
Aprire il file [`tests.py`](tests.py) ed implementare nel file [`main.py`](main.py)
le funzioni necessarie per fare passare tutti i test.


## Parte terza - bonus

Se esegui il file [`crash.py`](crash.py) accade un errore strano...

Usa il debugger per capire cosa sta succedendo e tenta di fare passare
l'unico controllo `assert`.