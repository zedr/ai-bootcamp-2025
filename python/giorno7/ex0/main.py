import csv

with open("data.csv") as fd:
    reader = csv.reader(fd)
    for line in reader:
        print(line)