from enroute import enroute
from get_distances import get_distances
from mph import miles_time


def nearest(truck, pack_table, loading, offset):
    path = []
    next_loc = ""
    location_now = "HUB"
    ind = 0
    total = offset
    truck.current = [None] * len(loading)
    truck.load(loading)
    enroute(pack_table, truck.current)

    for i in range(len(truck.current)):
        if truck.current == [] or all(v is None for v in truck.current) == True:
            break
        min_dist = 1000000.0
        dists_now = get_distances(location_now)
        for pack_ind in truck.current:
            obj = pack_table.search(pack_ind)
            if obj is not None:
                this_dist = float(dists_now[obj.address])
                if this_dist < min_dist:
                    min_dist = this_dist
                    next_loc = obj.address
                    ind = pack_ind

        total += min_dist
        minutes = miles_time(total)
        path.append([ind, total, minutes])
        truck.current.remove(ind)
        pack_table.search(ind).status = "Delivered"
        location_now = next_loc

        rem_ind = 0
        while rem_ind < len(truck.current):
            rem_obj = pack_table.search(truck.current[rem_ind])
            if rem_obj is not None:
                if rem_obj.address == next_loc:
                    rem_obj.status = "Delivered"
                    path.append([truck.current[rem_ind], total, minutes])
                    truck.current.remove(truck.current[rem_ind])
                    continue
            rem_ind += 1
    dist_now = get_distances(location_now)
    hub = float(dist_now["HUB"])
    total += hub
    path.append(["HUB", total])

    return path
