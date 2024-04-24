import reader
from hash_table import hash_table
from truck import truck
from package import package

pack_file = reader.read_pack()
dist_file = reader.read_dist()

pack_table = hash_table()

truck1 = truck()
truck2 = truck()

i = 0
packages = [None]*40
for row in pack_file:
    packages[i] = package(row)
    pack_table.insert(packages[i].id, packages[i])
    i += 1

for row in dist_file:
    print(row)