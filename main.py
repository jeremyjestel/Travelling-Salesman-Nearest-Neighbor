#Jeremy Jestel
# Student ID: 011013013

from helpers import reader
from helpers.hash_table import hash_table
from helpers.lookup import at_time, lookup
from helpers.mph import to_str
from nearest import nearest
from classes.truck import truck
print("Welcome to WGUPS Nearest Neighbor delivery system!\n")
while True:
    # read package file in
    pack_file = reader.read_pack()
    # create the hash table
    pack_table = hash_table()
    # instantiate trucks
    truck1 = truck()
    truck2 = truck()
    # populate the table with the pack file
    pack_table.pop_table(pack_file)

    # get the full path of the trucks as they drive and total distances at each point
    loading = ["13", "14", "15", "16", "19", "20", "21", "34", "39", "35", "27"]
    path_1 = nearest(truck1, pack_table, loading, 0.0)
    loading = ["2", "7", "8", "25", "26", "10", "29", "30", "33"]
    path_1.extend(nearest(truck1, pack_table, loading, path_1[-1][1]))
    loading = ["1", "4", "11", "18", "22", "23", "40"]
    path_2 = nearest(truck2, pack_table, loading, 0.0)
    loading = ["5", "37", "38", "9", "3", "6", "12", "17", "24", "31", "32", "36", "28"]
    path_2.extend(nearest(truck2, pack_table, loading, path_2[-1][1]))

    raw = input("\nWhat would you like to do?\nSubmit A to run the algorithm view the path the packages take and at what time they are dropped off: \nSubmit B to lookup a specific time:\nSubmit C to look up a specific package's details:\nSubmit Q to quit this program:\n")
    if raw == "A":
        print("Truck 1:")
        for val in path_1:
            if val[0] == "HUB":
                continue
            print("Package " + val[0] + " was delivered at " + to_str(val[2]))
        print("Truck 2:")
        for val in path_2:
            if val[0] == "HUB":
                continue
            print("Package " + val[0] + " was delivered at " + to_str(val[2]))
        print("The total mileage was " + str(path_1[-1][1] + path_2[-1][1]))
    elif raw == "B":
        time = input("What time would you like to lookup the statuses at, please use HH:MM formatting:")
        # get the full status list
        update_1 = at_time(time, path_1)
        update_2 = at_time(time, path_2)
        update_1.extend(update_2)
        # sort the full status list
        sorted = sorted(update_1, key=lambda x: int(x[0]))
        #print the sorted variable
        for line in sorted:
            print("Package " +line[0] + " is " +  line[1] + " and its delivery time is " + line[2])
        print("Total Mileage Travelled " + str(path_1[-1][1] + path_2[-1][1]))
    elif raw == "C":
        id = input("Lookup a specific package ID:")
        obj = lookup(pack_table, id)
        if obj is None:
            print("Key is incorrect")
        else:
            print("ID: " + obj.id)
            print("Address: " + obj.address)
            print("City: " + obj.city)
            print("Zip: " + obj.zip)
            print("Deadline: " + obj.deadline)
            print("Weight: " + obj.weight)
            print("Status: " + obj.status)
            print("Delivery Time: " + str(to_str(obj.time)))
    elif raw == "Q":
        break





















