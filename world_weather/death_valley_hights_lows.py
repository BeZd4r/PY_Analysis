import csv

filename = "data/death_valley_2021_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, collumn_header in enumerate(header_row):
        print(index,collumn_header)