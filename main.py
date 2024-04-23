import reader
from hash_table import hash_table
from truck import truck
from package import package

pack_file = reader.read_pack()
dist_file = reader.read_dist()
pack_table = hash_table.hash_table
truck1 = truck.truck()
truck2 = truck.truck()
package1 = package.package(pack_file[0])
print(vars(package1))
packages = [None]*40
i = 0

for row in pack_file:
    packages[i] = package.package(row)
    i += 1

