import csv
#read the package file
def read_pack():
    with open('data/WGUPS Package File.csv', 'r', encoding='utf-8-sig') as file:
        pack = csv.reader(file)
        rows = []
        for row in pack:
            rows.append(row)
        return rows
#read the distance file
def read_dist():
    with open('data/WGUPS Distance Table.csv', 'r', encoding='utf-8-sig') as file:
        dist = csv.reader(file)
        rows = []
        for row in dist:
            rows.append(row)
        return rows