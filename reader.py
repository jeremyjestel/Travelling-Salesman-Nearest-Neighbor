import csv
with open('WGUPS Package File.csv', 'r') as file:
    pack = csv.reader(file)
    for row in pack:
        print(row)

with open('WGUPS Distance Table.csv', 'r') as file:
    dist = csv.reader(file)
    for row in dist:
        print(row)

