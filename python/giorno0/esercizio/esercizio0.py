# Scrivere un programma in Python che stampi a schermo il seguente:
# 1. la scritta "ciao, mondo!"
print("ciao, mondo!\n")
# 2. il risultato della somma dei numeri 40 e 2
somma= 40+2
print("il risultato della somma dei numeri 40 e 2 è: ", somma ,"\n")
# 3. il risultato della divisione del numero 40 per il numero 0 ;)
divisione_float = 40/0     """ZeroDivisionError: division by zero"""
print("il risultato della divisione del numero 40 per il numero 0 è: ", divisione, "\n")
# 3.1 approssimo lo zero per avere un risultato stampabile rispettando i limiti computazionali
divisione_1 = 40/(10**(-300))
print("il risultato della divisione del numero 40 per una approssimazione del numero 0 è: ", divisione_1, "\n")
#BONUS
#Scrivere un altro programma in Python che stampi a schermo il contenuto di questo file `README.md` (Get-Content -path "README.md")
