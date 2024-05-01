from helpers import reader

from helpers.hash_table import hash_table
from helpers.lookup import at_time
from nearest import nearest
from classes.truck import truck

pack_file = reader.read_pack()
pack_table = hash_table()
truck1 = truck()
truck2 = truck()
pack_table.pop_table(pack_file)

loading = ["13","14","15","16","19","20","21","34","39", "35", "27"]
path_1 = nearest(truck1, pack_table, loading, 0.0)
loading = ["2", "7","8", "25","26", "10","29","30","33"]
path_1.extend(nearest(truck1, pack_table, loading, path_1[-1][1]))
loading  = ["1","4","11","18","22", "23", "40"]
path_2 = nearest(truck2, pack_table, loading, 0.0)
loading = ["5", "37", "38", "9","3","6","12","17", "24", "31", "32", "36","28" ]
path_2.extend(nearest(truck2, pack_table, loading, path_2[-1][1]))

update_1 = at_time(pack_table, "8:30", path_1)
update_2 = at_time(pack_table, "8:30", path_2)
update_1.extend(update_2)

sorted = sorted(update_1, key=lambda x:int(x[0]))

for line in sorted:
    print(line)
print(path_1[-1][1] + path_2[-1][1])







