from helpers.get_distances import get_distances
from helpers.mph import miles_time
def nearest(truck, pack_table, loading, offset):
    #initialize all needed variables and load trucks properly
    path = []
    next_loc = ""
    location_now = "HUB"
    ind = 0
    total = offset
    truck.current = [None] * len(loading)
    truck.load(loading)
    pack_table.enroute(truck.current)
    #repeat for the size of the array of loaded packages
    while True:
        #break the loop if the truck is empty
        if truck.current == [] or all(v is None for v in truck.current) == True:
            break
        min_dist = 1000000.0
        #get all distances from current location
        dists_now = get_distances(location_now)
        #loop over all packages in truck
        for pack_ind in truck.current:
            #retrieve the pacakge
            obj = pack_table.search(pack_ind)
            #if object isnt empty continue
            if obj is not None:
                this_dist = float(dists_now[obj.address])
                #if this distance shorter than lowest found so far set next location variables to this location
                if this_dist < min_dist:
                    min_dist = this_dist
                    next_loc = obj.address
                    ind = pack_ind
        #Add to the total distance
        total += min_dist
        minutes = miles_time(total)
        pack_table.search(ind).time = minutes
        frame = truck.current.copy()
        truck.current.remove(ind)
        #add to path all relevant variables
        path.append([ind, total, minutes, frame])
        pack_table.search(ind).status = "Delivered"
        location_now = next_loc
        rem_ind = 0
        #loop through every package on truck
        while rem_ind < len(truck.current):
            rem_obj = pack_table.search(truck.current[rem_ind])
            if rem_obj is not None:
                if rem_obj.address == next_loc:
                    rem_obj.status = "Delivered"
                    frame = truck.current.copy()
                    rem_obj.time = minutes
                    path.append([truck.current[rem_ind], total, minutes, frame])
                    truck.current.remove(truck.current[rem_ind])
                    continue
            rem_ind += 1
    dist_now = get_distances(location_now)
    hub = float(dist_now["HUB"])
    total += hub
    path.append(["HUB", total, 0.0, []])
    return path
