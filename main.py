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

truck1.load(["13","14","15","16","19","20","21","26","27","34","35","39"])



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

dist_now = get_distances(location_now)
hub = float(dist_now["HUB"])
truck1_dist1 += hub

truck1.current = [None] * 8
truck1.load(["2","3", "7","8","10","29","30","33"])

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
    truck1_dist2 += min_dist
    location_now = next

truck2.current = [None] * 8
truck2.load(["1","4","11","18","22", "23", "28", "40"])

next = ""
location_now = "HUB"
ind = 0
for i in range(len(truck2.current)):
    if truck2.current == []:
        break
    min_dist = 1000000.0
    dist_now = get_distances(location_now)
    for pack_ind in truck2.current:
        obj = pack_table.search(pack_ind)
        if float(dist_now[obj.address]) < min_dist:
            min_dist = float(dist_now[pack_table.search(pack_ind).address])
            next = pack_table.search(pack_ind).address
            ind = pack_ind
    truck2.current.remove(ind)
    for rem_ind in truck2.current:
        obj = pack_table.search(rem_ind)
        if obj.address == next:
            truck2.current.remove(rem_ind)
    truck2_dist1 += min_dist
    location_now = next

dist_now = get_distances(location_now)
hub = float(dist_now["HUB"])
truck2_dist1 += hub

truck2.current = [None] * 12
truck2.load(["5","6","9","12","17", "24", "25", "31", "32", "36", "37","38"])


next = ""
location_now = "HUB"
ind = 0
for i in range(len(truck2.current)):
    if i == 7:
        i = i
    if truck2.current == [] or all(v is None for v in truck2.current) == True:
        break
    min_dist = 1000000.0
    dist_now = get_distances(location_now)
    for pack_ind in truck2.current:
        obj = pack_table.search(pack_ind)
        if obj != None:
            if float(dist_now[obj.address]) < min_dist:
                min_dist = float(dist_now[pack_table.search(pack_ind).address])
                next = pack_table.search(pack_ind).address
                ind = pack_ind
    truck2.current.remove(ind)
    rem_ind = 0
    while rem_ind < len(truck2.current):
        obj = pack_table.search(truck2.current[rem_ind])
        if obj != None:
            if obj.address == next:
                truck2.current[rem_ind] = None
                rem_ind=1
        rem_ind+=1
    truck2_dist2 += min_dist
    location_now = next


print(truck1_dist1)
print(truck1_dist2)
print(truck2_dist1)
print(truck2_dist2)