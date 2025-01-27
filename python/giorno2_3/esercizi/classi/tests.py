from main import Country, Region, City

# Creo una nuova istanza di paese chiamato "Italy"
italy = Country("Italy")

assert italy.name == "Italy"

# Creo una regione chiamata Sicilia
sicily = Region("Sicily")

# Aggiungo la Sicilia all'Italia
italy.add(sicily)

# Aggiungo alla Sicilia due città
sicily.add(City("Catania", pop=300_000))
sicily.add(City("Palermo", pop=600_000))

# Verifico che la somma della popolazione delle due città siciliane
# sia corretta, andando a guardare l'attributo (una proprietà) chiamata `pop`
assert sicily.pop == 900_000

# Creo un'altra regione...
calabria = Region("Calabria")
# ... e una città
calabria.add(City("Reggio Calabria", pop=170_000))

# Aggiungo la nuova regione all'Italia
italy.add(calabria)

# Infine, guarda un attributo (anch'esso una proprietà)
# sul paese Italia
assert italy.pop == 1_070_000

# La correttezza della risposta dipende ovviamente
# dalla quantità e qualità di dati che abbiamo.
assert italy.most_populuous_city.name == "Palermo"