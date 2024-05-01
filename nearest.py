from get_distances import get_distances


def nearest(truck, pack_table):
    path = [][]
    next = ""
    location_now = "HUB"
    ind = 0
    total = 0
    for i in range(len(truck.current)):
        if truck.current == [] or all(v is None for v in truck.current) == True:
            break
        min_dist = 1000000.0
        dists_now = get_distances(location_now)
        for pack_ind in truck.current:
            obj = pack_table.search(pack_ind)
            if obj != None:
                this_dist = float(dists_now[obj.address])
                if this_dist < min_dist:
                    min_dist = this_dist
                    next = obj.address
                    ind = pack_ind

        truck.current.remove(ind)
        obj.status = "Delivered"

        rem_ind = 0
        while rem_ind < len(truck.current):
            rem_obj = pack_table.search(truck.current[rem_ind])
            if rem_obj != None:
                if rem_obj.address == next:
                    rem_obj.status = "Delivered"
                    truck.current[rem_ind] = None
                    rem_ind -= 1
            rem_ind += 1
        total += min_dist
        location_now = next