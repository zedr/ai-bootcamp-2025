from main import Country, Region, City

italy = Country("Italy")

assert italy.name == "Italy"

sicily = Region("Sicily")
italy.add(sicily)

sicily.add(City("Catania", pop=300_000))
sicily.add(City("Palermo", pop=600_000))

assert sicily.pop == 900_000

calabria = Region("Calabria")
calabria.add(City("Reggio Calabria", pop=170_000))

italy.add(calabria)
assert italy.pop == 1_170_000

# La correttezza della risposta dipende ovviamente
# dalla quantità e qualità di dati che abbiamo.
assert italy.most_populuous_city.name == "Palermo"