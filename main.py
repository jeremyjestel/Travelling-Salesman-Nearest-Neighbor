import reader
from get_distances import get_distances
from hash_table import hash_table
from truck import truck
from package import package

pack_file = reader.read_pack()


pack_table = hash_table()

truck1 = truck()
truck2 = truck()

i = 0
packages = [None]*40
for row in pack_file:
    packages[i] = package(row)
    pack_table.insert(packages[i].id, packages[i])
    i += 1

truck1.load(["1","2","4","5","7","8","10","11","12","13","14","15","16","19","20","21"])
truck2.load(["3","18","36","38","37"])


truck1_dist1 = 0
truck1_dist2 = 0
truck2_dist1 = 0
truck2_dist2 = 0


next = ""
location_now = "HUB"

ind = 0
for i in range(len(truck1.current)):
    if truck1.current == []:
        break
    min_dist = 1000000.0
    dist_now = get_distances(location_now)
    for pack_ind in truck1.current:
        obj = pack_table.search(pack_ind)
        if float(dist_now[obj.address]) < min_dist:
            min_dist = float(dist_now[pack_table.search(pack_ind).address])
            next = pack_table.search(pack_ind).address
            ind = pack_ind
    truck1.current.remove(ind)
    for rem_ind in truck1.current:
        obj = pack_table.search(rem_ind)
        if obj.address == next:
            truck1.current.remove(rem_ind)
    truck1_dist1 += min_dist
    location_now = next



next = ""
location_now = "HUB"
ind = 0
for i in range(len(truck1.current)):
    if truck1.current == []:
        break
    min_dist = 1000000.0
    dist_now = get_distances(location_now)
    for pack_ind in truck1.current:
        obj = pack_table.search(pack_ind)
        if float(dist_now[obj.address]) < min_dist:
            min_dist = float(dist_now[pack_table.search(pack_ind).address])
            next = pack_table.search(pack_ind).address
            ind = pack_ind
    truck1.current.remove(ind)
    for rem_ind in truck1.current:
        obj = pack_table.search(rem_ind)
        if obj.address == next:
            truck1.current.remove(rem_ind)
    total_dist1 += min_dist
    location_now = next
