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
    pack_table.search(ind).status = "Delivered"
    for rem_ind in truck1.current:
        obj = pack_table.search(rem_ind)
        if obj.address == next:
            obj.status = "Delivered"
            truck1.current.remove(rem_ind)
    truck1_dist2 += min_dist
    location_now = next
